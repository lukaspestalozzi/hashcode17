from objects import *
from create_output import *
import random

def solve(caches, endpoints, requests, videos):
    # shuffle requests to acheive different solutions every time
    random.shuffle(requests)

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
