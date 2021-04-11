from tkinter import *
import os
from pathlib import Path
from Resources import Res
from Windows import PssUI

os.system('clear')
#variables
Path(os.path.join(os.path.join(Path().absolute()),'Data')).mkdir(parents=True, exist_ok=True)
rootUI = Tk()
rootUI.iconbitmap('@' + os.path.join(Path().absolute(), 'logo.xbm'))
appWidth = 600
appHeight = 300
allProcesses = []
rootUI.resizable(False, False)
location = Res.Center(rootUI,appHeight,appWidth)
rootUI.title('Welcome')
rootUI.geometry(f'{appWidth}x{appHeight}+{int(location[0])}+{int(location[1])}')

#close = Queue(1)

def loggerStarter():
    global  statusLabel,allProcesses,startBtn,stopBtn
    Res.loggerStarter(statusLabel, allProcesses,startBtn,stopBtn)

def loggerStoper():
    global allProcesses,statusLabel
    Res.loggerStoper(allProcesses, statusLabel,startBtn,stopBtn)

def closeApp():
    loggerStoper()
    rootUI.destroy()
#widgets
rootUI.protocol("WM_DELETE_WINDOW", closeApp)
welcomeLabel = Label(rootUI, text='Welcome to Textlogger', font='Helvetica 20 bold')
statusLabel = Label(rootUI,text='',font='Helvetica 11')
startBtn = Button(rootUI, text='Start Textlogger',cursor='hand2', bd='5', command=loggerStarter,state='active')
MesurePssBtn = Button(rootUI, text='Measure PSS Value',cursor='hand2', bd='5', command=PssUI.UIStarter)
stopBtn = Button(rootUI, text='Stop Textlogger', bd='5',cursor='hand2', command=loggerStoper,state='disabled')
Label(rootUI,text='Use ( CTRL+ ALT+ H ) to Pause Textlogger',font='Helvetica 10 italic').place(relx=0.30,rely=0.87)
Label(rootUI,text='Use ( CTRL+ ALT+ I ) to Resume Textlogger',font='Helvetica 10 italic').place(relx=0.30,rely=0.92)

#attaching
welcomeLabel.pack()
statusLabel.place(relx=0.373,rely=0.25)
startBtn.place(relx=0.373,rely=0.4)
MesurePssBtn.place(relx=0.363,rely=0.55)
stopBtn.place(relx=0.373,rely=0.70)
rootUI.mainloop()
