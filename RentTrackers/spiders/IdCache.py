import json
import os


class IdCache:
    """
    Cache for storing ids that have been encountered during scraping.
    Ids are dropped from the cache after they are not seen multiple times in a row.
    """

    def __init__(self, path):
        self.path = path
        self.cache = {}
        self.__load_cache__()

    def add(self, e):
        self.cache[e] = -1

    def contains(self, e):
        if e in self.cache:
            self.cache[e] = -1
            return True
        else:
            return False

    def __load_cache__(self):
        if os.path.isfile(self.path):
            with open(self.path, "r") as f:
                cache = json.load(f)
                self.cache = {int(k): v for k, v in cache.items()}

    def write_cache(self):
        new_cache = {post_id: n + 1 for post_id, n  in self.cache.items() if n < 10}
        with open(self.path, "w") as f:
            json.dump(new_cache, f, indent=0)
