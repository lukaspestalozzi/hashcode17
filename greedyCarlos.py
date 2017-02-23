from objects import *

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