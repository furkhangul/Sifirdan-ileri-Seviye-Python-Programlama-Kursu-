"""
Bu derste verilen örneklerin çözümünü göstereceğim :)
FurOfTheWeak
"""

liste = [1,3,5,7,9,12,15,19,21,35,38,40,42,50,54,56,57,61,68,70]
#---------------------------------------------------------
# 1- Listedeki hangi sayılar 3'ün katıdır ?
#---------------------------------------------------------
for x in liste:
    if(x % 3 == 0 ):
        print(f"{x} sayısı 3'ün katıdır.")



#---------------------------------------------------------
# 2-Listedeki sayıların toplamı kaçtır ?
#---------------------------------------------------------
toplam = 0
for n in liste:
    toplam += n

print(f"Sayıların toplamı: {toplam}")

#---------------------------------------------------------
# 3-Listedeki tek sayıların karesini alınız.
#---------------------------------------------------------
for k in liste:
    if (k%2!=0) :
        print(k**2)

#---------------------------------------------------------
# 4-Şehirlerin hangisi en fazla 5 karakterlidir ?
#---------------------------------------------------------

sehirler = ["Kocaeli","İstanbul","Ankara","İzmir","Diyarbakır","Siirt"]

for city in sehirler:
    deger = len(city)
    if deger<=5:
        print(city)

#---------------------------------------------------------
# 5-Urunlerin fiyatlarının toplamı nedir ?
#---------------------------------------------------------
Urunler = [
    {"Name":"Samsung S6", "Price":3000},
    {"Name":"Samsung S7", "Price":4000},
    {"Name":"Samsung S8", "Price":5000},
    {"Name":"Samsung S9", "Price":6000},
    {"Name":"Samsung SX", "Price":7000}
]
total = 0
for urun in Urunler:
    total += urun["Price"]


print(f"Ürünlerin toplam bedeli: {total}")
