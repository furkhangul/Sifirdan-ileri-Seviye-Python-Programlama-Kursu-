"""
Bu bölümde fonksiyonların kullanımı hakkında bilgileri derledim.
methodların kullanım örnekleri aşağıda yer alıyor:
"""

liste = ["a","b","c","d","e"]
def harfekle():
    ekle = input("Lütfen harf ekle:")
    liste.append(ekle)

harfekle()
print(liste)

#---------------------------------------------------------
#---------------------------------------------------------

def yashesapla():
    dogum = int(input("Lütfen  doğum yılınızı giriniz:"))
    yas = 2024 - dogum
    print(f"Yaşınız: {yas}")
yashesapla()
def emeklilikhesaplama(yas):
    age = yashesapla(yas)
    emeklilik = 65 - age
    if emeklilik > 0 :
        print(f"emeliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Zaten emeklisiniz.")

emeklilikhesaplama()
