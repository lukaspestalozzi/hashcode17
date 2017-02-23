from collections import namedtuple

Cache = namedtuple("Cache", ["cid", "capacity"])

CacheLatency = namedtuple("CacheLatency", ["cid", "latency"])

Request = namedtuple("Request", ["vid", "amount", "eid"])

EndPoint = namedtuple("EndPoint", ["eid", "cache_latencies", "caches", "requests"])
