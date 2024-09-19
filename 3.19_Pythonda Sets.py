"""
Bu derste ise pythonda bulunan seth listeleri üzerinde çalışıldı.
"""

meyveler = {"karpuz","kavun","elma","muz"}
"""
Sets listelerine index ile erişemeyiz bunun için döngüleri kullanmamız
gerekmektedir.

print(meyveler[0]) // indekslenemez ve bu kullanım hatalıdır.
"""

for x in meyveler:
    print(x)
"""
pythonda döngüler bu şekilde kullanılır.
"""

meyveler.add("çilek")
"""
Şeklinde kullanarak istediğimiz şeyi ekleyebiliriz.
"""

meyveler.update(["mango","kivi"])
"""
Bu kullanım tarzı ile listeleri de ekleyebiliriz.
"""
print(meyveler)

"""
Liste içerisindeki tekrarlı elemanları silmek için.
"""
mylist = [1,2,2,2,3,4,5,6,4,2,8,3,5,4,2,6,7,8,6]
print(set(mylist))

"""
İstemediğimiz şeyleri remove methodu ile silebiliriz.
"""
meyveler.remove("kivi")
print(meyveler)
