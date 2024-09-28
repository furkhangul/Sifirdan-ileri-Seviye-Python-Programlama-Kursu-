"""
Bu derste kalıtım yani inheritance kavramının üzerinde duruldu.
"""
"""
Inheritance: miras alma
kalıtım ile açılan bir sınıfın altında başka bir sınıf açıp ana sınıftaki
özelliklerin alt sınıfa aktarılmasını sağladığı bir sistem oluşturmaktır.
"""

# Person => name,lastname,age,eat(),run(),drink()
# Student => Student(Person) , Teacher(Person)

#Animal => Dog(Animal),Cat(Animal)

class Person:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        print("Person created !")
    def who_am_i(self):
        print("İ am person")


class Student(Person):
    def __init__(self,name,lastname,number):
        Person.__init__(self,name,lastname)
        self.number = number
        print("Student Created !")

s1 = Student("Furkan","Gül",20)
print(f"Name: {s1.name}\nLastname:{s1.lastname}\nNumber: {s1.number}")

s1.who_am_i()
