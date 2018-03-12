import urllib.request
from functools import lru_cache


def web_lookup_old_school(url, saved={}):
    if url in saved:
        return saved[url]
    with urllib.request.urlopen(url) as req:
        page = req.read()
        saved[url] = page
        return page


@lru_cache(maxsize=32)
def web_lookup_modern(url):
    with urllib.request.urlopen(url) as req:
        return req.read()
