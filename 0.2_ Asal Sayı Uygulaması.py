"""
Bu uygulamada ise girilen bir sayının asal olup olmadığını bulan kodları yazmaya çalıştım.
"""

"""
Tanım: asal sayı yalnızca 1 ve kendine bölünebilen sayılara verilen özel addır."""


sayi = int(input("Sayı:"))
sayac = 0
for i in range(1,sayi+1):
    if sayi % i == 0:
        sayac +=1


if sayac == 2:
    print(f"Girdiğiniz {sayi} sayısı asal bir sayıdır")
else:
    print(f"Girdiğiniz {sayi} sayısı asal bir sayı değildir.")
