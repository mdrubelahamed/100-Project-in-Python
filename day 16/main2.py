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