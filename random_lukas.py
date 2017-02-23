from objects import *
from create_output import *
import random

def solve(caches, endpoints, requests, videos):
    # shuffle requests to acheive different solutions every time
    random.shuffle(requests)

    for r in requests:
        # find cache that has enough space left
        found = False
        for c in caches:
            if remaining_capacity(c) >= r.video.size and r.video.vid not in [v.vid for v in c.videos]:
                c.videos.add(r.video)
                found = True
                break
        # done putting video in cache
    # done putting all requests
    create_output(caches)

    return caches

def remaining_capacity(cache):
    tot_capacity = cache.capacity
    s = 0
    for v in cache.videos:
        s += v.size
    return tot_capacity - s
