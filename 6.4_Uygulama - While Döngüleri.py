"""
Bu derste while döngüleri ile uygulamaları çözmeye çalıştım :
FurOfTheWeak
"""

number = [1,3,5,7,8,9,12,19,21]

#------------------------------------------
# 1- listedeki elemanları while döngüsü ile ekrana yazdır.
#------------------------------------------
"""
i =0
while i<len(number):
    print(number[i])
    i+=1
"""
#------------------------------------------
# 2-Başlangıç ve bitiş değerlerini kullanıcıdan alıp tüm tek
# sayılarını ekrana yazdırın
#------------------------------------------
"""
bas = int(input("Başlangıç değeri giriniz:"))
son = int(input("Son değeri giriniz:"))
i = bas
while i<son:
    i += 1
    if (i % 2 == 1):
        print(f"{i} değeri tek sayıdır.")


"""
#------------------------------------------
# 3- 1 ile 100 arasındaki sayıları azalan şekilde yazdırınız.
#------------------------------------------
"""
a = 100
while a>0:
    print(a)
    a-=1

"""
#------------------------------------------
# 4-Kullanıcıdan aldığımız 5 sayıyı sıralı bir şekilde yazdıralım.
#------------------------------------------
numbers = []
i = 0
while i<5:
    sayi = int(input("Sayıyı giriniz:"))
    numbers.append(sayi)
    i +=1

numbers.sort()
print(numbers)
#------------------------------------------
# 5-Kullanıcıdan alacağımız sınırsız ürün bilglsi için liste
#------------------------------------------
#ürünü kullanıcıya soracağız
# dictionatr liste yapısı şeklinde olacak
# ürün ekleme işlemi bittiğinde ürünleri ekranda while döngüsü ile listele.

urunler = {
}
urunsayisi = int(input("Girilecek ürün sayısı:"))

while urunsayisi>0:
    isim = input("Ürün adı:")
    kod = int(input("Ürün kodu:"))
    mensei = input("Ürün menşei:")
    sonkullanmayili = int(input("Son kullanma yılı:"))

    urunler[kod] ={
        "İsim":isim,
        "Menşei":mensei,
        "Son Kullanma Yılı": sonkullanmayili
    }
    urunsayisi -=1

for urun in urunler:
    print(f"URUN ADI: {urun["name"]}")
