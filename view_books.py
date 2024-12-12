import json


def view_books():
    try:
        with open('books.json', 'r') as file:
            pythonObj = json.load(file)
            
        if pythonObj != []:
            for book in pythonObj:
                print(f'Book Name: {book['title']} | Author: {book['authour']} | ISBN: {book['isbn']} | Publish Year: {book['publish_year']} | Price: {book['price']} | Quentity: {book['Quintity']}')
    except:
        print("Something wrong...")
    else:
        print("No Book Available..")