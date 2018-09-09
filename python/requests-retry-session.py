# Best practice for request retries
# https://www.peterbe.com/plog/best-practice-with-retries-with-requests 

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

"""
Testing the Solution
"""
import time

t0 = time.time()
try:
    response = requests_retry_session().get(
        'http://localhost:9999',
    )
except Exception as x:
    print('It failed :(', x.__class__.__name__)
else:
    print('It eventually worked', response.status_code)
finally:
    t1 = time.time()
    print('Took', t1 - t0, 'seconds')

"""
Works In Conjunction With timeout
"""
t0 = time.time()
try:
    response = requests_retry_session().get(
        'http://httpbin.org/delay/10',
        timeout=5
    )
except Exception as x:
    print('It failed :(', x.__class__.__name__)
else:
    print('It eventually worked', response.status_code)
finally:
    t1 = time.time()
    print('Took', t1 - t0, 'seconds')


"""
Works For 500ish Errors Too
"""
t0 = time.time()
try:
    response = requests_retry_session().get(
        'http://httpbin.org/status/500',
    )
except Exception as x:
    print('It failed :(', x.__class__.__name__)
else:
    print('It eventually worked', response.status_code)
finally:
    t1 = time.time()
    print('Took', t1 - t0, 'seconds')

