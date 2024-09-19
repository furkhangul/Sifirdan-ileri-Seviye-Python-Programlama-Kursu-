"""
Bu bölümde listeler için örnenkler yapıcağız.
"""

#-----------------------------------------
# 1-BMW , OPEL , MERCEDES, MAZDA  elemanlarına sahip liste oluştur
#-----------------------------------------
otomobil = ["BMW","Opel", "Mercedes", "Mazda"]
print(otomobil)

#-----------------------------------------
# 2-Liste kaç elemanlıdır ?
#-----------------------------------------
elemanSayisi= len(otomobil)
print("{0} elemanlı bir listedir.".format(elemanSayisi))

#-----------------------------------------
# 3-Listenin ilk ve son elemanı nedir ?
#-----------------------------------------
print(otomobil[0])
print(otomobil[elemanSayisi-1])

#-----------------------------------------
# 4-Mazda değerini Toyota ile değiştirin.
#-----------------------------------------
otomobil[3] = ("Toyota")

#-----------------------------------------
# 5-Mercedes listenin bir elemanı mıdır ?
#-----------------------------------------
elemanMi = 'Mercedes' in otomobil
print(elemanMi)
#-----------------------------------------
# 6- listenin -2. indeksindeki değer nedir
#-----------------------------------------
cevap = otomobil[-2]
print(cevap)

#-----------------------------------------
# 7-Listenin ilk 3 elemanını alın.
#-----------------------------------------

ilkuc = otomobil[0:3]
print(ilkuc)

#-----------------------------------------
# 8- Listenin son 2 elemanına "toyota" ve "renault" değerlerini ekleyin
#-----------------------------------------
otomobil[-2: ] = ["Renault","Toyota"]
print(otomobil)

#-----------------------------------------
# 9-Listeye "Audi" ve "Nissan" değerlerini ekleyelim.
#-----------------------------------------
otomobil = otomobil + ["Audi","Nissan"]
print(otomobil)

#-----------------------------------------
# 10-Listenin son elemanını silin.
#-----------------------------------------
del otomobil[-1]
print(otomobil)

#-----------------------------------------
# 11-Listedeki elemanları tersten yazdırın.
#-----------------------------------------

sonuc = otomobil[::-1]
print(sonuc)
#-----------------------------------------
# 12-Aşağıdaki verileri bir liste içinde saklayınız.
#-----------------------------------------

Ogrenci1 = ["Furkan","Gül",2004,[60,70,80]]
Ogrenci2 = ["Mustafa","Şentop", 2002,[100,80,90]]
Ogrenci3 = ["Kerim","Aslan",2006,[80,40,60]]

#-----------------------------------------
# 13-Liste elemanlarını çağırın.
#-----------------------------------------
print(Ogrenci1)
print(Ogrenci2)
print(Ogrenci3)
