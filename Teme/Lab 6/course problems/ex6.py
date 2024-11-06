# 6 ------------------------------------------------
# Design a library catalog system with a base class LibraryItem and subclasses for different types of items
# like Book, DVD, and Magazine. Include methods to check out, return, and display information about each item.

class LibraryItem:
    def __init__(self, name, price, count, description, isAvailable = True):
        self.description = description
        self.isAvailable = isAvailable
        self.price = price
        self.name = name
        self.count = count
    def return_item(self):
        if(not self.isAvailable):
            self.isAvailable = True
        self.count += 1
        print(self.name, "was returned to the library")
    def check_out(self):
        if (self.count == 0):
            self.isAvailable = False
            print(self.name, "isn't available now")
        elif(self.count > 0):
            self.count -= 1
            print(self.name, "is checked out now")
    def display_info(self):
        print(self.description)

class Book(LibraryItem):
    def __init__(self, name, price, count, description, author, publication_date):
        super().__init__(name, price, count, description)
        self.author = author
        self.publication_date = publication_date
        self.type = "Book"
    def __str__(self):
        return self.type + " | " + self.author + " | " + self.publication_date + " | " + self.name + " | " + str(self.price) + " | " + self.description

class Magazine(LibraryItem):
    def __init__(self, name, price, count, description, pages):
        super().__init__(name, price, count, description)
        self.pages = pages
        self.type = "Magazine"
    def __str__(self):
        return self.type + " | " + self.name + " | " + str(self.price) + " | " + str(self.pages) + " | " + self.description

class DVD(LibraryItem):
    def __init__(self, name, price, count, description, duration):
        super().__init__(name, price, count, description)
        self.duration = duration
        self.type = "DVD"
    def __str__(self):
        return self.type + " | " + self.name + " | " + str(self.price) + " | " + str(self.duration) + " | " + self.description

library_items = [Book("Sleepy Hollow", 42, 5, "\"The Legend of Sleepy Hollow\" is an 1820 short story titled The Sketch Book of Geoffrey Crayon, Gent..", "Washington Irving", "01-01-1820"),
                 Magazine("Forbes", 15, 8, "Forbes is an American business magazine published eight times a year, Forbes features articles on finance, industry, investing, and marketing topics..", 45),
                 DVD("Bad Boys for Life", 30, 3, "Bad Boys for Life is a 2020 American action comedy film that is the sequel to Bad Boys II..", 124)]

library_items[0].return_item()
library_items[1].check_out()
library_items[2].display_info()
print()

for item in library_items:
    print(item)
