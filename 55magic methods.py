# (07:46:16)

# magic methods(dunder method {__init__})

class book:

    def  __init__(self , title , author , pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # __str__ helps to display content instead of memory
    def __str__(self):
        return f"{self.title} by {self.author} of {self.pages}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # __lt__ is used to check weather a pages is less than other
    def __lt__(self , other ):
        return self.pages < other.pages
    
    def __gt__(self , other ):
        return self.pages > other.pages
    
    # __add__ is used to perform addition
    def __add__(self , other):
        return self.pages + other.pages
    
    # To check membership operator
    def __contains__(self,keyword):
            return keyword in self.title
    
    # __getitem__ returns item
    def __getitem__(self , key ):
         if key == "title":
              return self.title
         elif key == "author":
              return self.author
         elif key == "pages":
              return self.pages
         else:
              return f"key {key} was not found"
         
book1 = book("A" , "a" , 220)
book2 = book("B" , "b" , 20)
book3 = book("C" , "c" , 500)

# print(book1)
# print(book2)
# print(book3)
# print(book1 == book2 == book3)
# print(book1 < book2)
# print(book1 > book2)
# print(book1 + book2)
# print("B" in book3)
# print(book3['title'])
# print(book3['author'])
# print(book3['pages'])
# print(book3['audio'])