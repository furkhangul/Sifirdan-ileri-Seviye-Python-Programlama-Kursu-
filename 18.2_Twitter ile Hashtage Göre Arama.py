"""
Bu bölümde twitter giriş bölümünü kodladım. koddaki xpath uzantıları değişebilir. bunun değiştirilmesi için ChoPath chrome
eklentisini kullanıyorum.
Giriş bölümü daha hızlı olabilir.
"""
"""
Bu bölümde ise giriş yapıldıktan sonra hesabımız üzerinden search methodunu kullanmak. Keys.Enter tuşu için Keys kütüphanesini
import ettim.
"""

from selenium.webdriver.common.by import By
from twitterLogin import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver  = webdriver.Chrome()
driver.get("https://x.com/i/flow/login/")
time.sleep(2)
driver.find_element(By.XPATH, "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[4]/label[1]/div[1]/div[2]/div[1]/input[1]").send_keys(username)
driver.find_element(By.XPATH,"//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[2]").click()
time.sleep(0.8)
driver.find_element(By.XPATH,"//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/label[1]/div[1]/div[2]/div[1]/input[1]").send_keys(password)
driver.find_element(By.XPATH,"//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/span[1]/span[1]").click()
time.sleep(2)
search =driver.find_element(By.XPATH,"//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]")
search.send_keys("furoftheweak")
search.send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
