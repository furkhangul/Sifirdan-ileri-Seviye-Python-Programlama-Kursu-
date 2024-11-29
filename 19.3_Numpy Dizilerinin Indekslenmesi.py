"""
Bu derste numpy ile oluşturduğumuz dizilerdeki elemanlara nasıl ulaşılacağı
ve nasıl kontrol edilebileceği üzerine duruldu.
"""
import numpy as np

dizi = np.arange(0,75,5)
print(dizi)

sec = dizi[5]
print(sec)
"""
buranın mantığı listeleme mantığı ile tamamen aynı 
"""
# dizi içindeki belirli bir aralığı seçmek için dilimleme (slicing) kullanılabilir
# Örneğin:
dilim = dizi[2:6]
print(dilim)

# Burada, dizi[2:6] ifadesi, 2. ve 6. indisler arasındaki elemanları içerir
# (6. indis dahil değil). Yani çıktı şu şekilde olacaktır:
# [10 15 20 25]

# Adım parametresi ile daha esnek dilimleme yapılabilir:
adimli_dilim = dizi[1:8:2]
print(adimli_dilim)

# Bu ifade, 1. indisten başlayıp 8. indise kadar (8 dahil değil) 
# 2'şer adım atlayarak elemanları seçer.
# Çıktı: [ 5 15 25 35]

# Eğer dizi üzerinde bir koşul belirterek elemanlara ulaşmak isterseniz, 
# Boolean dizileriyle seçim yapabilirsiniz:
kosullu_secim = dizi[dizi > 30]
print(kosullu_secim)

# Burada dizi > 30 koşulunu sağlayan elemanlar seçilir.
# Çıktı: [35 40 45 50 55 60 65 70]

# Ayrıca, dizideki bir elemanın var olup olmadığını kontrol edebilirsiniz:
var_mi = 50 in dizi
print(var_mi)  # Çıktı: True

# Eğer bir elemanı dizide değiştirmek isterseniz, indeksleme ile bunu yapabilirsiniz:
dizi[3] = 99
print(dizi)

# Artık dizi şu şekilde güncellenmiş olacak:
# [ 0  5 10 99 20 25 30 35 40 45 50 55 60 65 70]

# Birden fazla elemanı değiştirmek için dilimleme kullanılabilir:
dizi[0:3] = [1, 2, 3]
print(dizi)

# Çıktı:
# [ 1  2  3 99 20 25 30 35 40 45 50 55 60 65 70]

# Bu şekilde, numpy dizileri üzerinde çok çeşitli işlemler gerçekleştirilebilir.
# Bu yöntemler, veri manipülasyonu ve analizi sırasında oldukça faydalıdır.
