# smart ass you could've just used len function if it was a string. you didnt even need loop.
def CountDigit(Number): 
    count = 0
    for i in Number:
        count = count+1
    return count
    

def main():
    print("Enter the number: ")
    No = input()                    #here we kept it string as we could count number of characters

    Ret = CountDigit(No)
    print("The number of digits in number: ", Ret)


if __name__ == "__main__":
    main()