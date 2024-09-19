"""
Bu derste bize verilen örnekleri çözemeye çalıştım.
"""
names = ["Furkan","Kemal","Recep","Mehmet","Selim"]
years = [2004,2005,2006,2007,2008]

#--------------------------------------------------------
# 1-"Cenk" ismini listenin sonuna ekleyiniz.
#--------------------------------------------------------
names.append("Cenk")
print(names)
#--------------------------------------------------------
# 2-"Kemal" ismini listeden siliniz.
#--------------------------------------------------------
names.remove("Kemal")
print(names)
#--------------------------------------------------------
# 3-"Sena" ismini listenin başına ekleyiniz.
#--------------------------------------------------------
names.insert(0,"Sena")
print(names)
#--------------------------------------------------------
# 4- "Furkan" isminin indeksi nedir.
#--------------------------------------------------------
kacinciIndex  = names.index("Furkan")
print(kacinciIndex)
#--------------------------------------------------------
# 5- "Mehmet listenin elemanı mıdır ?
#--------------------------------------------------------
sonuc = "Mehmet" in names
print(sonuc)
#--------------------------------------------------------
# 6-Liste elemanlarını tersine çevirin
#--------------------------------------------------------
names.reverse()
print(names)
#--------------------------------------------------------
# 7-Liste elemanlarını alfabetik olarak sırayınız.
#--------------------------------------------------------
names.sort()
print(names)
#--------------------------------------------------------
# 8- years listesini alfabetik olarak sıralayınız.
#--------------------------------------------------------
years.sort()
print(years)
#--------------------------------------------------------
# 9- str ="Chervolet,Dacia" karakter dizisini listeye çeviriniz.
#--------------------------------------------------------
str ="Chervolet,Dacia"
listele = str.split(",")
print(listele)
#--------------------------------------------------------
# 10-Years dizisinin en küçük ve en büyük elemanı nedir
#--------------------------------------------------------,
print(min(years))
print(max(years))
#--------------------------------------------------------
# 11-Years dizisinde kaç tane 2005 vardır.
#--------------------------------------------------------
sonuc1 = years.count()
print(sonuc1)
#--------------------------------------------------------
# 12-Years dizisinin tüm elemanlarını siliniz.
#--------------------------------------------------------
years.clear()
#--------------------------------------------------------
# 13-Kullanıcının 3 tane marka bilgisini listeleyip saklayınız.
#--------------------------------------------------------
marka = []
print(input("Marka:"))
marka.append(marka)
print(input("Marka:"))
marka.append(marka)
print(input("Marka:"))
marka.append(marka)
print(marka)
