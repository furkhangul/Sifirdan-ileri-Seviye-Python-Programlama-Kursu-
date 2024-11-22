"""
Bu derste fonkisyonlarda iç içe fonkisyonları değerlendirdim.
fonkisyonlar da bi obje olduğunu öğrenerek başlıyoruz.
"""
from contextlib import nullcontext

def greeting(name):
    print("Hello "+name )

print(greeting("Furkan"))
print(greeting)

"""
Şeklinde yazdığımız zaman furkan kelimesini import ettik
"""

sayhello = greeting
print(sayhello)
"""
 SAYHELLO silinirse 
"""
del sayhello

print(greeting)
### yeni bi örnek üzerinde duracak olursak :)
"""
Bu örnekte fonksiyon içerisine fonksiyon yerleştirebiliyoruz.
"""
def outer(num1):
    def inner_increment(num1):
        return num1  + 1
    inner_increment(num1)


outer(10)



### yeni bi örnek yapacak olursak

def factorial(number):
    def inner_factorial(number):
        if number <= 1:
            return 1

        return number * inner_factorial(number  - 1)

    return inner_factorial(number)

print(factorial(4))


