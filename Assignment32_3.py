import schedule
import time
import os

def DisplayFile(FilePath):
    
    if not os.path.exists(FilePath):
        print("File does not exsist.")
        return
    
    size = os.path.getsize(FilePath)

    if size == 0:
        print("File is empty.")
        return
    
    try:
        fobj = open(FilePath, "r")
        display = fobj.read()
        gobj = open("DisplayFile.txt", "w")
        gobj.write(display)
        print("Displayed successfully.")

    except PermissionError as e:
        print("Permission Denied.")
    except OSError as e:
        print("File cannot be opened.")

def main():
    FileName = input(r"Enter file name/path: ")

    schedule.every(30).seconds.do(DisplayFile, FileName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()