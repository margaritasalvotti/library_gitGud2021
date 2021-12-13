list_of_books = {'Romeo and Juliet': 'William Shakespeare',
'1984': 'George Orwell',
'2001: a Space Odissey': 'Arthur C. Clarke',
'Pride and Prejudice' : 'Jane Austen',
'The Great Gatsby' : 'F.Scott Fitzgerald',
'The Lord of the Rings' : 'J. R. R. Tolkien',
'The Old Man and the Sea' : 'Ernest Hemingway',
'The Picture of Dorian Gray' : 'Oscar Wilde',
'A Christmas Carol' : 'Charles Dickens',
                 }


def check_book(title):
    if title in list_of_books:
        print("The book {} is written by {}".format(title, list_of_books[title]))
    else:
        print("Sorry, we do not have {}".format(title))

def check_author(author_name):

    found = False
    for title, author in list_of_books.items():
        if author == author_name:
            print("{} wrote {}".format(author_name, title))
            found = True

    if not found:
        print("Sorry, {} is not present.".format(author_name))


def book_pages(number_of_p):

    """
    Function to find the book with less pages that number_of_p parameter
    """

    books_length = {'Romeo and Juliet': 322,  # New dictionary
                    '1984': 340,
                    '2001: a Space Odyssey': 250,
                    'Pride and Prejudice': 450,
                    'The Great Gatsby': 200,
                    'The Lord of the Rings': 1100,
                    'The Old Man and the Sea': 100,
                    'The Picture of Dorian Gray': 300,
                    'A Christmas Carol': 125}

    max_pages = 0                               # Initialise variables
    book = None
    for k, v in books_length.items():            # Iteration
        # If found new book with more pages than the
        # previous best assign to update variable book
        if v < number_of_p and max_pages < v:
            max_pages = v
            book = k
    # Return
    a = f'The book with most pages less than {number_of_p}'
    b = f'is {book} with {max_pages}'
    return a+b
    
def check_by_initial_title(first_letter):
	"""
	check_by_initial_title() returns all books that starting with the letter given in input
	"""
    flag = 0 							# a flag used to verify if there is no books with that letter
    if len(first_letter) == 1: 			# if the user insert more than one letter, the script will return an print error
        for title in list_of_books.keys(): # iterator
            if title[0] == first_letter or title[0] == first_letter.upper(): 	# if a book start with the letter given in input
                print(title)													# it will be printed
                flag = 1														# deactivate the flag
        if flag == 0:															
            print("no books were found starting with the letter \"{}\"".format(first_letter))
    else:
        print("Error! enter only one letter")
