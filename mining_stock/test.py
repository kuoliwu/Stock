#import pandas as pd
import datetime

s = datetime.datetime.strptime("2016/12/20 21:12:22",  "%Y/%m/%d %H:%M:%S")

d = datetime.datetime.now().strftime('%Y%m%d%H%M%S_SimulateResult')

print (s)

s+=datetime.timedelta(hours=1)

print (s)

print (d)
#t = d-s
#print (d>s)
