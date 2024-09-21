"""
Bu derste mantıksal operatörlerin kullanımı ile problemleri çözmeye
çalışacağım.
"""

#------------------------------------------------------
# 1-Girilen bir sayının 0-100 arasında olup olmadığını bulunuz.
#------------------------------------------------------

number = int(input("SAYI:"))
arasindaMi = (number>0) and (number<100)
print(f"Sayı 0 ile 100 arasında mı: {arasindaMi}")

#------------------------------------------------------
# 2-Girilem bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
#------------------------------------------------------

pozitifcift = (number>0) and (number%2 == 0)
print(f"Girdiğiniz sayı pozitif ve çift mi: {pozitifcift}")

#------------------------------------------------------
# 3-email ve parola bilgileri ile giriş kontrolü yapınız
#------------------------------------------------------

email = input("Eposta:")
passwod = input("Şifre:")
dataemail = "gl56frkn@gmail.com"
datapassword = "furkanfurkan"

iftrue = (email == dataemail) and (passwod == datapassword)
print(f"Girdiğiniz bilgiler doğru mu: {iftrue}")

#------------------------------------------------------
# 4-Girilen 3 sayıyı büyüklüğü ile karşılaştırınız.
#------------------------------------------------------
sayi1 = int(input("1.sayiyi giriniz:"))
sayi2 = int(input("2.sayiyi giriniz:"))
sayi3 = int(input("3.sayiyi giriniz:"))


result = (sayi1>sayi2) and (sayi1 > sayi3)
print(f"{sayi1} en büyük sayıdır: {result}")

result1 = (sayi2>sayi1) and (sayi2>sayi3)
print(f"{sayi2} en büyük sayıdır: {result1}")

result2 = (sayi3>sayi1) and (sayi3>sayi2)
print(f"{sayi3} en büyük sayıdır: {result2}")

#------------------------------------------------------
# 5- Kullanıcıdan 2 vize(%60) ve 1(%40) final notu alıp ortalama hesapla.
#   Eğer ortalama 50 ve üstü ise geçti değilse kaldı yazılsın.
#   A) Ortalama 50 ise bile final notu 50 olması gerekmektedir.
#   B) Finalden 70 alındığında ortalama önemli olunmasın.
#------------------------------------------------------

vize1 = int(input("1.vize:"))
vize2 = int(input("2.vize:"))
final = int(input("Final:"))

ortalama = ((vize1+vize2)*0.6)+(final*0.4)

sonuc = ((ortalama>=50) and (final > 50) ) or (final >= 70)
print(f"Geçti : {sonuc}")








