"""
Bu derste ise login ve takipçi kısmına giriş yaptıktan sonra tüm takipçileri çekmeye yarayan kodu kodladık .
Bunun için xpath ve selector gibi ifadeler kullanıldı.
İnstagram takip edilmeyenleri listeleme programı bu mantıkta çalışmaktadır !
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from login import username, userpassword

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://instagram.com/"
driver.get(url)
time.sleep(2)

usernamelogin = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
usernamelogin.send_keys(username)
password = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
password.send_keys(userpassword)
loginbutton = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button")
loginbutton.click()
time.sleep(8)

profile_url = f"https://instagram.com/{username}"
driver.get(profile_url)
time.sleep(2)

lookfollowers = driver.find_element(By.XPATH, "//header/section/ul/li[2]/a")
lookfollowers.click()
time.sleep(3)

followers_popup = driver.find_element(By.XPATH, "//div[@role='dialog']//ul")
actions = ActionChains(driver)

followers_links = set()
last_height = 0

while True:
    followers = followers_popup.find_elements(By.XPATH, ".//li//a[@href]")
    for follower in followers:
        followers_links.add(follower.get_attribute("href"))

    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
    time.sleep(2)

    new_height = driver.execute_script("return arguments[0].scrollTop", followers_popup)
    if new_height == last_height:
        break
    last_height = new_height

print("Toplam takipçi:", len(followers_links))
for link in followers_links:
    print(link)
driver.quit()
