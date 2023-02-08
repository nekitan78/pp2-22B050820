class Person:
    def __init__(self, age, sex, name):
        self.age = age
        self.sex = sex
        self.name = name

    def __str__(self):
        return f"{self.name} {self.age} {self.sex}"
    
p1 = Person(43, "man"   , "Nikita")
print(p1)