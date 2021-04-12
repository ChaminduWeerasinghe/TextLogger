import multiprocessing
import Logger as logger

def loggerStarter(statusLabel,allProcesses,startBtn,stopBtn):
    loggerProcess = multiprocessing.Process(target=logger.starter)
    loggerProcess.start()
    allProcesses.append(loggerProcess)
    if loggerProcess.is_alive():
        print('Logger Starts')
        statusLabel['text'] = 'Text Logger Stated!'
        startBtn['state']= 'disabled'
        stopBtn['state'] = 'active'

def loggerStoper(allProcesses,statusLabel,startBtn,stopBtn):
    for process in allProcesses:
        process.terminate()
        print('Logger Stops')
        statusLabel['text'] = 'Text Logger Stopped!'
        stopBtn['state']= 'disabled'
        startBtn['state'] = 'active'

def Center(window,appHeight,appWidth):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    xlocation = (screenWidth / 2) - (appWidth / 2)
    ylocation = (screenHeight / 2) - (appHeight / 2)
    arr = [xlocation,ylocation]
    return arr



