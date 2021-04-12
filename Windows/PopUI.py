from tkinter import *
from Helper import Res
import Writer
import time
import threading

filLocation = 'Data/FatigueScores.csv'
snoozeTime = 10
popUI = None
var = None
submit = True

def PopUIStarter(ThreadName):
    global popUI,submit,snoozeTime
    threading.current_thread().name = ThreadName

    while True:
        if submit:
            submit = False
            time.sleep((snoozeTime * 60))
            popup()

def popup():
    global var, popUI, snoozeTime
    popUI = Tk()
    popWidth = 480
    popHeight = 200

    popUI.resizable(False, False)
    popUI.title('Please Review')
    popUI.resizable(False, False)
    PopLocation = Res.Center(popUI, popHeight, popWidth)
    popUI.protocol("WM_DELETE_WINDOW", onClose)
    popUI.geometry(f'{popWidth}x{popHeight}+{int(PopLocation[0])}+{int(PopLocation[1])}')

    Label(popUI, anchor="w", text="Do you Feel any Fatigue Condition??",
          font='Helvetica 14 bold').place(relx=0.18,rely=0.04)
    Label(popUI, anchor="w", text="(like tiredness, weariness, exhaustion, over-tiredness, drowsiness, somnolence)",
          font='Helvetica 10 italic').place(relx=0.02, rely=0.16)
    Button(popUI, text=' :) -Absolutely No [Low]', cursor='hand2', bd='3',
           command=lambda rslt='Low': SaveNClose(rslt)).place(relx=0.3, rely=0.3)
    Button(popUI, text=' :| -Not Much [Medium]', cursor='hand2', bd='3',
           command=lambda rslt='Medium': SaveNClose(rslt)).place(relx=0.305, rely=0.47)
    Button(popUI, text=' :( -Yah I Really Feel That [High] ', cursor='hand2', bd='3',
           command=lambda rslt='High': SaveNClose(rslt)).place(relx=0.25, rely=0.64)
    var = StringVar(popUI)
    OptionMenu(popUI, var, '15min', '30min', '1hours', '2hours', '3hours', '6hours',).place(relx=0.8, rely=0.83)

    popUI.mainloop()

def onClose():
    global submit, popUI
    submit = True
    popUI.destroy()

def SaveNClose(rslt):
    global var, popUI, filLocation, snoozeTime,submit
    if var.get() == '15min':
        snoozeTime = 15
    elif var.get() == '30min':
        snoozeTime = 30
    elif var.get() == '1hours':
        snoozeTime = 60
    elif var.get() == '2hours':
        snoozeTime = 120
    elif var.get() == '3hours':
        snoozeTime = 180
    elif var.get() == '6hours':
        snoozeTime = 360

    Writer.ScroreWriter.write_file(rslt, 'Data/FatigueScores.csv', )
    submit = True
    popUI.destroy()