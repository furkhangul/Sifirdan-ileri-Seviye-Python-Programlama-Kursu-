"""
bu derste python'da listeler konusu üzerinde duruldu.
Biz geçen derslerde öğrendiğimiz gibi stringler ile bir değişkenin
içindeki kelimeleri listeleyebiliyorduk.
"""

message = "Hello World My Name is Furkan Gül".split()
print(message)

"""
Burada gördüğümüz gibi 'split' methodu ile parçalara ayırdık.
"""

"""
yine aynı şekilde köşeli parantez kullanarakta bu listelemeye ulaşabiliriz.
"""

my_list = [1,2,3]
print(my_list)

my_list2 = ['bir',2,True,]
print(my_list2)

"""
veya iki listeyi düz bi şekilde de birleşitrebilirz.
"""

list1=["one","two","tree"]
list2=["four","five","six"]

topList = list1 + list2

print(topList)
"""
işte bu örnekteki gibi
"""

"""
Başka bir konuya değinecek olursam eğer yukarıda message değişkenini normal 
olarak [] içinde çağırsak bize n. harfi verirdi fakat split kullandığımız
için artık çağırıldığı zaman bize direkt Hello kelimesini getirecektir.
"""

"""
Yukarıda iki listeyi toplayıp tek liste haline getirmeyi göstermiştim.
Şimdi ise liste içinde nasıl liste saklanır onu göstereyim.
"""

listem1 = ["Furkan","Gül",20,"Yazılım mühendisliği"]
listem2 = ["Fatih","Aslan",22,"Elektirik mühendisliği"]
toplamListe = listem1 + listem2
toplamListe2 = [listem1,listem2]
print("ORNEK BİR:",toplamListe)
print("ORNEK IKI:",toplamListe2)

print(toplamListe2[0])
"""
burada da liste içindeki listeden birini seçtim
"""



