"""
Bu derste while döngüsünü kullanıyoruz.
"""
"""
Elimizde liste var ise ve bu liste ile işlem yapacaksak for döngüsü
en iyi çözüm yoluyodu. Fakat elimizde liste yoksa ve listesiz bir 
şekilde hareket etmek zorunda isek while döngüsünü kullanmak en iyi 
çözüm yolu olabilir.
"""

x=0
while x<100:
    print(x)
    x += 1

print("Bitti")

"""
Veya 
koşul ifadeleri ile de kurabiliriz.
"""


a = 1
while a<=100:
    if (a % 2 == 0):
        print(a)
a +=1
"""
Veya giriş ekranı yapabiliriz
"""
name = "" #false
while not name:
    name = input("İsminizi giriniz:")
