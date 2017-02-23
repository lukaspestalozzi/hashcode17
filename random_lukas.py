from objects import *
from create_output import *

def solve(caches, endpoints, requests, videos):

    for r in requests:
        # find cache that has enough space left
        found = false
        for c in caches:
            if c.capacity > r.video.size:
                c.videos.append(r.video)
                c.capacity = c.capacity - r.video.size
                found = true
                break
        # done putting video in cache
    # done putting all requests
    return caches
