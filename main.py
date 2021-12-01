'''Python file to continously compute CSV files'''
import os
from file.writeLog import Writing


def logging(path="input",done='done',loop=True):
    '''start of watch folder'''
    f_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),path)
    print("running")
    while True:
        for file in [f for f in os.listdir(f_path) if f.endswith('.csv')]:
            f_i=os.path.join(f_path,file)
            print("Processing "+f_i)
            Writing.writeL(f_i)
            os.replace(f_i,os.path.join(os.path.dirname(os.path.abspath(__file__)),done,file))
        if not loop:
            break

if __name__ == "__main__":
    logging()
