from collections import namedtuple

Video = namedtuple("Video", ["vid", "size"])


class Cache(namedtuple("Cache", ["cid", "capacity", "videos"]) ): # videos is an empty list at the beginning

    def __str__(self):
        s = str(self.cid)
        for v in self.videos:
            s += " "+str(v.vid)
        return s

Request = namedtuple("Request", ["video", "amount", "eid", 'maxsaving'])

EndPoint = namedtuple("EndPoint", ["eid", "latence_to_dc", "latency_savings", "requests"])
