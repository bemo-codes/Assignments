import shutil
import sys
import os
import time
import schedule

def Backup(SourceDir, DestinationDir):
    try:
        if not os.path.exists(SourceDir):
            print("Source file does not exist.")
            return

        filename = os.path.basename(SourceDir)
        current = time.strftime("%d_%m_%Y_%H_%M_%S")

        name, ext = os.path.splitext(filename)

        BackupFileName = name + "_" + current + ext

        DestinationPath = os.path.join(DestinationDir, BackupFileName)

        shutil.copy(SourceDir, DestinationPath)

        logfile = open("backup.txt", "a")
        print(f"Log file gets successfully created with name backup.txt")

        logfile.write("Backup completed successfully at " + 
                      time.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
        logfile.close()

        print("Backup completed successfully")

    except Exception as e:
        print("Error: ", e)

def main():

    schedule.every(1).minutes.do(Backup, sys.argv[1], sys.argv[2])

    print("Backup started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
