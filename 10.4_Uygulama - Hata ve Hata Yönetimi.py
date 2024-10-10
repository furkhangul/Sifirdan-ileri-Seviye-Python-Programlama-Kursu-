from tabnanny import check

liste= ["1","2","5a","10b","abc","10","50"]

"""
Liste elemanları içindeki sayısal değerleri bulunuz.
"""
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

"""
Kullanıcıdan "q" değerini girmedikçe aldığınız her input sayısının 
olduğundan emin olunuz aksi halde hata mesajı alınız:
"""
sayi= input("Sayi: ")
while True:

    if sayi == "q":
        break

    try:
        result =float(sayi)
    except ValueError:
        print("Geçersiz Sayı")
        continue

"""
Girilen parola içerisindeki tükrçe hatasını bulunuz.
"""
def chechPassword(parola):
    turkce_karakterler = "içğüşıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Türkçe Karakter Kullanıldı")
        else:
            pass

    print("Geçerli parola ")
parola = input("Parola:")

try:
    chechPassword(parola)
except TypeError as err:
    print(err)

"""
Faktöriyel fonksiyonun oluşturup fonksiyona gelen değer için hata mesajaları
verin
"""

def faktoriyel(x):
    x = int(x)
    if x > 0:
        raise ValueError("Negatif Değer")
    result = 1
    for i in range(1,x+1):
        result *=i
        return result

for x in [5,10,2,-3,"10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue

