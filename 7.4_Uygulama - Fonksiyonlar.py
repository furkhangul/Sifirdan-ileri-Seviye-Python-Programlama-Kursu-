"""
Bu derste ise fonkisyonlar ile alakalı örnekler çözeceğim
"""


"""
1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız
"""

tekrarsayisi = int(input("TEKRAR SAYISI:"))
def tekrar():
    for x in range(tekrarsayisi):
        print("Hello World !")

tekrar()

"""
Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye ekleyen
fonksiyonu yazınız.
"""

list =[]
resault = True
while resault == True:
    if resault == True:
        yeni = input("Lütfen bir karakter giriniz:")
        list.append(yeni)
        devam = input("Yeni eleman ekle (e):")
        if devam == "e":
            continue
        else:
            break
    elif resault == False:
        break
    else:
        break

print(list)

"""
Gönderilen iki sayı arasındaki bütün asal sayıları bulan program
yazınız
"""

birincideger = int(input("1.değer: "))
ikincideger = int(input("2.değer: "))


def asalhesapla(birincideger, ikincideger):
    if birincideger > ikincideger:
        alt_sinir, ust_sinir = ikincideger, birincideger
    else:
        alt_sinir, ust_sinir = birincideger, ikincideger

    for x in range(alt_sinir, ust_sinir):
        if x < 2:
            continue

        sayac = 0
        for a in range(1, x + 1):
            if x % a == 0:
                sayac += 1

        if sayac == 2:
            print(f"{x} sayısı bir asal sayıdır!")


asalhesapla(birincideger, ikincideger)

"""
Girilen bir sayının bölenlerinin listelerinin olduğu liste oluşturma!
"""

list = []
deger = int (input("Lütfen bir değer giriniz: "))

def bolenler():
    for x in range(1,deger+1):
        if (deger % x == 0):
            list.append(x)



    print(f"Girdiğiniz {deger} sayısının tam bölenleri: {list}")

bolenler()
