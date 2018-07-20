import eventlet
requests = eventlet.import_patched('requests')

urls = [
    "http://www.google.com/intl/en_ALL/images/logo.gif",
    "http://python.org/images/python-logo.gif",
    "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif",
]


def fetch(url):
    return requests.get(url)


pool = eventlet.GreenPool()
for resp in pool.imap(fetch, urls):
    print(resp.status_code, resp.url, len(resp.text))
