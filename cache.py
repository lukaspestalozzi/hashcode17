from sys import stdin
from objects import *
from random_lukas import *
from greedyCarlos import *

'''
    Use 'cat input.in | python thisscript.py' to execute
'''

# read the file v2
infile = stdin
line = infile.readline()
# Save problem parameters
v, e, r, c, x = list(map(int, line.split(" ")))

# advance to video sizes
line = infile.readline()
videos = []
videosizes = list(map(int, line.split(" ")))
for i in range(0, len(videosizes)):
    videos.append(Video(i, videosizes[i]))

# advance to endpoints
line = infile.readline()

endpoints = []
for i in range(0, e):
    l, k = list(map(int, line.split(" ")))
    line = infile.readline()

    # create cache latencies list
    cachelatencies = []
    for j in range(0, k):
        c, lc = list(map(int, line.split(" ")))
        cachelatencies.append(CacheLatency(c, lc))
        line = infile.readline()

    # Add endpoint
    endpoints.append(EndPoint(i, l, cachelatencies, []))

# advance to request descriptions
line = infile.readline()
requests = []
for i in range(0, r):
    rv, re, rn = list(map(int, line.split(" ")))
    req = Request(videos[rv], rn, re)
    endpoints[re].requests.append(req)
    requests.append(req)
    line = infile.readline()

# create list of caches
caches = []
for i in range(0, c):
    caches.append(Cache(i, x, []))


solve(caches, endpoints, requests, videos)
