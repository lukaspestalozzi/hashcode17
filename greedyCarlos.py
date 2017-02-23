from objects import *

def getLatency(videoID,endpointID, caches, videos, endpoints):
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

def solve(caches, endpoints, requests, videos):