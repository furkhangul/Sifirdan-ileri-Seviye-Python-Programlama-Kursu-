"""
Bu kod ile istenilen takipçiyi takip edebiliyoruz. Bu bot sayesinde bir dizin kullanıcıyı tek seferde takibe alabiliyoruz !
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
"""
Login kütüphanesini ben kendim kurdum yeni bir py olarak açıyoruz ardından burada şifre ve kullanıcı adını giriyorum
"""
from login import username,userpassword
driver = webdriver.Chrome()
url = "https://instagram.com/"
driver.get(url)
time.sleep(1)
usernamelogin = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
usernamelogin.send_keys(username)
password = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
password.send_keys(userpassword)
loginbutton = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]")
loginbutton.click()
time.sleep(8)
url = f"https://instagram.com/{username}"
driver.get(url)
time.sleep(1)
follow = input("Takip etmek istediğin kullanıcı adı: ")
driver.get(f"https://instagram.com/{follow}")
time.sleep(1)
if driver.find_element(By.XPATH,"//div[contains(text(),'Takiptesin')]").text == "Takiptesin":
    print("Zaten takip ediliyor ! ")
else:
    driver.find_element(By.XPATH,"//header/section[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//body/div[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]").click()
    print("Başarılı bir şekilde takip edildi !")
time.sleep(10)
driver.close()
