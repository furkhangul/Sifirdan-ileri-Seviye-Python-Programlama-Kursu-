"""
Bu aşamadan sonra decorator fonksiyon özellikleri üzerinde duracağız !
"""
from typing import final

""" 
Bu fonksiyon ile bir özelliği birden fazla yerde kullanabilmemizi sağlıyor 
"""

def deneme(fonk):
    def wrapper():
        print("Fonksiyondan önceki işlemler")
        fonk()
        print("Fonksiyondan sonraki işemler")
    return wrapper

@deneme
def merhaba(name):
    print("Merhaba",name)

def sayGreeting():
    print("Greeting")

merhaba = deneme(merhaba)

merhaba("Furkan")

"""
Veya 
"""
import math
import time
def usalma(a,b):
    start = time.time()
    print(math.pow(a,b))

    finish = time.time()
    print("Fonksiyon: "+ str(finish-start) + "saniye sürdü")
def faktoriyel(num):
    print(math.faktoriel(num))
