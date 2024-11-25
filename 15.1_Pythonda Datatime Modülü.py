"""
Bu derste datetime modülü üzerinde çalışacağız.
"""
"""
datetime kütüphanesini import ederek işe başlıyoruz
"""
#import datetime
"""
Aşağıda yazdığımız kodlarda çok fazla modül olduğundan datetime kütüphanesinden
istediğimiz modülü seçip çıkarabiliriz
"""
from datetime import datetime

#print(dir(datetime))
"""
ifadesi ile datetime kütüphanesinin işlevlerini listeleyebiliyoruz.
"""

"""
datetime kütüphanesi içerisinde bulunduğunu görüdüğümüz datetime modülünü görmek için
"""
print(dir(datetime))
"""
örnekler yapacak olursak 
"""

simdi = datetime.now()
"""
Bu günün tarihini saatini alır 
"""
sonuc = datetime.now()
print(sonuc)
sonuc = simdi.year
print(sonuc)
sonuc = simdi.month
print(sonuc)
sonuc = simdi.day
print(sonuc)
sonuc = simdi.hour
print(sonuc)
sonuc = simdi.minute
print(sonuc)
sonuc = simdi.second
print(sonuc)

result = datetime.ctime(simdi)
print(result)
result = datetime.strftime(simdi ,"%Y")
print(result)
result = datetime.strftime(simdi ,"%X")
print(result)
result = datetime.strftime(simdi ,"%d")
print(result)
result = datetime.strftime(simdi ,"%A")
print(result)
result = datetime.strftime(simdi ,"%B")
print(result)

"""
Eğer elimizde string bir ifade varsa ve ben bu string ifadeyi kullanmak istersem
"""
Tarih = "11 Nisan 2004 Pazartesi"
gun,ay,yil,gunismi = Tarih.split()
print(gun + ay + yil)
