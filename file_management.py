import json
def save_books(book):
    with open('books.json', 'w') as book_file:
        json.dump(book, book_file, indent = 4)

        