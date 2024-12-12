import add_books
import view_books
import file_management
import lend
books = [
    # {'title': 'Miracle', 'authour': 'Rakib', 'isbn': '1272', 'publish_year': '2022', 'price': 300, 'Quintity': 10},
    # {'title': 'Bangla', 'authour': 'Shathi', 'isbn': '2987', 'publish_year': '2000', 'price': 200, 'Quintity': 5},
    ]

while True:    
    print("\n -----Book Management System--------")
    print('1. Add New Book.')
    print('2. View All Book')
    print('3. Lends a book: ')
    print('4. Return book: ')
    print('5. Logout From System.')
    
    options = input("Please Choose an option-(1-3): ")
    
    if options == '1':
        all_books = add_books.add_book(books)
        file_management.save_books(books)
        print("Book Successfully Added.")
        
    elif options == '2':
        view_books.view_books()
        
    elif options == '3':
        lend.lends_book()
        
    elif options == '4':
        lend.Return_books()
    elif options == '5':
        print("Thank you for using Library")
        break
    else:
        print("Invalid input, please choose the valid option.")