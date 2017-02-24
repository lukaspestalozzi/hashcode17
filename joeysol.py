from objects import *
from create_output import *

def getCapacity(cache):
    curCapacity = cache.capacity
    for video in cache.videos:
        curCapacity -= video.size
    return curCapacity

def solveJ(caches, endpoints, requests, videos):
    for request in reversed(sorted(requests, key=lambda x: x.maxsaving)):
        savings = endpoints[request.eid].latency_savings
        cached = False
        # check if video is already in a cache that is fairly close
        for cache in savings.keys():
            if request.video in caches[cache].videos and savings[cache] > endpoints[request.eid].mean_cache_latency:
                print("Video skipped, ")
                cached = True
        while len(savings.keys()) and not cached:
            closest = max(savings, key=lambda key: savings[key])
            if getCapacity(caches[closest]) < request.video.size:
                # remove cache with insufficient capacity
                del savings[closest]
                print("Ran out of storage :(")
            else:
                # store video
                caches[closest].videos.add(request.video)
                cached = True

    create_output(caches)
