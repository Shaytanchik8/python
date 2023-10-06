class Library:
    def __init__(self):
        self.repository = {}

    def add_book(self,title,author):
        self.repository[title]={"title": title,"author":author}
    def find_book_by_author(self,author):
        by_author=[book for book in self.repository.values() if book["author"]==author]
        if len(by_author)>0:
            return by_author
        else:
            return f"Book written by {author} wasn't found"
    def find_book_by_title(self,title):
        if title in self.repository:
            return self.repository[title]
        else:
            return f"Book named {title} wasn't found"
    def remove_book(self,title):
        if title in self.repository:
            del self.repository[title]
        else:
            print(f"Book named {title} wasn't found")





library = Library()

library.add_book("Когда Ницше плакал", "Ирвина Ялома")
library.add_book("Ангелы и демоны", "Дэн Браун")
library.add_book("Война и мир", "Лев Толстой")

print(library.find_book_by_author("Дэн Браун"))
print(library.find_book_by_title("Ангелы и демоны"))
print(library.find_book_by_title("Ангелы"))
library.remove_book("Ангелы и демоны")
print(library.find_book_by_title("Ангелы и демоны"))