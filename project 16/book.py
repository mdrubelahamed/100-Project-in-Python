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
