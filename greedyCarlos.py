from objects import *
from create_output import *

def getRemainingCapacity(cache, videos):
    used = 0
    for video in cache.videos:
        used += video.size
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
    #print(endpoints[endpointID].cache_latencies_dict)
    for cacheServer in endpoints[endpointID].cache_latencies:
        #We check if the video is cached in a server
        if(videoID in caches[cacheServer.cid].videos):
            latencies.append(endpoints[endpointID].cache_latencies_dict[cacheServer.cid].latency)
    #Worst case it returns latency to the DC
    return min(latencies)

def getTotalLatencySavings(caches, videos, endpoints):
    """Calculates total latency savings"""
    result = 0
    for endpoint in endpoints:
        for request in endpoint.requests:
            result += (endpoint.latence_to_dc - getLatency(request.video,endpoint.eid, caches, videos, endpoints)) * request.amount
    return result

def solveC(caches, endpoints, requests, videos):
    """Comment"""
    #Best would be to sort the request before

    sortedRequests = sorted(requests, key = lambda x: x.amount*endpoints[x.eid].latence_to_dc)
    reversed(sortedRequests)

    for request in sortedRequests:
        if(getLowestLatency(request.video,request.eid, caches, videos, endpoints) != getLatency(request.video,request.eid, caches, videos, endpoints)):
            mIdx = 0
            minim=endpoints[request.eid].latence_to_dc
            for cacheServer in endpoints[request.eid].cache_latencies:
                if(minim > cacheServer.latency):
                    minim =  cacheServer.latency
                    #print("Possible improvement in cache server",cacheServer.cid)
                    mIdx = cacheServer.cid
            if(getRemainingCapacity(caches[mIdx], videos) > request.video.size):
                caches[mIdx].videos.add(request.video)
    #printgetTotalLatencySavings(caches,videos,endpoints)
    create_output(caches)