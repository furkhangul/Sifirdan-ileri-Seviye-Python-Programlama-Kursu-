"""
Numpy veri analizinde kullanılan oldukça popüler bir kütüphanedir.
Kullanım alanı oldukça geniştir.
"""
# pip install numpy ifadesi ile indirebiliriz.


#python listeleri

py_list = [1,2,3,4,5,6,7,8,9]
"""
Numpy kütüphanesi olmadan klasik dizi işlemlerini gerçekleştirebiliriz.
fakat ileride büyük verilerin daha kompleks bir şekilde kullanılması için numpy
kütüphanesine ihtiyaç duyarız.
"""

import numpy as np
"""
Burada numpy kütüphanesini import ettik ve kısaltma olarak np kullandık
"""

np_array = np.array([1,2,3,4,5,6,7,8,9,0])
print(type(py_list))
print(type(np_array))
"""
şeklinde yazdığımız zaman iki farklı türde listeleme gerçekleştiğini görmekteyiz.
"""

py_multi=([0,1,2,3,4],[5,6,7,8,9])
np_multi = np_array.reshape(2,5)
"""
şekilinde listeyi düzenleyebiliyoruz.
liste elemanlarını iki parçaya böldü mesela
"""

print(py_multi)
print(np_multi)
