class Phone:

    def __init__(self, brand: str = "vivo v17 pro", price : int = 30000) :
        self.brand = brand
        self.price = price
        self.version = 8.76


    def call(self, number):
        print(f"{self.brand} calling {number}... with a lattes version {self.version}")

    def __str__(self) :
        return f"brand = {self.brand}, price = {self.price}, version = {self.version}"

iphone = Phone("iphone 16", 500)
samsung = Phone("samsung galaxy", 800)

iphone.call("8888")
samsung.call("7777")
print(iphone)
print(samsung)

