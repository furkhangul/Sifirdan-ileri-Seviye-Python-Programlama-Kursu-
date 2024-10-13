"""
Bu dersimizde ise dosyadan bilgilerin nasıl okuanacağını denedik.
"""


#file = open("newfile.txt","r",)
"""
Bu kodda newfile dosyasını açmasını "r" parametresi ile ise okuma işlemi
yapılmaktadır. Eğer "r" yapmazsak bile normal olarak zaten kod kendi kendine
yine okuma işlemi yapabilmektedir.
"""
"""
try:
    file = open("newfile.txt","r")
    print(file)

except FileNotFoundError:
    print("Dosya okunamadı !")
finally:
    print("Dosya kapandı")
    file.close()

"""

#file = open("newfile.txt","r",encoding="utf-8")
"""
Bu kod ile türkçe karakterlerin de rahatlık ile okunmasını
sağlamaktayız.
"""

try:
    file = open("newfile.txt", "r", encoding="utf-8")
    for i in file:
        print(i,end="\n")
except FileNotFoundError:
    print("Dosya Okunamadı !")
finally:
    print("Dosya Kapatıldı !")
    file.close()


"""
For döngüsünün alternatifi ise read() fonksiyonudur
"""
"""
try:
    file = open("newfile.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Dosya Okunamadı !")
finally:
    print("Dosya Kapatıldı !")
    file.close()
content1 = file.read()
print("İçerik 1")
print(content1)
content2 = file.read()
print("İçerik 2")
print(content2)
file.close()
"""

"""
Bu yazımda ise content kısmındaki ifade 11 basamağa kadar
yazılan tüm karakterleri gösteriyor.
"""
"""
try:
    file = open("newfile.txt","r",encoding="utf-8")
    content = file.read(11)
    print(content)
    content = file.read(3)
    print(content)


except FileNotFoundError:
    print("Dosya Okunamadı ! ")
finally:
    print("Dosya Kapatıldı !")
    file.close()
"""

"""
Bu sefer ise readline() methdoduna bakacağız bu method yalnızca satırdaki
bilgileri okur.
"""

"""
try:
    file = open("newfile.txt","r",encoding="utf-8")
    print(file.readline(),end="")
    print(file.readline())
    print(file.readline())


except FileNotFoundError:
    print("Dosya Okunamadı ! ")
finally:
    print("Dosya Kapatıldı !")
    file.close()
"""
"""
Şimdi ise readlines() fonksiyonu açıklayacağız
"""
try:
    file = open("newfile.txt","r",encoding="utf-8")
    liste = file.readlines()
    print(liste)

except FileNotFoundError:
    print("Dosya Okunamadı ! ")
finally:
    print("Dosya Kapatıldı !")
    file.close()
    
    """
    şeklinde listelemeye yarar
    """
