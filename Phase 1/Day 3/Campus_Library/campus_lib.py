from library_utils import get_timestamp, find_book

books = []

def add_book(title, author):
    books.append({"title": title, "author": author, "available": True})

def list_books():
    for book in books:
        status = "Available" if book["available"] else "Borrowed"
        print(f"{book['title']} by {book['author']} — {status}")

def borrow_book(title):
    book = find_book(books, title)
    if book is None:
        print(f"'{title}' not found in catalog.")
        return
    if not book["available"]:
        print(f"'{title}' is already borrowed.")
        return
    book["available"] = False
    log_action(title, "BORROWED")

def return_book(title):
    book = find_book(books, title)
    if book is None:
        print(f"'{title}' not found in catalog.")
        return
    if book["available"]:
        print(f"'{title}' was not borrowed.")
        return
    book["available"] = True
    log_action(title, "RETURNED")

def log_action(title, action):
    with open("borrow_log.txt", "a") as f:
        f.write(f"{get_timestamp()} | {action} | {title}\n")

def view_log():
    print("\n--- Borrow Log ---")
    try:
        with open("borrow_log.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            print("No activity logged yet.")
        else:
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No activity logged yet.")

def summarize_library(**stats):
    print("\n===== END OF DAY REPORT =====")
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")
    print("==============================")

add_book("Clean Code", "Robert C. Martin")
add_book("The Pragmatic Programmer", "Andrew Hunt")

list_books()
borrow_book("Clean Code")
list_books()
return_book("Clean Code")

view_log()

summarize_library(
    total_books=len(books),
    books_available=sum(1 for b in books if b["available"]),
    books_borrowed=sum(1 for b in books if not b["available"])
)