import schedule
import time
import datetime

def FileCreation():
    ScanTime = time.ctime()
    FileName = "File"+"_"+ScanTime+".txt"
    FileName = FileName.replace(" ","_")
    FileName = FileName.replace(":","_")
    current_t = datetime.datetime.now()
    fobj = open(FileName, "w")
    fobj.write(f"File Name: {FileName}\n")
    fobj.write(f"Creation date: {current_t.date()}\n")
    fobj.write(f"Time of creation: {current_t.time()}\n")

def main():
    schedule.every(3).seconds.do(FileCreation)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()