from objects import *

def getLatency(videoID,endpointID, caches, videos, endpoints):
    latencies = []
    #First we push the latency from the data center
    latencies.append(endpoints[endpointID].latence_to_dc)
    #Now we query the latencies per cache server, we add nothing if the video is not cached
    for cache
    return result


def solve(caches, endpoints, requests, videos):
    
    
