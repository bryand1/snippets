import datetime

import pytz   # not part of standard library

dt = datetime.datetime.now()  # Assume we are on the west coast
dt_pst = pytz.timezone('US/Pacific').localize(dt)
dt_est = dt_pst.astimezone(pytz.timezone('US/Eastern'))
