import pandas as pd
from file.readCSV import Reading
import time

class Writing:
    def writeL(path):
        filename = path.split('/')[-1]
        f = open("results/"+filename+"_log.txt","w")
        fe = open("results/"+filename+"_logError.txt","w")
        op, hist = Reading.read(path)
        for i in range(len(hist)):
            if hist[i].get_result() == "Can't divide by zero":
                fe.write(str(i+1)+ ","+ filename+'\n')
            else:
                f.write(str(int(time.time()))+','+filename+','+str(i+1)+','+op+','+str(hist[i].get_result())+'\n')
        f.close()
        fe.close()
        return 