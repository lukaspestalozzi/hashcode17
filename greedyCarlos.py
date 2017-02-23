from objects import *
from create_output import *

def getRemainingCapacity(cache, videos):
    used = 0
    for video in cache.videos:
        used += videos[video].size
    return cache.capacity-used

def getLowestLatency(videoID,endpointID, caches, videos, endpoints):
    latencies = []
    latencies.append(endpoints[endpointID].latence_to_dc)
    for cacheServer in endpoints[endpointID].cache_latencies:
        #We check if the video is cached in a server
        latencies.append(cacheServer.latency)
    #Worst case it returns latency to the DC
    return min(latencies)


def getLatency(videoID,endpointID, caches, videos, endpoints):
    """Calculates latency of one video"""
    latencies = []
    #First we push the latency from the data center
    latencies.append(endpoints[endpointID].latence_to_dc)
    #Now we query the latencies per cache server, we add nothing if the video is not cached
    for cacheServer in caches:
        #We check if the video is cached in a server
        if(videoID in cacheServer.videos):
            latencies.append(endpoints[endpointID].cache_latencies[cacheServer.cid].latency)
    #Worst case it returns latency to the DC
    return min(latencies)

def getTotalLatencySavings(caches, videos, endpoints):
    """Calculates total latency savings"""
    result = 0
    for endpoint in endpoints:
        for request in endpoint.requests:
            result += (endpoint.latence_to_dc - getLatency(request.video,endpoint.eid, caches, videos, endpoints)) * request.amount
    return result

def solve(caches, endpoints, requests, videos):
    """Comment"""
    #print(getLatency(0,0, caches, videos, endpoints))
    print("The latency savings are", getTotalLatencySavings(caches, videos, endpoints))
    print("Trying to move videos to cache...")
    #Best would be to sort the request before
    for request in requests:
        if(getLowestLatency(request.video,request.eid, caches, videos, endpoints) != getLatency(request.video,request.eid, caches, videos, endpoints)):
            mIdx = 0
            minim=endpoints[request.eid].latence_to_dc
            for cacheServer in endpoints[request.eid].cache_latencies:
                if(minim > cacheServer.latency):
                    minim =  cacheServer.latency
                    mIdx = cacheServer.cid
            caches[mIdx].videos.add(request.video)
    print("The new latency savings are", getTotalLatencySavings(caches, videos, endpoints))
    #create_output(caches)