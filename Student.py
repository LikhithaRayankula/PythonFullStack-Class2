class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

s1=Student("Smith",20)
print(s1.get_name())
print(s1.get_age())

s2=Student("Smith",20)
print(s2.get_name())
print(s2.get_age())