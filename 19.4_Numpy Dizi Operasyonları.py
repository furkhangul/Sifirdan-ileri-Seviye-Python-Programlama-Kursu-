"""
Numpy kütüphaneleri ile dizi operatörlerinin nasıl kullanıldığına dair
dersin örneklerini yazdım.
öncelikle kütüphane import ediyoruz.
"""

import numpy as np
from selenium.webdriver.common.devtools.v128.debugger import resume

numbers1 = np.random.randint(0,100,10)
numbers2 = np.random.randint(0,100,10)

print(numbers1)
print(numbers2)

result = (numbers2+ numbers1)
print(result)
"""
ifades ile random olarak alınan 10 elemanlı iki dizi elde ediliyor.
Ardından bu iki dizi toplanılmaya çalışıyor.
Toplama işlemi sırasında numbers1 in 1.elemanı ile numbers2 nin 1. elemanı
toplanır.
"""

"""
veya diğer operatör işlemleri de kolaylıkla yapıılabilmektedir.
"""

result = numbers1 -10
print(result)
result = numbers1 * 10
print(result)
result = numbers1 / 2
print(result)

# Matematiksel işlemler numpy ile oldukça kolaydır.
# Örneğin, sinüs, kosinüs gibi trigonometrik işlemleri dizi elemanları üzerinde gerçekleştirebiliriz:

result_sin = np.sin(numbers1)
print("Sinüs Değerleri:")
print(result_sin)

result_cos = np.cos(numbers1)
print("Kosinüs Değerleri:")
print(result_cos)

result_tan = np.tan(numbers1)
print("Tanjant Değerleri:")
print(result_tan)

# Logaritmik işlemler de yapılabilir:
result_log = np.log(numbers1 + 1)  # 0 değerlerini engellemek için 1 ekliyoruz
print("Logaritmik Değerler:")
print(result_log)

# Karekök işlemi:
result_sqrt = np.sqrt(numbers1)
print("Karekök Değerleri:")
print(result_sqrt)

# Üstel işlemler:
result_exp = np.exp(numbers1)
print("Üstel Değerler (e^x):")
print(result_exp)

# Elemanların karesi:
result_square = numbers1 ** 2
print("Elemanların Karesi:")
print(result_square)

# Minimum, maksimum, toplam ve ortalama hesaplama:
min_value = np.min(numbers1)
max_value = np.max(numbers1)
sum_value = np.sum(numbers1)
mean_value = np.mean(numbers1)

print("Dizinin En Küçük Elemanı:", min_value)
print("Dizinin En Büyük Elemanı:", max_value)
print("Dizinin Toplamı:", sum_value)
print("Dizinin Ortalaması:", mean_value)

# İki dizi arasındaki element bazlı işlemler:
result_div = numbers1 / (numbers2 + 1)  # Bölme işlemi sırasında sıfıra bölme hatasını önlemek için +1 ekliyoruz
print("Eleman Bazlı Bölme İşlemi:")
print(result_div)

result_mod = numbers1 % numbers2
print("Eleman Bazlı Mod Alma:")
print(result_mod)

# Dizi elemanlarını sıralama:
sorted_numbers1 = np.sort(numbers1)
print("Sıralanmış Dizi (numbers1):")
print(sorted_numbers1)

# Elemanların pozitif-negatif kontrolü:
is_positive = numbers1 > 0
print("Pozitif Elemanlar (True/False):")
print(is_positive)

# İstatistiksel analiz:
std_dev = np.std(numbers1)  # Standart sapma
var = np.var(numbers1)      # Varyans
print("Dizinin Standart Sapması:", std_dev)
print("Dizinin Varyansı:", var)

# Matris işlemleri (diziyi yeniden şekillendirme):
matrix = numbers1.reshape(2, 5)  # 2 satır, 5 sütunlu matris oluşturma
print("Yeniden Şekillendirilmiş Matris:")
print(matrix)

# Matris transpozunu alma:
matrix_transpose = matrix.T
print("Matrisin Transpozu:")
print(matrix_transpose)

# Bu örneklerle, numpy kullanarak geniş bir yelpazede matematiksel ve istatistiksel işlemler yapabilirsiniz.



