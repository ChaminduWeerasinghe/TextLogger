from pynput.keyboard import Key, Listener, GlobalHotKeys
from os import path
from datetime import datetime
import threading
import Writer
from queue import Queue
from Windows import PopUI

List_of_Lists = []
fileLocation = "Data/Keypress.csv"
HotkeyStatus = 0
queue = Queue(maxsize=1)
fatigueLevel = 'NA'

def on_press(event):
    global HotkeyStatus
    if HotkeyStatus == 0 :
        threading.Thread(target=Writer.rawfileWriter().write_rawfile,args=('Data/RawKeystokes.csv',event,'Pressed',datetime.now(),)).start()
        Check_Availability()
        global List_of_Lists
        if not isExist(List_of_Lists,event):
            List_of_Lists.append(list([event,str(datetime.now()),'','']))

def setFatigueLevel():
    global fatigueLevel,queue
    if not queue.empty():
        fatigueLevel = queue.get()

def on_release(event):
    global HotkeyStatus
    if HotkeyStatus == 0:
        global List_of_Lists
        setFatigueLevel()
        threading.Thread(target=Writer.rawfileWriter().write_rawfile, args=('Data/RawKeystokes.csv', event, 'Released', datetime.now(),)).start()
        for list in List_of_Lists:
            if list[0]==event:
                list[2]=str(datetime.now())
                list[3]=fatigueLevel
                thred =  threading.Thread(target=Writer.Write().write_file, args=(list,fileLocation,))
                thred.start()
                List_of_Lists.remove(list)
    elif HotkeyStatus == 1:
        List_of_Lists = []


def on_Pause():
    global List_of_Lists
    global HotkeyStatus
    List_of_Lists = []
    print('pause')
    HotkeyStatus = 1

def on_Resume():
    global HotkeyStatus
    global List_of_Lists
    HotkeyStatus = 0
    List_of_Lists = []
    print('resume')

def isExist(listOFlist,key):
    for list in listOFlist:
        if list[0]==key:
            return True
    return False


def Check_Availability():
    if not path.exists(fileLocation):
        f = open(fileLocation,"w")
        f.close()
        firstList = ['key','keydown_time','keyup_time','fatigue level']
        thread1 = threading.Thread(target=Writer.Write().write_file, args=(firstList,fileLocation,))
        thread1.start()


KeyboardListner =  Listener(on_press=on_press, on_release=on_release)
HotKeyListner = GlobalHotKeys({'<ctrl>+<alt>+h':on_Pause,'<ctrl>+<alt>+i': on_Resume})

def startPopup():
    threading.Thread(target=PopUI.PopUIStarter, args=('PopUIThread',queue)).start()

def starter():
    startPopup()
    KeyboardListner.start()
    HotKeyListner.start()
    KeyboardListner.join()
    HotKeyListner.join()
