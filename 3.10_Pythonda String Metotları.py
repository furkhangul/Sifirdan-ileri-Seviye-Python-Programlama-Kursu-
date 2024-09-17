
#Bütün string kütüphane çeşitlerini python'un kendi web sitesi üzerinde bulunan kütüphaneler kısmında bulabiliriz.

message = "hello dear, my name is Furkan Gül"
print(message)

"""
bu şekilde mesajımız yazdığımız gibi kullanıcıya çıktı olarak iletilecektir.
"""

message = message.upper()
print(message)

"""
upper komutu ile bütün karakterlerin büyük harfe çevrilmesi gerçekleşir.
"""

message = message.lower()
print(message)

"""
lower komutu ile bütün karakterlerin küçük harfe çevrilmesi gerçekleşir.
"""

message = message.title()
print(message)

"""
title komutu ile bütün kelimelerin ilk harfi büyük harfle başlar.
"""

message = message.capitalize()
print(message)

"""
capitalize komutu ile cümlenin sadece ilk harfi büyük harf ile başlar.
"""

message = message.strip()
print(message)

"""
strip komutu ile girilen değişkenin başındaki boşluk ifadesi kaldırılır.
bu özellik genellikle şifre oluşturulurken kullanılır çünkü boşlukta bi karakterdir
""" 

message = message.split()
print(message)

"""
split komutu ile girdiğimiz cümledeki bütün kelimeleri birbirinden ayırabilme yeteneğine sahip oluyoruz.
"""



index = message.find("Furkan")
print(index)
"""
.find kod parçaığı ile cümle içinde Furkan kelimesini arar ve Furkan kelimesinin F harfinin bulunduğu konumu sayısal olarak
bize aktarır.
"""

isStarts= message.statswith("H")
print(isStarts)
                            
"""
startswith komutu ile cümlenin H harfi ile başlayıp başlamadığını bilgisayar tarafından tarıyoruz
"""

isEnd= message.startsEnd("H")
print(isEnd)
                            
"""
endswith komutu ile cümlenin H harfi ile bitip bitmediğini  bilgisayar tarafından tarıyoruz
"""

message = message.replace('gül','Gül')
print(message)

"""
replace komutu ile cümle içinde kelimelerin başka bir kelime ile değiştirilmesini gerçekleşitebiliyoruz.
"""

message = message.center(100)
print(message)
"""
center komutu ile bizim cümlemizi 100 karakterli bir bilgi içerisine alır.
"""

message = message.center(100,'---')
print(message)
"""
Bu komut ile ise cümlemizin sağına ve soluna eşit bi şekilde --- ifadesini yerleştirilemsini sağlıyoruz.
"""

