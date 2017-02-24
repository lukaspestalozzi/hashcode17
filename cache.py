from sys import stdin
from objects import *
from greedyCarlos import *
from joeysol import *

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
    latencysavings = {}
    for j in range(0, k):
        cid, lc = list(map(int, line.split(" ")))
        # if l > lc -> good
        # biggest value in latencysavings best
        latencysavings[cid] = l - lc
        line = infile.readline()

    # Add endpoint
    endpoints.append(EndPoint(i, l, latencysavings, []))

# advance to request descriptions
requests = []
for i in range(0, r):
    rv, re, rn = list(map(int, line.split(" ")))
    sav = endpoints[re].latency_savings
    maxsaving = -10000000
    if sav:
        maxsaving = max(sav, key=lambda key: sav[key])
    req = Request(videos[rv], rn, re, maxsaving)
    endpoints[re].requests.append(req)
    requests.append(req)
    line = infile.readline()

# create list of caches
caches = []
for i in range(0, c):
    caches.append(Cache(i, x, set()))


solveJ(caches, endpoints, requests, videos)
