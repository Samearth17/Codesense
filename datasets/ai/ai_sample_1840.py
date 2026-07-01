class Website:
 def __init__(self, url, author, copyright, language):
 self.url = url
 self.author = author
 self.copyright = copyright
 self.language = language
 
 def get_url(self):
 return self.url
 
 def get_author(self):
 return self.author
 
 def get_copyright(self):
 return self.copyright
 
 def get_language(self):
 return self.language