from lib.book import Book

class BookRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row['id'], row['title'], row['author_name'])
            books.append(item)

        return books
