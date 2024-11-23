"""
Bu derste geçen dersten arta kalan giriş kısmını dizayn ettim
ayrıca instagram girişi için hızlı bir panel eklemiş olduk.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
url = "https://www.instagram.com/accounts/login/"
driver.get(url)
time.sleep(1)
username = driver.find_element(By.NAME, 'username')
username.send_keys("furoftheweak")
time.sleep(1)
## lan şifremi çalarsan iyi küfür ederim bu hesap benim fake hesabımdı.
password = driver.find_element(By.NAME, 'password')
password.send_keys("furkanbaba00")
time.sleep(1)
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(10)
url = "https://instagram.com/furoftheweak"
driver.get(url)
time.sleep(3)
followers = driver.find_element(By.CLASS_NAME, "x5n08af x1s688f x1lliihq")
followers.click()
time.sleep(10)
driver.close()
