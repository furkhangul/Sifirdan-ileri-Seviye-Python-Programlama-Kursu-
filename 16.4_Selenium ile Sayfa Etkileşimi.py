"""
Bu dersimzde ise selenium ile bir etikete, bir login butonuna veya bir forum
kısmına nasıl erişebiliriz, nasıl kontrol edebileceğimizi çalışacağız.
"""

"""
öncelikle web sitesi üzerinden nelerin nereden ulaşılacağını anlatan selenium
web sitesini paylaşıyorum:
https://selenium-python.readthedocs.io/  > Locating kısmını kullanarak ulaşırız.
diğer gerekli dükümanlara web sitesi üzerinden ulaşabiliriz.
"""

"""
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")

ifadeleri selektörlere nasıl ulaşabileceğimizi bize göstermektedir. 
"""

"""
Örnek verecek olursak: 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://yazilimmuhendisligi.com.tr/wp-admin"
driver.get(url)
time.sleep(1)
driver.maximize_window()
username = driver.find_element(By.ID, 'user_login')
username.send_keys("furkhangul")
time.sleep(1)
password = driver.find_element(By.ID, 'user_pass')
password.send_keys("123456576")
time.sleep(1)
loginbutton = driver.find_element(By.ID, 'wp-submit')
time.sleep(5)
loginbutton.click()
driver.close()
