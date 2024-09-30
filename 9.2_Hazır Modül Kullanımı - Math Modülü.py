"""
Bu derste hazır modül kullanımına örnekler yapıldı.
"""
import math
"""
İmport kod bloğu ile math kütüphanesini import ettik.
bir modülü indirmek için import kodunu kullanırız."""

value = dir(math)
print(value)
"""
şeklinde yazılarak kütüphanenin içindeki bütün fonksiyonları görebiliyoruz
"""

result = help(math)
print(math)
"""
Yazıldığı zaman ise bize yardım amacı ile kütüphanedeki fonksiyonların 
amacını bize derler
"""

#Example:
value = math.sqrt(49)
print(value)
value = math.floor(4.9)
print(value)
value = math.ceil(72)
print(value)

"""
peki komple bütün kütüphaneyi indirmek yerine from ile istediğimiz modülü
import edebiliriz.
"""

from math import factorial,sqrt,floor

"""
Bu sayede sadece factoriel,sqrt ve floor fonksiyonlarını import ettik.
"""
