from lib.book import Book

"""
When an instance of the Book class is created
id, title and author name properties are assigned
"""

def test_book_constructs_properties():
    book = Book(1, "Jack Reacher", "Lee Child")
    assert book.id == 1
    assert book.title == "Jack Reacher"
    assert book.author_name == "Lee Child"

"""
We can format books into strings
"""

def test_book_formats_nicely():
    book = Book(1, "Jack Reacher", "Lee Child")
    assert str(book) == "1 - Jack Reacher - Lee Child"


"""
When we have two identical books
then they will be classed as equal
"""

def test_books_are_equal():
    book1 = Book(1, "Jack Reacher", "Lee Child")
    book2 = Book(1, "Jack Reacher", "Lee Child")
    assert book1 == book2