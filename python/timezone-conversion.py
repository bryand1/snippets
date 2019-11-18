import datetime

import pytz   # not part of standard library

dt = datetime.datetime.utcnow()
dt_utc = dt.replace(tzinfo=pytz.utc)
dt_est = dt_utc.astimezone(pytz.timezone('America/New_York'))
