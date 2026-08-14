import time
import datetime
import schedule

def Display():
    print("Current Date and Time is: ", datetime.datetime.now())

def main():
    schedule.every(3).seconds.do(Display)

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()