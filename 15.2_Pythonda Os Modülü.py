"""
Bu dersimizde OS modülü üzerinde çalışmaktayız.
"""
import os
print(dir(os))
"""
Görülüdüğüz üzere onlarca methodun olduğu kalabalık bir dosya 
"""
print(os.name) #İfadesi ile işletim sistemini ifade eder nt = windows kullandığımı ifade eder
print(os.getcwd()) #İfadesi ise dosyamızın konumunu görmemizi sağlamaktadır.
os.mkdir("downloads") #İfadesi ile downloads adından dizinimizde bir dosya oluşturur.
os.chdir("C://") # ifadesi ile istediğimiz bölgeye path ile ulaşabiliyoruz.
os.rmdir("yeni_klasor")  # Boş bir klasörü siler.
os.removedirs("ana_klasor/alt_klasor")  # Tüm yolu siler (boşsa).
print(os.listdir("."))  # Mevcut dizindeki dosya ve klasörleri listeler.
print(os.listdir("."))  # Mevcut dizindeki dosya ve klasörleri listeler.
print(os.path.isdir("yeni_klasor"))  # True dönerse bir klasördür.
print(os.path.isfile("dosya.txt"))  # True dönerse bir dosyadır.
print(os.path.exists("dosya.txt"))  # True dönerse dosya veya klasör var.
print(os.path.getsize("dosya.txt"))  # Dosyanın boyutunu bayt cinsinden döner.
print(os.name)  # "nt" Windows için, "posix" Linux/Mac için döner.
print(os.environ)  # Tüm ortam değişkenlerini bir sözlük olarak döner.
os.remove("dosya.txt")  # Belirtilen dosyayı siler.
os.system("cls")  # Windows'ta ekranı temizler.
os.system("ls")   # Linux/Mac'te mevcut dosya ve klasörleri listeler.
os.rename("eski_dosya.txt", "yeni_dosya.txt")  # Dosya adını değiştirir.
path = os.path.join("C:/Users", "Username", "Desktop")  # Dinamik olarak yol oluşturur.
print(path)  # C:/Users/Username/Desktop
print(os.path.split("C:/Users/Username/Desktop/dosya.txt"))  # ('C:/Users/Username/Desktop', 'dosya.txt')
print(os.path.splitext("dosya.txt"))  # ('dosya', '.txt')
print(os.getenv("PATH"))  # PATH değişkenini döner.
print(os.getenv("TEMP"))  # Windows'ta geçici dosya yolunu döner.
os.chdir(os.getenv("TEMP"))  # Geçici dizine geçiş yapar.
print(os.path.dirname(os.path.abspath(__file__)))  # Çalışan dosyanın tam yolunu verir.
import string
drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]
print(drives)  # Örn: ['C:\\', 'D:\\', 'E:\\']
"""
CMD ÜZERİNDEN HAREKET İÇİN :
"""
os.system("dir")  # Windows için dizindeki dosyaları listeler
os.system("ls")   # Linux/Mac için dizindeki dosyaları listeler
os.system("ping www.google.com")  # Google'a ping atar


