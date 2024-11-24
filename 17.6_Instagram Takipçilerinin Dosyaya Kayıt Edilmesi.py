from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from login import username, userpassword

driver = webdriver.Chrome()
driver.get("https://instagram.com/")
time.sleep(2)

usernamelogin = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
usernamelogin.send_keys(username)
password = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
password.send_keys(userpassword)
loginbutton = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button")
loginbutton.click()
time.sleep(5)

driver.get(f"https://instagram.com/{username}")
time.sleep(2)

driver.find_element(By.XPATH, "//header/section/ul/li[2]/a").click()
time.sleep(2)

followers_popup = driver.find_element(By.XPATH, "//div[@role='dialog']//ul")

FollowerList = []
action = ActionChains(driver)

for _ in range(10):
    action.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(1)

followers = followers_popup.find_elements(By.XPATH, ".//li//a[@href]")
FollowerList = [user.get_attribute("href") for user in followers]

with open("followers.txt", "w", encoding="utf-8") as file:
    for link in FollowerList:
        file.write(link + "\n")

print(f"{len(FollowerList)} takipçi bağlantısı 'followers.txt' dosyasına kaydedildi.")

driver.close()
