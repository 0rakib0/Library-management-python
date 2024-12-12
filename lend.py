import datetime
import json
import file_management
lend_data = []


def lends_book():
    name = input("Enter your name: ")
    phone = input("Enter phone number: ")
    book_title = input("Enter Book title: ")
    Return_month = (input("Enter return month-(1-12): "))
    Return_day = (input("Enter return date-(1-30): "))
    try:
        date = str(datetime.date(2024, int(Return_month), int(Return_day)))
        info = {
            'name':name,
            'phone':phone,
            'book_title':book_title,
            'return_date':date
        }  
        lend_data.append(info)
        with open('lends.json', 'w') as lends_file:
            json.dump(lend_data, lends_file, indent=4)
            
        with open('books.json', 'r') as file:
            Books = json.load(file)
            for i in Books:
                if i['title'] == book_title:
                    i['Quintity'] = int(i['Quintity'])-1                    
                file_management.save_books(Books)
            
    except Exception as e:
        print('Something wrong, ', e)
 
 
        
        
def Return_books():
    book_title = input("Enter Book Name: ")
    borrower_name = input("Enter Book Name: ")
    with open('lends.json', 'r') as file:
            Borrower = json.load(file)
            for i in Borrower:
                if i['name'] == borrower_name:
                    Borrower.pop(Borrower.index(i))
                else:
                    print('No Data Found with this name.')
            with open('lends.json', 'w') as lends_file:
                json.dump(Borrower, lends_file, indent=4)
    with open('books.json', 'r') as file:
            Books = json.load(file)
            for i in Books:
                if i['title'] == book_title:
                    i['Quintity'] = int(i['Quintity'])+1  
                file_management.save_books(Books)

    
    