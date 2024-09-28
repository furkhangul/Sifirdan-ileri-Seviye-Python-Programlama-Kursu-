"""
Geçen derste öğrendiğimiz class ve object yani instance kavramları üzerinde
duracak olursak:
"""
from tkinter.font import names

"""
Sınıf tanımlamak için class başlığı ile başlatmamız gerekmektedir.
"""
class Person:
    pass # bu key word bizim boş classların boş iken hata vermemesini sağlar
    #attributes
    #methods

#objecet ( instance )
p1 = Person()
p2 = Person()
"""
Bu şekilde person class'ına  iki yeni nesne ekledik
"""
print(p1)
"""
yazdığım zaman person sınıfından alındığına dair bilgi karşımıza çıkar
"""
print(type(p1))
"""
burada da aynı şekilde sınıf olarak Person sınfı gösterilir
"""
#############################################################
"""
class içine attributes ve method ekleyebilidiğimizi söylemiştim.
attrebutes = bağlamak
örnek yapacak olursak.
"""
"""
bu derste yalnızca attributes üzerinde çalışacağımız için yapılarına bakacak
olursak """

class User:
    #class attributes
    #constructer ( yapıcı method )
    #methods

    def __init__(self,name,year):
        self.name = name
        self.age = year
        print("İnit methodu çalışır.")



u1 = User("Furkan",20)
u2 = User("Berkan",16)
print("-----------------------------------")
print(f"Name: {u1.name}\nAge: {u1.age}")
print("-----------------------------------")
print(f"Name: {u2.name}\nAge: {u2.age}")
"""
Bu derste attributes üzerinde duruldu attributesler için yapıcı methodlara
ihtiyacımız olduğunu belirttik ve bunun için __init__ methodunu çağırdığımız
zaman gelen self bloğunu kullandık. Yukarıdaki örneğin devamı bi sonraki derste
hoca tarafından anlatıldı.
"""
