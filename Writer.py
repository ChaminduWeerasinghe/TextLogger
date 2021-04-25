from threading import Thread
from os import path
from datetime import datetime

class Write(Thread):
    def write_file(self, list, filename):
        with open(filename, "a") as file:
            i = 0
            dataToPrint = ''
            for elemnt in list:
                i += 1
                if i == 1:
                    key = str(str(elemnt).replace("'", '')).replace("Key.",'')
                    dataToPrint = key
                else:
                    dataToPrint = dataToPrint+','+elemnt
            file.write(dataToPrint)
            file.write("\n")

class rawfileWriter(Thread):
    def write_rawfile(self,filename,event,eventType,time,fatigueScore):
        key = str(str(event).replace("'", '')).replace("Key.", '')
        dataToWrite = key + ',' + eventType + ',' + str(time) + ',' + fatigueScore
        if not path.exists(filename):
            f = open(filename, "w")
            f.write('key,event_type,time,fatigue_score\n')
            f.write(dataToWrite+'\n')
            f.close()
        else:
            f = open(filename, "a")
            f.write(dataToWrite+'\n')
            f.close()





class ScroreWriter():
    @staticmethod
    def write_file(score, filLocation):
        if not path.exists(filLocation):
            f = open(filLocation, "w")
            f.write('Time,Score\n')
            f.write(str(datetime.now()) + ',' + score)
            f.close()
        else:
            f = open(filLocation, 'a')
            f.write("\n")
            f.write(str(datetime.now()) + ',' + score)
            f.close()
