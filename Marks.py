class Marks:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__marks = 0
    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        self.__marks += marks

m=Marks("John", 20)
print(m.get_marks())
m.set_marks(100)
print(m.get_marks())
