#!/usr/bin/env python
import urllib2
import json
import matplotlib.pyplot as plt
import datetime as dt

data_url = "http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94576.json"

response = urllib2.urlopen(data_url)
data = response.read()

# observations -> data -> lots of hunks
data = json.loads(data)

dates = []
temps = []

for d in data["observations"]["data"]:
    dates.append(dt.datetime.strptime(d["local_date_time_full"], '%Y%m%d%H%M%S'))
    temps.append(d["apparent_t"])

plt.plot(dates, temps)
plt.gcf().autofmt_xdate()
plt.show()
