from file.writeLog import Writing
import os

def logging(path="input",done='done',loop=True):
    f_path = os.path.join(os.getcwd(),path)
    print("running")
    while True:
        for file in [f for f in os.listdir(f_path) if f.endswith('.csv')]:
            fi=os.path.join(f_path,file)
            print("Processing "+fi)
            Writing.writeL(fi)
            os.replace(fi,os.path.join(os.getcwd(),done,file))
        if not loop:
            break

if __name__ == "__main__":
    logging()