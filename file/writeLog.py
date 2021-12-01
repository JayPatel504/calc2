'''Writing results to log file'''
#pylint: disable=E0401,E0213,E1101,R0903,R1732,C0103,C0301
import time
from file.readCSV import Reading


class Writing:
    '''Writing Class'''
    def writeL(path):
        '''Writing out'''
        filename = path.split('/')[-1]
        new_path = '/'.join(path.split('/')[:-2])
        file_g = open(new_path+"/results/"+filename+"_log.txt","w",encoding="utf-8")
        file_b = open(new_path+"/results/"+filename+"_logError.txt","w",encoding="utf-8")
        oper, hist = Reading.read(path)
        for i,row in enumerate(hist):
            if row.get_result() == "Can't divide by zero":
                file_b.write(str(i+1)+","+filename+'\n')
            else:
                file_g.write(str(int(time.time()))+','+filename+','+str(i+1)+','+oper+','+str(row.get_result())+'\n')
        file_g.close()
        file_b.close()
