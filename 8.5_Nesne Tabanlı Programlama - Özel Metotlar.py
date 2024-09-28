"""
Bu derste objeler üzerinde kullanılan özel methodlara baktık.
"""

mylist = [1,2,3]
mystring = "Hello"

print(len(mylist))
print(len(mystring))
"""
Görüldüğü gibi string ifadede harf sayısını hesaplarken liste mehodunda
ise eleman sayısını hesaplar buradan çıkracağımız sonuc kendi ürettiğimiz
bir sınıf tanımlarken de bu şekilde özellikler ekleyebiliriz.
"""

class Movie():
    pass

m = Movie()
print(type(m))
#print(len(m)) yazamayız çünkü sınıfta len ile alakalı bir bilgi yok
"""
burada movie classının içinden çağırılan bir objenin tipine bakıldığında 
movie sınıfının tiplemesini aldığını görüyoruz
"""

class Movie1:
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duraction = duration

m1 = Movie1("Esaret", "Tom", "Leader")
