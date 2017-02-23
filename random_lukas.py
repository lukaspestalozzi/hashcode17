from objects import *
from create_output import *
import random

DEBUG = False

def solve(caches, endpoints, requests, videos):
    # shuffle requests to acheive different solutions every time
    random.shuffle(requests)
    if DEBUG:
        print("chaches:", len(caches))
        print("endpoints:", len(endpoints))
        print("requests:", len(requests))
        print("videos:", len(videos))

    requests = sorted(requests, key=lambda x: x.amount, reverse=True)

    ep_to_caches = {}
    for r in requests:
        # find caches connected to the endpoint
        if r.eid in ep_to_caches:
            possible_caches = ep_to_caches[r.eid]
        else:
            possible_caches = [caches[cl.cid] for cl in endpoints[r.eid].cache_latencies]
            ep_to_caches[r.eid] = possible_caches

        # if the video is already in one of the caches, dont add it again
        can_be_added = True
        for c in possible_caches:
            if r.video.vid in [v.vid for v in c.videos]:
                can_be_added = False

        if can_be_added:
            # find cache that has enough space left
            found = False
            for c in possible_caches:
                if (remaining_capacity(c) >= r.video.size
                    and r.video.vid not in [v.vid for v in c.videos]):
                    c.videos.add(r.video)
                    found = True
                    break
            # done putting video in cache
    # done putting all requests
    create_output(caches)

    return caches


def remaining_capacity(cache):
    tot_capacity = cache.capacity
    s = 0
    for v in cache.videos:
        s += v.size
    return tot_capacity - s
