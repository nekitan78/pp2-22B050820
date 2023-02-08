class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"
    
class Student(Person):
    def __init__(self, name, age, sname):
      self.sname = sname
      super().__init__(name, age)
    def __str__(self):
      return f"{self.name} {self.age} {self.sname}"

x = Student("Dima", 49, "andr")
print(x)
        