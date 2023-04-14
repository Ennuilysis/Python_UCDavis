#store all classes here for future use
from prog5 import count_in_other,buy_items

class Person1:
    def __init__(self,a):
        print("Using class Person")
        self.a=a
    def __str__(self):###what string value does the value with this class have##
        print("Democracy Prime")
        b=str(3)
        return  "frickin commie"+b

class Person:
    def __init__(self, first_name, last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person("Scott", "Thompson", 58)
print(p1)
print(p1.first_name, p1.last_name, p1.age)

p2= Person1("a")
print(p2.a)