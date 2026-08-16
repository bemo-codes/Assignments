import schedule
import sys

def DisplayMessage(Message):
    print(Message)

def main():
    schedule.every(int(sys.argv[2])).seconds.do(DisplayMessage, sys.argv[1])

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()
