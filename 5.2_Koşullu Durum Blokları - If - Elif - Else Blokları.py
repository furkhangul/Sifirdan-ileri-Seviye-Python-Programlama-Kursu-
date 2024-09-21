
"""
Bu derste elif komut istemcisi üzerinde çalıştım.
"""
x = 10
y = 20

if x >y:
    print("X, Y'den büyüktür")
elif x == y:
    print("X, Y'ye eşittir")
else:
    print("X, Y'den küçüktür.")

#----------------------------------------------

num = int(input("Bir sayı giriniz:"))
if num > 0:
    print("Sayı pozitif")
elif num< 0:
    print("Sayı negatif")
else:
    print("Sayı ne pozitif ne negatif")
