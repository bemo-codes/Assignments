import os
import time

def DirectoryScanner(Directory):
    # Directory = os.path.basename(Directory)
    print(f"Directory Scanned: {Directory}")
    Fcount = 0
    SubCount = 0
    FileCount = 0
    for FolderName, SubFolder, FileName in os.walk(Directory):
        Fcount += 1
        for subf in SubFolder:
            SubCount += 1
        for fname in FileName:
            FileCount += 1

    ScanTime = time.ctime()
    print("Total Folders: ", Fcount)
    print("Total subdirectories: ", SubCount)
    print("Total files: ", FileCount)
    print("Scan Time: ", ScanTime)

def main():
    DirPath = input(r"Enter directory path: ")
    DirectoryScanner(DirPath)
    
if __name__ == "__main__":
    main()