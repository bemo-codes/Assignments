import threading

def Small(name):
    count = 0
    for i in name:
        if i.islower():
            count += 1
    print("Number of lowercase characters: ", count)
    print("Thread ID of small: ", threading.get_ident())
    print("Thread name of small: ", threading.current_thread().name)

def Capital(name):
    count = 0
    for i in name:
        if i.isupper():
            count += 1
    print("Number of UPPERCASE characters: ", count)
    print("Thread ID of Capital: ", threading.get_ident())
    print("Thread name of Capital: ", threading.current_thread().name)

def Digits(name):
    count = 0
    for i in name:
        if i.isdigit():
            count += 1
    print("Number of Digit characters: ", count)
    print("Thread ID of Digits: ", threading.get_ident())
    print("Thread name of Digits: ", threading.current_thread().name)

def main():
    name = input("Enter the ID: ")

    t1 = threading.Thread(target=Small, args=(name,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=Capital, args=(name,))
    t2.start()
    t2.join()

    t3 = threading.Thread(target=Digits, args=(name,))
    t3.start()
    t3.join()

if __name__ == "__main__":
    main()
