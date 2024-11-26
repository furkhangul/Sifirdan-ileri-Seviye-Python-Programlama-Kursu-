import re
"""
Bu derste Regular Expression kütüphanesi ile çalışıldı.
Python'daki re modülü, düzenli ifadelerle (regular expressions) çalışmayı sağlar. Bu modül, metin arama, eşleme ve değiştirme gibi birçok işlemi kolaylaştırır.
"""
print(dir(re))


"""
re.match(pattern, string)
Belirtilen düzenli ifadeyi metnin başında arar. Sadece metnin başındaki eşleşmeleri döndürür.
"""
result = re.match(r"Hello", "Hello world!")
if result:
    print("Eşleşti:", result.group())
else:
    print("Eşleşmedi")

"""
Hello metnin başında olduğundan eşleşir.
"""
####################################################################
"""
re.search(pattern, string)
Metin içinde düzenli ifadeye uyan ilk eşleşmeyi arar (başlangıçtan bağımsız).
"""
result = re.search(r"world", "Hello world!")
if result:
    print("Bulundu:", result.group())
"""
world metin içinde geçtiği için eşleşir.
"""
####################################################################
"""
re.findall(pattern, string)
Metin içinde düzenli ifadeye uyan tüm eşleşmeleri liste olarak döndürür.
"""
result = re.findall(r"\d+", "Bugün 3 elma, 7 muz aldım.")
print("Eşleşmeler:", result)
"""
\d+ (bir veya daha fazla rakam) ifadeleri bulur. Çıktı: ['3', '7']
"""
####################################################################
"""
re.finditer(pattern, string)
Metin içinde düzenli ifadeye uyan tüm eşleşmeleri bir iterator olarak döndürür.
"""
matches = re.finditer(r"\w+", "Python öğreniyorum!")
for match in matches:
    print("Eşleşme:", match.group())
"""
\w+ harf ve rakamlardan oluşan kelimeleri bulur.
"""
####################################################################
"""
 re.split(pattern, string, maxsplit=0)
Düzenli ifadeyi kullanarak metni böler. Opsiyonel maxsplit parametresi ile en fazla kaç bölme yapılacağını belirtebilirsiniz.
"""
result = re.split(r"\s+", "Python öğreniyorum çok eğlenceli.")
print("Bölünmüş metin:", result)
"""
\s+ boşluklara göre böler. Çıktı: ['Python', 'öğreniyorum', 'çok', 'eğlenceli.']
"""
####################################################################
"""
re.sub(pattern, repl, string, count=0)
Düzenli ifadeye uyan kısımları belirtilen repl ile değiştirir. count parametresi değiştirme sınırını belirler.
"""
result = re.sub(r"\d", "*", "Şifre: 1234")
print("Sonuç:", result)
"""
Rakamları * ile değiştirir. Çıktı: Şifre: ****
"""
####################################################################
"""
re.subn(pattern, repl, string, count=0)
re.sub ile aynı işlemi yapar, ancak bir tuple döner: (değiştirilmiş metin, değişiklik sayısı).
"""
result = re.subn(r"\s+", "-", "Python öğreniyorum çok eğlenceli.")
print("Sonuç:", result)
"""
 Boşlukları - ile değiştirir. Çıktı: ('Python-öğreniyorum-çok-eğlenceli.', 3)
"""
####################################################################
"""
re.compile(pattern, flags=0)
Düzenli ifadeyi bir nesne olarak derler. Bu, aynı deseni tekrar tekrar kullanırken faydalıdır.
"""
pattern = re.compile(r"\d+")
result = pattern.findall("Bugün 3 elma, 7 muz aldım.")
print("Sonuç:", result)
"""
Daha performanslı ve düzenli kod yazmak için kullanılır.
"""
####################################################################
"""
Flags (Bayraklar)
re modülü bazı bayraklar ile düzenli ifadelerin davranışını değiştirmenize olanak tanır:

re.IGNORECASE (veya re.I): Büyük/küçük harf farkını göz ardı eder.
re.MULTILINE (veya re.M): Çok satırlı eşleşme sağlar.
re.DOTALL (veya re.S): . ifadesinin yeni satır karakterini de eşlemesini sağlar.
re.VERBOSE (veya re.X): Daha okunabilir düzenli ifadeler yazmanıza olanak tanır.
"""
text = "Merhaba\nDünya"

# DOTALL örneği
result = re.search(r".+", text, flags=re.DOTALL)
print("Sonuç:", result.group())
####################################################################
"""
Gruplama ve Geri Referanslar
Gruplama:
Düzenli ifadede parantezler ( ) ile gruplar oluşturabilirsiniz.
"""
result = re.search(r"(elma|muz)", "Ben elma seviyorum.")
print("Eşleşen grup:", result.group())
"""
Geri Referanslar:
Grupları tekrar kullanabilirsiniz.
"""
result = re.search(r"(\d+)-\1", "123-123")
print("Sonuç:", result.group())
####################################################################
"""
re.escape(string)
Metindeki özel karakterleri kaçar (\) ile işaretler.
"""
pattern = re.escape("a.b+c?")
print("Kaçış yapılmış desen:", pattern)
"""
a.b+c? gibi bir deseni düzenli ifade olarak kullanmak için uygular.
"""


