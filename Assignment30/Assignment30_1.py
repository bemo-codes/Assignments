import schedule
import time

def Display():
    print("Jay Ganesh...")

def main():
    print("Automation Script")

    schedule.every(5).seconds.do(Display)

    while True:
        schedule.run_pending()
        

if __name__ == "__main__":
    main()