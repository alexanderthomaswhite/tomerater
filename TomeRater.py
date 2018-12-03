#User class
class User(object):
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.book = {}  

#Return email value
  def get_email(self):
    return self.email  

#Change email value
  def change_email(self, address):
    self.email = address
    print(self.name + "'s email has been changed to " + address + ".") 

#String representation
  def __repr__(self):
    return "user: {name}, email: {email}, books read: {num_books)}".format(name = self.name, email = self.email, num_books = len(self.book)) 

#Comparison method
  def __eq__(self, other_user):
    if self.name == other_user.self.name and self.email == other_user.self.email:
      return True
    else:
      return False


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


#Fiction, subclass of Book
class Fiction(Book):
  def __init__(self, title, isbn, author):
    Book.init(self, title, isbn)
    self.author = author

#Return author
  def get_author(self):
    return self.author

#Set pleasing string representation
  def __repr__(self):
    return "{title} by {author}".format(title = self.title, author = self.author)


#Non-Fiction, subclass of Book
class Non_Fiction(book):
  def __init__(self, title, subject, level, isbn):
    book.init(self, title, isbn)
    self.subject = subject
    self.level = level

#Return subject
  def get_subject(self)
    return self.subject

#Return level
  def get_level(self):
    return self.level

#string representation 
  def __repr__(self):
    return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)




