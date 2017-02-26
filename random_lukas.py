from objects import *
from create_output import *
import random
from time import time

DEBUG = False

def solve(caches, endpoints, requests, videos, output=True):
    # shuffle requests to acheive different solutions every time
    # random.shuffle(requests)
    if DEBUG:
        print("chaches:", len(caches))
        print("endpoints:", len(endpoints))
        print("requests:", len(requests))
        print("videos:", len(videos))

    requests = sorted(requests, key=lambda x: x.amount, reverse=True)

    ep_to_caches = {}
    for r in requests:
        # find caches connected to the endpoint, sorted by latency
        if r.eid in ep_to_caches:
            possible_caches = ep_to_caches[r.eid]
        else:
            cache_latencies = sorted(endpoints[r.eid].cache_latencies, reverse=True, key=lambda x: x.latency)
            possible_caches = [caches[cl.cid] for cl in cache_latencies]
            ep_to_caches[r.eid] = possible_caches

        # check if the video is already in one of the caches,
        caches_with_vid = [c for c in possible_caches if r.video in c.videos]
        # remove caches that dont have space left
        possible_caches = [c for c in possible_caches if remaining_capacity(c) >= r.video.size]
        if len(caches_with_vid) == 0 and len(possible_caches) > 0:
            # put it in the first cache
            possible_caches[0].videos.add(r.video)

    # done putting all requests
    if output:
        create_output(caches)

    return caches


def remaining_capacity(cache):
    tot_capacity = cache.capacity
    s = 0
    for v in cache.videos:
        s += v.size
    return tot_capacity - s

def score(caches, endpoints, requests, videos):
    """Calculates total latency savings"""
    result = 0
    for endpoint in endpoints:
        for request in endpoint.requests:
            result += (endpoint.latence_to_dc - getLatency(request.video, endpoint.eid, caches, videos, endpoints)) * request.amount
    return result

def getLatency(videoID, endpointID, caches, videos, endpoints):
    """Calculates latency of one video"""
    latencies = []
    # First we push the latency from the data center
    latencies.append(endpoints[endpointID].latence_to_dc)
    # Now we query the latencies per cache server, we add nothing if the video is not cached
    # print(endpoints[endpointID].cache_latencies_dict)
    for cacheServer in endpoints[endpointID].cache_latencies:
        # We check if the video is cached in a server
        if(videoID in caches[cacheServer.cid].videos):
            latencies.append(endpoints[endpointID].cache_latencies_dict[cacheServer.cid].latency)
    # Worst case it returns latency to the DC
    return min(latencies)
