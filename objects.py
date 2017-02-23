from collections import namedtuple

Video = namedtuple("Video", ["vid", "size"])

Cache = namedtuple("Cache", ["cid", "capacity", "videos"])

CacheLatency = namedtuple("CacheLatency", ["cid", "latency"])

Request = namedtuple("Request", ["video", "amount", "eid"])

EndPoint = namedtuple("EndPoint", ["eid", "latence_to_dc", "cache_latencies", "caches", "requests"])
