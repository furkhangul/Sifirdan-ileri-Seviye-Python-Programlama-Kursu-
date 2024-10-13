
"""
Dosyaa açmak ve oluşturmak için open() fonkisyonu kullanılır.
Kullanımı : open(dosya_Adı, dosya_erişme_modu)
dosya_erişme_modu => dosya hangi amaçla açtığımızı belirtiriz


w : write - yazma modu. dosya konumunda oluşturulur.
a : append - ekleme. dosta konumunda yoksa oluşturulur.
x : create - oluşturmak. dosya zaten varsa hata verir.
r : read - okuma. varsayılan dosya konumda yoksa hata verir.
"""

result = open("newfile.txt","w")
print(result)


result = open("C:/Users/Furkan/Desktop/new.txt","w")
print(result)


file = open("newfilie.txt","w",encoding="utf-8")
file.write("Furkan Gül")
file.close()
