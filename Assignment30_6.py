from datetime import datetime
import schedule

def Lunch():
    print("Lunch Time!")

def WrapUp():
    print("Wrap Up Work.")

def main():
    schedule.every().day.at("13:00").do(Lunch)
    schedule.every().day.at("18:00").do(WrapUp)

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()