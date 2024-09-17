#Bir kullanıcının maaş bilgisini hesaplamak için uygulama yapacağız.
#Örneğin 5000TL maaş alan bi kullanıcının maaşı ile orantılı olarak ödediği vergiler ile brüt maaşını hesaplama 
#Vergi Oranı 0.27 olursa:
print(5000-(5000 * (2.7/100)))
#Veya

maasAli = 5000
maasAhmet = 4000
vergiOrani = 0.27

print(maasAli - (maasAli * vergiOrani))
print(maasAhmet - (maasAhmet * vergiOrani))

#Değişken tanıma kuralları 
#1)Değişken sayı ile başlayamaz.
#2)Büyük küçük harf duyarlılığı vardır.
#3)Türkçe karakter kullanılamaz.

x = 1 #int
y = 2.5 #float
name = "Furkan" #string 
isStudent = True  #bool

a = '10'
b = '20'
print (a+b) # => 1020

firstname = "Furkan"
lastname  = "Gül"
print(firstname+lastname) # =>FurkanGül
