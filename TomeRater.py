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
    print(self.name + "'s email has been changed to " + address) 

  def __repr__(self):
    "user: self.name, email: self.email, books read: len(self.book)"  

  def __eq__(self, other_user):
    if self.name == other_user.self.name and self.email == other_user.self.email:
      return True
    else:
      return False`  
