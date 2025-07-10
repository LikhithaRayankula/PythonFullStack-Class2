class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price
    def get_name(self):
        print(self.name)
    def get_price(self):
        print(self.price)

p1=Product("abc", 100)
p1.get_name()
p1.get_price()

p2=Product("def",200)
p2.get_name()
p2.get_price()

print(p1.name)
print(p1.price)