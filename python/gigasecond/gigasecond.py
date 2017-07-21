from datetime import datetime
import math, time, calendar

def add_gigasecond(dt):
    return datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(int(calendar.timegm(dt.utctimetuple())) + pow(10,9))),"%Y-%m-%d %H:%M:%S")