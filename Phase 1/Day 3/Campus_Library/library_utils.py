from datetime import datetime

def get_timestamp():
    """Reusable helper: returns current time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def find_book(books, title):
    """Reusable helper: finds a book dict by title, or returns None."""
    for book in books:
        if book["title"] == title:
            return book
    return None