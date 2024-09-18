"""
Bu derste verilen örnekleri çözmeye çalıştım.
"""

#--------------------------------------------------------------
# 1-'Hello world' dizisinin baş ve sondaki boşluk karakterlerini silin
# 2- "www.furkan.com" içindeki furkan karakteri dışındaki tüm karakterleri silin.
# 3-'course' karkater dizisinin tüm karakterlerini küçük hary yapın
# 4-'website' değişkeninin içinde kaç tane a karakteri olduğunu hesaplayınız.
# 5-'website' değişkeni www ile başlayıp .com ile bitiip bitmediğini kontrol etmek.
# 6-'website' değişkeni içinde .com ifadesi var mı .
# 7-'course' içindeki karakterlerin hepsi alfabetik mi.
# 8- 'countents' ifadesini satırda 50 karakter içine ekleyip sağ ve soluna 50 karakter * koy.
# 9- 'course' değişkeninde bulunan bütün boşlukları - ifadesi ile değiştirin.
# 10- 'Hello world' karakter dizisinin world ifadesini there olarak değiştir
#--------------------------------------------------------------
website = "https://www.furkan.com"
course = "Sıfırdan ileri seviye Python dersleri ve ASP Core NeT kavramları."

"""
1.örnekte bizim sprit komutunu kullanmamızı istiyor.
"""

result = " Hello World ".sprit()
result = " Hello World ".lsprit() #yalnızca soldaki boşluk karakterlerini siler
result = " Hello World ".rsprit() #yalnızca sağdaki boşluk karakterini siler

"""
2.örnekte bizim strip komutu yerine geçen öğrendiğimiz komutlar ile yapmamız isteniyor.
"""

result = "www.furkan.com".strip('w.com')

"""
3.örneği çözmek için lower kod parçacığını kullanacağız.
"""
result = course.lower()

"""
4.örneği çözebilmek için count komutunu kullanmamız gerekecektir. count methodu 
bir karakter dizisi içinde belli bir karakterin kaç kez geçtiğini sorgulamamızı sağlar.
"""

result = website.count('a')

"""
5.örneği stratswith ve endswith koumutlararı yardımı ile çözeceğim
"""
result = website.startswith("www")
result2 = website.endswith(".com")

"""
6.örneği ise find methodu ile bulacağız 
"""
result = website.find(".com")

"""
7.örnek
"""
result = course.isalpha()
result = 'Hello'.isalha()
result = course.isdigith()

"""
8.örneği center, ljust, rjust kodlarını kullanarak çözmeye çalışacağız.
"""
result = 'contents'.center(50,'*')
result = 'contents'.ljust(25,'*')
result = 'contents'.rjust(25,'*')

"""
9.örneği replace kodu ile yer değiştirerek kullanacağız.
"""
result = course.replace(" ", "-")

"""
10.örneği de aynı method ile çözeceğiz.
"""

result  = 'Hello World !'.replace("Hello","There")
