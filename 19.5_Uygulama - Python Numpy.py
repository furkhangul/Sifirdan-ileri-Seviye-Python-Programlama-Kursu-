# 1.soru: (10,20,30,45,60 değerlerine sahip numpy dizisi oluştur
import numpy as np
diziolustur = np.array([10,20,30,45,60])
print(diziolustur)

#2.soru: (5-15) arasındaki sayılarla numpy dizisi oluştur.
araliklidizi = np.arange(5,15)
print(araliklidizi)

#3.soru: (50,100) arasıdnaki sayıları 5er 5er dizi yap
beserbeser = np.arange(50,100,5)
print(beserbeser)

#4.soru: 10 elemanlı 0 lardan oluşan dizi oluştur.
onsifir = np.zeros(10)
print(onsifir)

#5.soru: 10 elemanlı 1 lerden oluşan dizi oluştur.
onbir = np.ones(10)
print(onbir)

#6.soru: (0,100) arasıdnaki sayıları 5 eşit parçada böl
besesit = np.linspace(0,100,5)
print(besesit)


#7.soru: (0,50) arasıdnaki 3 rastgele tam sayı oluştur
rastgelebessayi = np.random.randint(0,50,3)
print(rastgelebessayi)

#8.soru: (-1-1) arasıdnaki 3 rastgele  sayı oluştur
eksibirvebirarasinda = np.random.randn(3)
print(eksibirvebirarasinda)

#9.soru: (3x5) boyutlarında (10-50) arasındaa rastgele bir matris oluştur.
rastgelematris = np.random.randint(10,50,15).reshape(3,5)
print(rastgelematris)

#10.soru: Üretilen matrisin satır ve sütun sayılarının toplamını hesaplayınız.
rowtotal =  rastgelematris.sum(axis=1)
coltotal =  rastgelematris.sum(axis=0)
print(rowtotal)
print(coltotal)

#11.soru: Üretilen matrisin en büyük, en küçük ve ortalaması nedir?
max_value = np.max(rastgelematris)
print( max_value)
min_value = np.min(rastgelematris)
print( min_value)
mean_value = np.mean(rastgelematris)
print( mean_value)

#12.soru: Üretilen matrisin en büyük değerinin indeksi kaçtır?
max_value = np.max(rastgelematris)

max_index = np.unravel_index(np.argmax(rastgelematris), rastgelematris.shape)
print( max_value)
print( max_index)

#13.soru: (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
dizi = np.arange(10, 21)
ilk_uc_eleman = dizi[:3]
print(ilk_uc_eleman)

#14.soru: Üretilen dizinin elemanlarını tersten yazdırın.
dizi = np.arange(10, 21)
ters_dizi = dizi[::-1]
print(ters_dizi)

#15.soru: Üretilen matrisin ilk satırını seçiniz.
ilk_satir = rastgelematris[0]
print(ilk_satir)

#16.soru: Üretilen matrisin 2. satır 3. sütunundaki elemanı hangisidir?
eleman = rastgelematris[1, 2]
print(eleman)

#17.soru: Üretilen matrisin tüm satırlardaki ilk elemanını seçiniz.
ilk_sutun = rastgelematris[:, 0]
print(ilk_sutun)

#18.soru:  Üretilen matrisin her bir elemanının karesini alınız.

karesinial = np.random.randint(0,10,1)
uzunluk = len(karesinial)
for i in uzunluk:
    print(karesinial[i] * karesinial[i])
