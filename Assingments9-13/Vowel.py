def Vowel(ch):
    list = ['a', 'e', 'i', 'o', 'u']
    for i in list:
        if ch == i:
            print(f"{ch} is Vowel.") 
            break
    else:
        print(f"{ch} is consonent.")          
        
def main():
    Character = input("Enter a character: ")
    Vowel(Character)
    

if __name__ == "__main__":
    main()