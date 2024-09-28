"""
Bu derste ise class içindeki methodlar üzerinde duruldu:
"""

class Person:
    def __init__(self,name,surname,age,adress):
        self.name = name
        self.surname = surname
        self.age = age
        self.adress = adress
    def Entry(self):
        print("Welcome to Home !")

p1 = Person("Furkan","Gül",20,"Siirt")
print("------------------------------------------------------")
print(f"Name: {p1.name}\nSurname:{p1.surname}\nAge:{p1.age}\nAdress:{p1.adress}")
print("------------------------------------------------------")
p1.Entry()

class Circile:
    pi = 3.14
    def __init__(self,yaricap):
        self.yaricap = yaricap
    def cevrehesap(self):
        return  self.yaricap * self.pi * 2

    def alanhesap(self):
        return (self.yaricap ** 2) * self.pi

c1 =  Circile(1)

print(f"c1\nalan : {c1.alanhesap()} \nçevre : {c1.cevrehesap()}")

