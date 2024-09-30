#main.py

import _random

result = help(_random)
print(result)
result = _random.number
print(result)
result = _random.numbers
print(result)
result = _random.person["name"]
print(result)
result = _random.person["age"]
print(result)
result = _random.modul(10)
print(result)

o = _random.person()
o.speak()

###########################################################################################
#_random.py

"""
Bu derste ise bir modülü kendimizi oluşturmaya çalışacağız
örnek olarak bir number adında bir değerimiz olsun.
"""
print("modül eklendi")
number = 10
numbers = [1,2,3]
person ={
    "name":"Furkan",
    "age":"20",
    "city":"Siirt"
}

def modul(x):
    """
    Fonksiyon hakkıdna bilgiler
    :param x:
    :return:
    """

