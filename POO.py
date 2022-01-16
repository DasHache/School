class Book:
    def __init__(self, title, pages, date, color):
        self.t = title
        self.p = pages
        self.d = date
        self.c = color
        
    def info(self):
        return f"The book '{self.t}' containing {self.p} pages, is {self.c} and was released in {self.d}"
    
    def bbb(self):
        return f"{self.info()} et je suis un gato"
tbh = Book("To be honest", 233, 2018, "black")
print(tbh.info())
print(tbh.bbb())