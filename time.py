import time
import datetime
a=datetime.datetime.today()
for i in range(200):
    print "."
#time.sleep(120)
b=datetime.datetime.today()
print b-a
