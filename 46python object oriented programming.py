# (06:32:32)

# python object oriented programming

class car:
    def __init__(self , model , year , color , for_sale):#contructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self ):#method
        print(f"You drove {self.model}")

amg = car("G63" , 2025 , "Black" , False )
print(amg.model)
print(amg.year)
print(amg.color)
print(amg.for_sale)
amg.drive()#method calling

gls = car("550D" , 2025 , "Snow White" , False)
print(gls.model)
print(gls.year)
print(gls.color)
print(gls.for_sale)