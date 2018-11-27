class User(object):
#user constructor, will store name, email, and dictionary of books
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.book = {}  

#return users email
  def get_email(self):
    return self.email  

#change users email
  def change_email(self, address):
    self.email = address
    print(self.name + "'s email has been changed to " + address + ".") 

  def __repr__(self):
    return user: self.name, email: self.email, books read: len(self.book)  

  def __eq__(self, other_user):
    if self.name == other_user.self.name and self.email == other_user.self.email:
      return True
    else:
      return False

#Book class, will store info about the books themselves
class Book(object):
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.ratings = {}

  def get_title(self):
    return self.title

  def get_isbn(self):
    return self.isbn

  def set_isbn(self, isbn):
   self.isbn = isbn
   print(self.title + "'s isbn number has been reset to " + self.isbn + ".")
 
  def add_rating(self, rating):
    if rating >= 0 and rating <= 4:
      self.ratings.append(rating)
    else:
      print("Invalid rating! (must be between 0 and 4)")

  def __eq__(self, other_book):
    if self.title == other_book.self.title and self.isbn == other_book.self.isbn:
      return True
    else:
      return False
