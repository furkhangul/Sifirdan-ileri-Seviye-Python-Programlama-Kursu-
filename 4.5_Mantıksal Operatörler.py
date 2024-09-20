"""
Bu derste mantıksal operatörler üzerinde çalışıldı.
"""
x = 115
cevap = 15<x<200
print(cevap)
"""
bazen bi değişken içerisinde birden fazla müdahil dahil olacağından
mantıksal operatörlere ihtiyaç duyarız.
"""

result = (x>5) and (x<150)

print (result)

"""
örnek olarak bi oyun tarzını taklit edersek 
oyunda hakkımız varsa ve e harfine basarsak oyuna devam edebileceğimizi
aktaran bi oyun olsun 
"""
hak = 5
devam = input("Bas:")

sonuc = (hak>0) and (devam =="e")
print(sonuc)


"""
veya matematiksel ifadeler için de kullanabiliriz.
"""

result = (x>0) or (x%2==0)
print(result)
