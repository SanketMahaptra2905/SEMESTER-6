print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017")

class Chapter:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

class Book:
    def __init__(self, title):
        self.title = title
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def total_pages(self):
        return sum(chapter.page_count for chapter in self.chapters)

book = Book("Python Programming")

chapter1 = Chapter("Introduction to Python", 30)
chapter2 = Chapter("Data Structures", 40)
chapter3 = Chapter("Object-Oriented Programming", 50)

book.add_chapter(chapter1)
book.add_chapter(chapter2)
book.add_chapter(chapter3)

print(f"Total page count of the book '{book.title}': {book.total_pages()} pages")
