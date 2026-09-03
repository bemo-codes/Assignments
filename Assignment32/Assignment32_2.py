import schedule 
import datetime
import time
import os

def SizeMonitor(FilePath):
    
    size = os.path.getsize(FilePath)
    now = datetime.datetime.now()

    fobj = open("FileSizeLog.txt", "a")
    fobj.write(f"File path: {FilePath}\n")
    fobj.write(f"Size of file: {size} bytes.\n")
    fobj.write(f"Date and time: {now}.\n")
    fobj.write("-----------------------------------\n")

def main():
    FileName = input(r"Enter file path: ")
    if os.path.exists(FileName):
        schedule.every(30).seconds.do(SizeMonitor, FileName)

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print(f"File with name {FileName} does not exist.")
        return

if __name__ == "__main__":
    main()
