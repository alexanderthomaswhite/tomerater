class User(object):
  def __init__(self, name, email):
    self.name = name
    self.email = email
    # Dictionary that will hold user's ratings & a count of books read
    self.books = {}  

  def get_email(self):
    return self.email  

  def change_email(self, address):
    self.email = address
    print("{name}'s email has been changed to {email}".format(name = self.name, email = self.email)) 

  def __repr__(self):
    return "user: {name}, email: {email}, books read: {num_books)}".format(name = self.name, email = self.email, num_books = len(self.books)) 

  def __eq__(self, other_user):
    return self.name == other_user.name and self.email == other_user.email

  # Adds key value pairs to self.books
  def read_book(self, book, rating = None):
    self.books[book] = rating

  # Returns average of ratings in self.books
  def get_average_rating(self):
    rtngTotal = 0
    bookCount = 0
    for rating in self.books.values():
      rtngTotal += rating
      bookCount += 1
    return rtngTotal / bookCount


class Book(object):
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.ratings = []

  def get_title(self):
    return self.title

  def get_isbn(self):
    return self.isbn

  def set_isbn(self, isbn):
   self.isbn = isbn
   print("{title}'s ISBN has been updated to {isbn}".format(title = self.title, isbn = self.isbn))

  def add_rating(self, rating):
    if rating >= 0 and rating <= 4:
      self.ratings.append(rating)
    else:
      print("Invalid rating! (must be between 0 and 4)")

  def __eq__(self, other_book):
    return self.title == other_book.title and self.isbn == other_book.isbn

  def get_average_rating(self):
    total = 0
    for rating in self.ratings:
      total += rating
    return total / len(self.ratings)

# Returns hash value for book object
  def __hash__(self):
    return hash((self.title, self.isbn))


# Fiction, Book subclass
class Fiction(Book):
  def __init__(self, title, isbn, author):
    super().__init__(title, isbn)
    self.author = author

  def get_author(self):
    return self.author

  def __repr__(self):
    return "{title} by {author}".format(title = self.title, author = self.author)


# Non-Fiction, Book subclass
class Non_Fiction(book):
  def __init__(self, title, subject, level, isbn):
    super().__init__(title, isbn)
    self.subject = subject
    self.level = level

  def get_subject(self):
    return self.subject

  def get_level(self):
    return self.level

  def __repr__(self):
    return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)



#TomeRater class
class TomeRater(object):
  def __init__(self):
    # Dictionary, will store store user emails as keys to User objects
    self.users = {}
    # Dictionary, will store Book objects as keys to the number of users that have read them
    self.books = {}

  def create_book(self, title, isbn):
    return Book(title, isbn)

  def create_novel(self, title, author, isbn):
    return Fiction(title, author, isbn)

  def create_non_fiction(self, title, subject, level, isbn):
    return Non_Fiction(title, subject, level, isbn)

#  def add_book_to_user(self, book, email, rating = None):
#    user = self.users.get(email, "No user with email: {email}".format(email = email)
#
#     user.read_book(book, rating)
#      book.add_rating(rating)
#      if book in self.books:
#        self.books[book] += 1
#      else:
#        self.books[book] = 1

  def add_user(name, email, user_books = None):
    if email not in self.users:
      self.users[email] = User(name, email)
      if user_books is not None:
        for book in user_books:
          self.add_book_to_user(book, email)
    else:
      print("{name} is already a user.".format(name = name)

  def add_book_to_user(self, book, email, rating = None):
    user = self.users.get(email, "No user with email: {email}".format(email = email)
    if user:
      user.read_book(book, rating)
      book.add_rating(rating)
      if book in self.books:
        self.books[book] += 1
      else:
        self.books[book] = 1 


  def print_catalog(self):
    for book in self.books.keys():
      print(book)
   
  def print_users(self):
    for users in self.users.values():
      print(user)

  def most_read_book(self):
    readCount = 0
    mostRead = None
    for book in self.books:
      nmrofReads = self.books[book]
      if nmrOfReads > readCount:
        readCount = nmrOfReads
        mostRead = book
    return mostRead

  def most_positive_user(self):
    highestRating = 0
    positiveUser = None
    for user in self.users.values():
      avgRating = user.get_average_rating()
      if avgRating > highestRating:
        highestRating = avgRating
        positiveUser = user
    return positiveUser
