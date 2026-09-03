import schedule
import time
import os

def DeleteEmpty(SourceDir):
    if not os.path.exists(SourceDir):
        print(f"Directory {SourceDir} doesn't exist.")
        return

    for Folder, SubFolder, Files in os.walk(SourceDir):

        for Filename in Files:
            FilePath = os.path.join(Folder, Filename)
            size = os.path.getsize(FilePath)

            if size == 0:
                os.remove(FilePath)
                fobj = open("DeleteLog.txt", "a")
                fobj.write(f"Deleted file: {FilePath}\n")
                print(f"Deleted file: {FilePath}")
                fobj.close()
    
def main():
    path = input("Enter the Source Directory Path: ")
    schedule.every(1).minutes.do(DeleteEmpty, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()