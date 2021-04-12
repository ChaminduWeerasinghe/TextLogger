from Helper import Res
from tkinter import *
import threading
import Writer

Q1 = 'In the last month, how often have you been upset because of something that happened unexpectedly ?'
Q2 = 'In the last month, how often have you felt that you were unable to control the important things in your life ?'
Q3 = 'In the last month, how often have you felt nervous and stressed ?'
Q4 = 'In the last month, how often have you felt confident about your ability to handle your personal problems ?'
Q5 = 'In the last month, how often have you felt that things were going your way ?'
Q6 = 'In the last month, how often have you found that you could not cope with all the things that you had to do ?'
Q7 = 'In the last month, how often have you been able to control irritations in your life ?'
Q8 = 'In the last month, how often have you felt that you were on top of things ?'
Q9 = 'In the last month, how often have you been angered because of things that happened that were outside of your ' \
     'control ? '
Q10 = 'In the last month, how often have you felt difficulties were piling up so high that you could not overcome ' \
      'them ? '


Ans1 = '0 - Never'
Ans2 = '1 - Almost Never'
Ans3 = '2 - Sometimes'
Ans4 = '3 - Fairly Often'
Ans5 = '4 - Very Often'

filLocation = 'Data/Scores.csv'

pssUI = None

OMresult = []
CalcBtn = None
Total = 0
ResultLabel = None
StressLabel = None
CloseBtn = None

def UIStarter():
    global pssUI
    pssUI = Tk()
    pssUI.resizable(False, False)
    appWidth = 1200
    appHeight = 400
    location = Res.Center(pssUI, appHeight, appWidth)
    pssUI.title('Measure Stress Using PSS')
    pssUI.geometry(f'{appWidth}x{appHeight}+{int(location[0])}+{int(location[1])}')
    createWidgets()


def createWidgets():
    global Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, pssUI, CalcBtn, OMresult,ResultLabel,StressLabel,CloseBtn
    QuestionArr = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10]
    yVal = 0.1
    Label(pssUI, anchor="w", text="~Let's Check Your Current Stress Value~", font='Helvetica 16 bold').place(relx=0.2, rely=0.01)
    CalcBtn = Button(pssUI, text="Let's Measure Value!", bd='5', cursor='hand2', state='disabled', command=calcSore)
    CloseBtn = Button(pssUI, text="Close", bd='5', cursor='hand2', command=pssUI.destroy)
    StressLabel = Label(pssUI, anchor="w", text="", font='Helvetica 14 bold')
    ResultLabel = Label(pssUI, anchor="w", text="", font='Helvetica 12 italic')

    ResultLabel.place(relx=0.5, rely=0.92)
    StressLabel.place(relx=0.7, rely=0.92)
    CloseBtn.place(relx=0.2, rely=0.9)
    CalcBtn.place(relx=0.3, rely=0.9)

    for i in range(0, 10):
        var = StringVar(pssUI)
        var.set('Please Select')
        OMresult.append(var)
        Label(pssUI, anchor="w", text=QuestionArr[i], font='Helvetica 12 bold').place(relx=0.01, rely=yVal)
        OptionMenu(pssUI, var, '0 - Never', '1 - Almost Never', '2 - Sometimes', '3 - Fairly Often', '4 - Very Often',command=validate).place(relx=0.8, rely=(yVal - 0.02))
        yVal += 0.08




def validate(event):
    global OMresult
    count = 0
    for var in OMresult:
        if not var.get() == 'Please Select':
            count = count + 1
        if count == 10:
            CalcBtn['state'] = 'active'
            break


def calcSore():
    global OMresult,Total,ResultLabel
    Answer = []
    for var in OMresult:
        Answer.append(getScore(var.get()))
    Answer[4] = getChagedScore(Answer[4])
    Answer[5] = getChagedScore(Answer[5])
    Answer[7] = getChagedScore(Answer[7])
    Answer[8] = getChagedScore(Answer[8])

    for result in Answer:
        Total = result + Total
    ResultLabel['text'] = 'Your PSS Value is Value is : '+str(Total)

    stressLevel = ''
    if Total <= 13:
        stressLevel = 'Low'
        if not Total == 0:
            storeNClean(stressLevel)
            Total = 0
    elif Total >= 14 & Total <= 26:
        stressLevel = 'Moderate'
        if not Total == 0:
            storeNClean(stressLevel)
            Total = 0
    elif Total >= 27 & Total <=40:
        stressLevel = 'High'
        if not Total == 0:
            storeNClean(stressLevel)
            Total = 0


def storeNClean(stressLevel):
    global  CalcBtn,OMresult
    StressLabel['text'] = 'You are in ' + stressLevel + ' Stress Level'
    thread = threading.Thread(target=saveScore, args=(stressLevel,))
    thread.start()
    for var in OMresult:
        var.set('Please Select')
    CalcBtn['state']='disabled'

def getChagedScore(score):
    if score == 0:
        return 4
    elif score == 1:
        return 3
    elif score == 2:
        return 2
    elif score == 3:
        return 1
    elif score == 4:
        return 0


def getScore(text):
    if text == Ans1:
        return 0
    elif text == Ans2:
        return 1
    elif text == Ans3:
        return 2
    elif text == Ans4:
        return 3
    elif text == Ans5:
        return 4


def saveScore(score):
    global filLocation
    Writer.ScroreWriter.write_file(score,filLocation)



