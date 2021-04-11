from threading import Thread
from os import path
import pytz
from datetime import datetime

class Write(Thread):
    def write_file(self, list, filename):
        with open(filename, "a") as file:
            i = 0
            for elemnt in list:
                i += 1
                if i == 1:
                    key = str(elemnt).replace("'", '')
                    key = str(key).replace("Key.",'')
                    file.write(key)
                else:
                    file.write(str(elemnt))
                if i < 3:
                    file.write(str(","))
            file.write("\n")


class ScroreWriter():
    @staticmethod
    def write_file(score, filLocation):
        if not path.exists(filLocation):
            print('came')
            f = open(filLocation, "w")
            f.write('Time,Score\n')
            f.write(str(datetime.now(tz=pytz.utc)) + ',' + score)
            f.close()
        else:
            f = open(filLocation, 'a')
            f.write("\n")
            f.write(str(datetime.now(tz=pytz.utc)) + ',' + score)
            f.close()