

def add_book(books):
    title = input("Enter Book Title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN number: ")
    publish_year = input("Enter publish year: ")
    price = int(input("Enter price."))
    Quintity = int(input("Enter Book Quintity: "))
    
    book = {
        'title':title,
        'authour': author,
        'isbn': isbn,
        'publish_year': publish_year,
        'price': price,
        'Quintity': Quintity
    }
    
    try:
        books.append(book)
        
    except Exception as e:
        print("Book not added, Something wrong.", e)
    
    