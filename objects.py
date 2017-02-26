from collections import namedtuple

Video = namedtuple("Video", ["vid", "size"])


class Cache(namedtuple("Cache", ["cid", "capacity", "videos"]) ): # videos is an empty list at the beginning

    def output_format(self):
        s = str(self.cid)
        for v in self.videos:
            s += " "+str(v.vid)
        return s

CacheLatency = namedtuple("CacheLatency", ["cid", "latency"])

Request = namedtuple("Request", ["video", "amount", "eid"])

EndPoint = namedtuple("EndPoint", ["eid", "latence_to_dc", "cache_latencies", "cache_latencies_dict", "requests"])
