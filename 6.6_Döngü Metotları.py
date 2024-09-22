"""
İşimizi kulaylaşıracak birkaç yardımcı koda dikkat ediyoruz.
"""
from operator import index

for items in range(10):
    print(items)

"""
range kod bloğu ile aralığı belirleyerek ekran çıktısı çıarabiliriz
"""

for i in range(2,100):
    print(i)

"""
şeklinde yazıldığında 2 den 100e kadar bize çıktı verir.
"""

greeting = "Hello There"
for letter in greeting:
    print(letter)

"""
bu kod ile birlikte indexte almak  istersek enumerate kodu kullanılır.
"""

for index,letter in greeting:
    print(f"index:{index} letter: {greeting[index]}")

for item in enumerate(greeting):
    print(item)
"""
zip ile de kısaltma yapabiliriz.
"""

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

print(list(zip(list1,list2)))

"""
şeklinde yazıldığında artık listeler birleştirilebiliyor.
"""
list3 = [100,200,300,400,500]
print(list(zip(list1,list2,list3)))
