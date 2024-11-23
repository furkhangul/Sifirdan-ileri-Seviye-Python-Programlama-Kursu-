"""
Bu derste ise instagrama hızlı giriş yapıpı bu giriş üzerinden veri çekebilen bir programın kodlanmasını yaptım.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WebDriver başlatma
driver = webdriver.Chrome()

# Instagram giriş URL'si
url = "https://www.instagram.com/accounts/login/"
driver.get(url)

# Sayfanın yüklenmesi için bekleme süresi
time.sleep(5)

# Pencereyi büyüt
driver.maximize_window()

# Kullanıcı adı alanına erişim (ID veya diğer locator'ları kendinize göre değiştirin)
username = driver.find_element(By.NAME, 'username')  # 'username' doğru locator'dır
username.send_keys("your_username")  # Kullanıcı adınızı buraya yazın
time.sleep(1)

# Şifre alanına erişim
password = driver.find_element(By.NAME, 'password')  # 'password' doğru locator'dır
password.send_keys("your_password")  # Şifrenizi buraya yazın
time.sleep(1)

# Giriş butonuna erişim
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Giriş butonu locator
login_button.click()

# Giriş işlemi tamamlanana kadar bekle
time.sleep(5)

# DM kutusuna yönlendirme
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(5)

# Oturumu kapat ve tarayıcıyı kapat
driver.close()
