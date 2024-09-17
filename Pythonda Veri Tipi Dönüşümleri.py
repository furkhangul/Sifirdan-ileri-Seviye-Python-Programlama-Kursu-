x = input('1.sayı: ') # x = 10
y = input('2.sayı: ') # y = 20
toplam = x + y
print(toplam) # Toplam => 1020

#Peki ne yapmamız gerekiyor

x = input('1.sayı: ') # x = 10
y = input('2.sayı: ') # y = 20
print(type(x))
print(type(y))
toplam = int(x) + int(y)
print(toplam)

"""
Bunların tamamı bi örnek ise bunun devamında 
"""
x = 5 #int
y =2.5 #float
name= "Furkan" #string
isOnline = True #bool

print(type(x))
print(type(y))
print(type(name))
print(type(isOneline))

"""
PEKİ YUKARIDA YAPTIĞIMIZ GİBİ STRİNG DEĞERİNDEKİ Bİ DEĞİŞKENİ BAŞKA BİR DEĞİŞKENE DE ÇEVİREBİLİR MİYİZ 
Tabiki evet, bu örnekte floata çevirmeyi denedim
"""
x = float(x)
print(x)
print(type(x)) #Sonuc => 5.0 --type:float

