import time
import schedule
import os
import shutil

def CopyFiles(SourcePath, DistinationPath):

    if not os.path.exists(SourcePath):
        print("Source Directory does not exist.")
        return

    if not os.path.exists(DistinationPath):
        print("Distination Directory did not exist.")
        os.makedirs(DistinationPath, exist_ok=True)

    for filename in os.listdir(SourcePath):
        filepath = os.path.join(SourcePath,filename)
        if os.path.isfile(filepath) and filename.endswith(".txt"):
            DistinationFile = os.path.join(DistinationPath, filename)

            try:
                shutil.copy2(filepath, DistinationFile)                 #used copy2 as it preserves metadata i.e. time of creation, time of modification etc.
                print(filename, "copied successfully.")

                fobj = open("LogFile.txt", "a")
                fobj.write(f"{filename} copied successfully.\n")
                fobj.close()

            except Exception as e:
                print("Unable to copy", filename, ":", e)

def main():
    Source_Path = input(r"Enter the source path: ")
    DestinationPath = input(r"Enter the destination path: ")

    schedule.every(10).minutes.do(CopyFiles, Source_Path, DestinationPath)

    while True: 
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()