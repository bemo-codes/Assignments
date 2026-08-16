import schedule
import time

def Display(Message):
    print(Message)

def main():
    message = input("Enter the message: ")
    interval = int(input("Enter the time interval(in seconds): "))
    schedule.every(interval).seconds.do(Display, message)

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()

