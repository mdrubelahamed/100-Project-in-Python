# Day 16 Project 16

---
---
### What?
- 

---
---





- How to integreted python packages into project?
Ans: I just install a package in my "100 project in python" folder, 
package name - PrettyTable
version - 0.7.2
```pip install PrettyTable==0.7.2```   

NOTE: I am install this version explicitly 'cause from my learning resource,she install the same version so it would better that i use the same version when i am learning, which makes less confusion


- Use PrettyTable
```
from prettytable import PrettyTable

x = PrettyTable()
x.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

print(x)
```

```
# CREATE A TABLE ON YOUR OWN
from prettytable import PrettyTable

# create an object called 'table' from 'PrettyTable' class 
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

# print(table.align)
table.align = "r"


print(table)

```



Q. BUILD A REAL LIFE TABLE FROM THE INTERNET?   
-- pass


--------------------------
```
from book import Book

update_book = True
book_store = []
i = 1
while update_book:
    print(f"Enter details for Book {i}:")
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    year = input("Year: ")
    book_store.append(Book(title, author, genre, year))

    i += 1
    if input(f" Do you want to enter another book? (y/n): ") == 'n':
        update_book = False

print("\nBook Information:")
for book in book_store:
    book.display_info()
    print()
```

- The `book.py` file
```
class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Year: {self.year}")

# Creating instances of the Book class
# book1 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960)
# book2 = Book("1984", "George Orwell", "Science Fiction", 1949)

# # Displaying book information
# book1.display_info()
# book2.display_info()

```

-----------------------------