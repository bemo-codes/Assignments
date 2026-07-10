import threading

def Diplay():
    
    for i in range(1,51):
        print(i, end = " ")
    print(" ")

def RevDisplay():
    for i in range(50, 0, -1):
        print(i, end = " ")

def main():
    print("Numbers 1 to 50: ")
    t1 = threading.Thread(target=Diplay, args= ())
    t1.start()
    t1.join()

    print("Numbers from 50 to 1: ")
    t2 = threading.Thread(target=RevDisplay, args=())
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()