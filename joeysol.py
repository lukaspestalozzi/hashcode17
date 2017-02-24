from objects import *
from create_output import *

def getCapacity(cache):
    curCapacity = cache.capacity
    for video in cache.videos:
        curCapacity -= video.size
    return curCapacity

def solveJ(caches, endpoints, requests, videos):
    for request in reversed(sorted(requests, key=lambda x: x.amount)):
        savings = endpoints[request.eid].latency_savings
        cached = False
        while len(savings.keys()) and not cached:
            closest = max(savings, key=lambda key: savings[key])
            if getCapacity(caches[closest]) < request.video.size:
                # remove cache with insufficient capacity
                del savings[closest]
            else:
                # store video
                caches[closest].videos.add(request.video)
                cached = True

    create_output(caches)
