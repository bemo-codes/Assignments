from datetime import datetime
import time
import schedule

def Display():
    current = datetime.now()
    print(f"Task excuted at: {current.date()} {current.time()}")

def main():
    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()