"""
Bu dersimizde ise numpy dizileri ile çalışma üzerine çalışacağız
"""

import numpy as np

result = np.array([1,3,5,7,9])
print(result)
"""
Şeklinde numpy kütüphanesi ile yeni bir liste oluşturabiliyoruz
"""
result1 = np.arange(10,100)
print(result1)
"""
veya sıra halinde bir diziyi oluşturmak için range methodunu da kullanabiliriz
10 ile 100 arasındaki  sayıları diziye eklemeye başlar.
"""
result2 = np.arange(10,100,3)
print(result2)
"""
10 ile 100 arasındaki üçer üçer sayıları diziye eklemeye başlar.
"""
result3 = np.zeros(10)
print(result3)
"""
10 tane 0 girer
"""
result4 = np.ones(5)
print(result4)
"""
5 tane 1 değerini ekler
"""
result5 = np.linspace(0,100,5)
print(result5)

"""
0 ile 100 arasındaki sayıları 5 eşit parçaya böler ve 5 sayıyı bize gösterir.
"""
result6 = np.random.randint(0,10)
print(result6)
"""
0 ile 10 arasında random sayı seçer
"""
result7 = np.random.randin(10)
print(result7)
"""
otomatik bir şeikilde 0 ile 10 arasında seçer
"""
result7 = np.random.randint(0,10,3)
print(result7)
"""
0 ile 10 arasında 3 değer çeker
"""
np_dizi = np.arange(50)
np_multi = np_dizi.reshape(5,10)
print(np_multi.sum(axis=1))
