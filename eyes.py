from PIL import ImageGrab
from PIL import Image
import time
import datetime
import os
i=0
size = 1360,768#900,508#980, 950
while True:
    time.sleep(0.5)
    a= str(datetime.datetime.today())
    s=''
    for i in range(len(a)):
        if a[i] not in [':']:
            s=s+str(a[i])
        else:
            s=s+';'
    im=ImageGrab.grab()

    im.thumbnail(size)
    im.save('C:\\Brother\\capture'+str(s)+".jpeg", "jpeg")
    try:
        a=open('D:\\cmd.txt','r')
        b=a.read()
        a.close()
        if 'stop' in b:
            break
        else:
            pass
    except:
        pass
    i=i+1
