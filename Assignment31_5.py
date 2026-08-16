import schedule
import os
import time

def DirectoryCount(Dir):
    Fcount = 0
    SubCount = 0
    FileCount = 0
    for FolderName, SubFolder, FileName in os.walk(Dir):
            Fcount += 1
            for subf in SubFolder:
                SubCount += 1
            for fname in FileName:
                FileCount += 1
    fobj = open("DirectoryCountLog.txt", "a")
    fobj.write(f"Directory: {Dir}\n")
    fobj.write(f"Number of files: {FileCount}.\n")
    fobj.write(f"Created at time: {time.ctime()}\n")
    fobj.close()

def main():
    directory = input(r"Enter the directory: ")
    schedule.every(5).minutes.do(DirectoryCount, directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()