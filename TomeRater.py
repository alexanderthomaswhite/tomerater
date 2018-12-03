#User class
class User(object):
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.books = {}  

#Returns email value
  def get_email(self):
    return self.email  

#Changes email value
  def change_email(self, address):
    self.email = address
    print(self.name + "'s email has been changed to " + address + ".") 

#String representation
  def __repr__(self):
    return "user: {name}, email: {email}, books read: {num_books)}".format(name = self.name, email = self.email, num_books = len(self.books)) 

#Comparison method
  def __eq__(self, other_user):
    if self.name == other_user.self.name and self.email == other_user.self.email:
      return True
    else:
      return False

#Adds key value pairs to self.books
  def read_book(self, book, rating = None):
    self.books[book] = rating

#Returns average of ratings in self.books
  def get_average_rating(self):
    total = 0
    num_books = 0
    for value in values.self.books():
      total += value
      num_books += 1
    return total / num_books
    

#Book class,
class Book(object):
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.ratings = []

#Return title
  def get_title(self):
    return self.title

#Return isbn
  def get_isbn(self):
    return self.isbn

#Set isbn
  def set_isbn(self, isbn):
   self.isbn = isbn
   print(self.title + "'s isbn number has been reset to " + self.isbn + ".")
 
#Add rating to list
  def add_rating(self, rating):
    if rating >= 0 and rating <= 4:
      self.ratings.append(rating)
    else:
      print("Invalid rating! (must be between 0 and 4)")

#Comparison method
  def __eq__(self, other_book):
    if self.title == other_book.self.title and self.isbn == other_book.self.isbn:
      return True
    else:
      return False

#Returns average of self.ratings
  def get_average_rating(self):
    total = 0
    for rating in self.ratings:
      total += rating
    return total / len(self.ratings)

#Makes Book object hashable
  def __hash__(self):
    return hash((self.title, self.isbn))


#Fiction, subclass of Book
class Fiction(Book):
  def __init__(self, title, isbn, author):
    Book.init(self, title, isbn)
    self.author = author

#Returns author
  def get_author(self):
    return self.author

#String representation
  def __repr__(self):
    return "{title} by {author}".format(title = self.title, author = self.author)


#Non-Fiction, subclass of Book
class Non_Fiction(book):
  def __init__(self, title, subject, level, isbn):
    book.init(self, title, isbn)
    self.subject = subject
    self.level = level

#Returns subject
  def get_subject(self)
    return self.subject

#Returns level
  def get_level(self):
    return self.level

#string representation 
  def __repr__(self):
    return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)



#TomeRater class
class TomeRater(object)
  def __init__(self):
    self.users = {}
    self.books = {}

#Creates book object
  def create_book(self, title, isbn):
    return Book(title, isbn)

  def create_novel(self, title, author, isbn):
    return Fiction(title, author, isbn)

  def create_non_fiction(self, title, subject, level, isbn):
    return Non_Fiction(title, subject, level, isbn)

  def add_book_to_user(self, book, email, rating = None):
    user = self.users.get(email, "No user with email: {email}".format(email = email)
    if user:
      user.read_book(book, rating)
      book.add_rating(rating)
      if book in self.books:
        self.books[book] += 1
      else:
        self.books[book] = 1
  
  def add_user(name, email, user_books = None):
    if email not in self.users:
      self.users[email] = User(name, email)
      if user_books is not None:
        for book in user_books:
          self.add_book_to_user(book, email)
   else:
     print("{name} is already a user.".format(name = name)


  def print_catalog(self):
    for book in self.books.keys():
      print(book)
   
  def print_users(self):
    for users in self.users.values():
      print(user)

  def most_read_book(self):
    


