"""
Bu dersimizde ise selenium kütüphanesinin temek programlama fonksiyonları
üzerinde çalışacağız.
"""
import time
from selenium import webdriver

# Tarayıcı sürücüsünü başlat
driver = webdriver.Chrome()

# URL'yi belirtin (http:// veya https:// ile başlamalı)
url = "https://yazilimmuhendisligi.com.tr/wp-admin"

# Belirtilen URL'ye git
driver.get(url)

# Sayfanın yüklenmesini beklemek için uyku süresi
time.sleep(10)

# Pencereyi tam ekran yap
driver.maximize_window()


## Ekran fotosu çekemk için ise

driver.save_screenshot("ekranfotosu.png")
# Sayfa başlığını yazdır
print(driver.title)

# Kapatmadan önce beklemek için uyku süresi
time.sleep(10)

# Tarayıcıyı kapat
driver.close()
