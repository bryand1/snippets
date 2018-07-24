import gevent.monkey
from urllib.request import urlopen
gevent.monkey.patch_all()

urls = [
    "http://www.google.com",
    "http://www.yandex.ru",
    "http://www.python.org",
]


def fetch(url):
    resp = urlopen(url).read()
    print(len(resp))


jobs = [gevent.spawn(fetch, url) for url in urls]
gevent.wait(jobs)
