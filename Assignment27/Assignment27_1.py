class BookStore:
    NoOfBooks = 0

    def __init__(self, name, author):
        self.name = name
        self.author = author
        #self.NoOfBooks += 1                       this doesnt work as it creates new variable
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.name} by {self.author}. No of books: {self.NoOfBooks}")

obj1 = BookStore("Linux System Programming" , "Robert Love")
obj1.Display()

obj2 = BookStore("C Programming" , "Dennis Ritchie")
obj2.Display()
