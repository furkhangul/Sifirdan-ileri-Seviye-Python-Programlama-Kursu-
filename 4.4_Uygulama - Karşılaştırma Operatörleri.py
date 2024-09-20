"""
Bu derste karşılaştırma operatöratörleri üzeirnde çalıştık ve
bu konu hakkındaki soruları çözdüğüm bölüm oldu.
"""
#-----------------------------------
# 1- Girilen iki sayıdan hangisi daha büyüktür.
#-----------------------------------
"""
a = int(input("1.sayı:"))
b = int(input("2.sayı:"))
buyukmu = (a < b)
print("{0} sayısı {1} sayısından küçüktür : {2}".format(a,b,buyukmu))
"""
#-----------------------------------
# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# eğer ortalama 50 ve üzerinde ise geçti değilse kaldı.
#-----------------------------------

vize1 = int(input("1.vize:"))
vize2 = int(input("2.vize:"))
final = int(input("Final:"))
ortalama = ((vize1+vize2)*0.6) + (final * 0.4)

kaldimi = (50 < ortalama)
print("Geçti:{0}".format(kaldimi))

#-----------------------------------
# 3-Girilen bir sayının tek mi çift mi olduğunu tespit etme
#-----------------------------------

number1 = int(input("Sayı giriniz:"))
ciftmi = (number1%2==0)
print(f"Girilen sayı çift:{ciftmi}")

#-----------------------------------
# 4-Girilen sayının negatif mi pozitif mi olduğunu belirleyiniz.
#-----------------------------------
deger = int(input("Sayı giriniz:"))
negatifmi = (deger <0)
print(f"Girdiğiniz değer negatif mi : {negatifmi}")

#-----------------------------------
# 4-Parola ve e posta doğruluğunu kontrol ediniz.
#-----------------------------------
eposta = "furkangul@gmail.com"
password = 123

enterusername = input("Enter username:")
enterpassword = int(input("Enter password:"))

dogrumu = (eposta == enterusername and password == enterpassword)
print("Girdiğiniz kullanıcı: {dogrumu}")
