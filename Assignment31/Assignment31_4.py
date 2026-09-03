import schedule
import os
import time 

def LogFile(DirPath):
    timestamp = time.ctime()

    LogFileName = "LogFile" + "_"+ str(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    Ret = False 

    Ret = os.path.exists(DirPath)
    if Ret == False:
        print("Directory path doesn't exist.")
        return

    Ret = os.path.isdir(DirPath)
    if Ret == False:
        print("It isn't a directory.")
        return

    print("Log file gets created by name: ", LogFileName)

    fobj = open(LogFileName, "w")

    fobj.write("Log file gets created successfully. \n")
    fobj.write(f"Creation Time: {timestamp} \n")

def main():
    path = input(r"Enter the Directory path: ")
    schedule.every(5).seconds.do(LogFile, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    
