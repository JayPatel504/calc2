from file.writeLog import Writing
import os

def main():
    f_path = os.path.join(os.getcwd(),"input")
    print("running")
    while True:
        if len(f_path) == 0:
            continue
        else:
            for file in [f for f in os.listdir(f_path) if f.endswith('.csv')]:
                fi=os.path.join(f_path,file)
                Writing.writeL(fi)
                os.replace(fi,os.path.join(os.getcwd(),"done",file))

if __name__ == "__main__":
    main()