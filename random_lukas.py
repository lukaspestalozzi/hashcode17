from objects import *

def solve(caches, endpoints, requests, videos):
    for r in requests:
        # find cache that has enough space left
