from objects import *
from create_output import *
import random
from time import time
import random_lukas as rndm
from sys import stderr, stdin

def eprint(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

def solve(caches, endpoints, requests, videos):
    # caches = rndm.solve(caches, endpoints, requests, videos, output=False)
    caches = load_caches_from_file(videos=videos, capacity=caches[0].capacity, filename='outputs/best_trending_today.out')

    sls_sol = sls(caches, endpoints, requests, videos)
    create_output(sls_sol) # , filename='outputs/sls_out.out')
    return sls_sol

def sls(caches, endpoints, requests, videos):
    start_t = time()
    total_request_amount = sum([r.amount for r in requests])

    temp = 0.01
    limit_temp = 0.00001

    iterations = 100
    it_at_limit = iterations*0.9
    decay = (limit_temp / temp)**(1.0/it_at_limit)

    eprint("decay", decay)


    best_score = 0
    all_time_best = 0

    for i in range(iterations):
        # print(temp)
        if i <= 100 or i % 1000 == 0 or i > iterations-2:
            eprint("iteration", i, "temp", temp, "score", best_score, "time", time()-start_t)
        start_t = time()

        # choose random EndPoint
        ep = endpoints[random.randrange(len(endpoints))]
        if len(ep.cache_latencies) <= 0:
            continue # no improvement to be made here

        # choose random cache connected to ep
        cl = ep.cache_latencies[random.randrange(len(ep.cache_latencies))]
        cache = caches[cl.cid]

        # choose random request from ep (and its video)
        req = ep.requests[random.randrange(len(ep.requests))]
        vid = req.video

        # put the video in the cache
        ev = put(vid, cache)
        # # old
        # take random video
        # vid = videos[random.randrange(len(videos))]
        # put it into a random cache
        # cache = caches[random.randrange(len(caches))]
        # ev = put(vid, cache)
        # # end old

        if ev is False or ev is True:
            continue # did not change anything
        else:
            # test whether to keep that arrangement
            sc = score(caches, endpoints, requests, total_request_amount)
            # print("score:", sc)
            if sc > all_time_best:
                all_time_best = sc
                all_time_best_sol = copy_caches(caches)
            if sc > best_score*(1.0-temp):
                # print("score improved! from", best_score, "to", sc)
                best_score = sc
            else:
                # revert changes
                revert(cache, vid, ev)

        # update temp
        temp = max(limit_temp, temp*decay)

    return all_time_best_sol


def copy_caches(caches):
    new_l = []
    for c in caches:
        copy_c = Cache(c.cid, c.capacity, list(c.videos))
        new_l.append(copy_c)
    return new_l

caches_for_ep = {}
def score(caches, endpoints, requests, total_request_amount):

    sc = 0
    for r in requests:
        ep = endpoints[r.eid]
        if r.eid in caches_for_ep:
            cl = caches_for_ep[r.eid] # cl is tuple (cache, latency)
        else:
            cl = [(caches[cl.cid], cl.latency) for cl in ep.cache_latencies]
            caches_for_ep[r.eid] = cl
        ep_latencies = [c_l[1] for c_l in cl if r.video in c_l[0].videos]
        L = min(ep_latencies) if len(ep_latencies) > 0 else ep.latence_to_dc
        sc += r.amount*(ep.latence_to_dc - L)
    return int((sc*1000.0) / total_request_amount)

def load_caches_from_file(videos, capacity, filename):
    # namedtuple("Cache", ["cid", "capacity", "videos"])

    with open(filename) as f:
        caches = []
        nbr_lines = int(f.readline())
        for k in range(nbr_lines):
            line = [int(i) for i in f.readline().strip().split(' ')]
            new_cache = Cache(line[0], capacity, set())
            for vid in line[1:]:
                new_cache.videos.add(videos[vid])
            caches.append(new_cache)
        return caches




def put(video, cache):
    """
    puts the video into the cache. Evicts random videos if there is not enough spaces.
    Does nothing if the video is already in the cache.
    returns a list of evicted videos if the video was placed,
    returns True if the video already was in the cache
    returns False if the video is bigger than the total capacity of the cache.
    """
    if video in cache.videos:
        return True
    if cache.capacity < video.size:
        return False
    evicted = []
    while remaining_capacity(cache) < video.size:
        ev = evict_random_video(cache)
        evicted.append(ev)
    cache.videos.add(video)
    return evicted

def evict_random_video(cache):
    return cache.videos.pop() # TODO make truly random

def revert(cache, video, evicted):
    # print("revert:", cache, video, evicted)
    cache.videos.remove(video)
    for e in evicted:
        cache.videos.add(e)



def remaining_capacity(cache):
    tot_capacity = cache.capacity
    s = 0
    for v in cache.videos:
        s += v.size
    return tot_capacity - s
