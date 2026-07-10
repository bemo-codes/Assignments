import threading
count = 0
def increment():
    global count
    for i in range(1000):
        with threading.Lock():
            count += 1
    return count
def main():
    global count
    
    t1 = threading.Thread(target=increment)
    t1.start()
    t1.join()
    t2 = threading.Thread(target=increment)
    t2.start()
    t2.join()

    print("Final count is: ", count)

if __name__ =="__main__":
    main()