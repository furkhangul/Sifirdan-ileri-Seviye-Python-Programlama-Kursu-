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
from selenium.webdriver.common.keys import Keys
from twitterLogin import username, password
from selenium import webdriver
import time

# Driver başlatma ve siteye giriş
driver = webdriver.Chrome()
driver.get("https://x.com/i/flow/login/")
time.sleep(2)

# Kullanıcı adı ve şifre ile giriş yap
driver.find_element(By.XPATH, "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[4]/label[1]/div[1]/div[2]/div[1]/input[1]").send_keys(username)
driver.find_element(By.XPATH, "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[2]").click()
time.sleep(0.8)
driver.find_element(By.XPATH, "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/label[1]/div[1]/div[2]/div[1]/input[1]").send_keys(password)
driver.find_element(By.XPATH, "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/span[1]/span[1]").click()
time.sleep(2)

# Arama işlemi
search = driver.find_element(By.XPATH, "//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]")
search.send_keys("python")
search.send_keys(Keys.ENTER)
time.sleep(5)

# Scroll işlemi ve tweetleri toplama
tweets = []
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Sayfadaki tweet metinlerini toplama
    tweet_elements = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")  # Tweet metinlerini içeren öğeler
    for element in tweet_elements:
        tweet_text = element.text.strip()
        if tweet_text not in tweets:  # Aynı tweet'i tekrar eklememek için kontrol
            tweets.append(tweet_text)

    # Sayfanın sonuna kaydır
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Yeni sayfa yüksekliğini kontrol et
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # Eğer sayfa değişmiyorsa kaydırmayı durdur
        break
    last_height = new_height

# Tweetleri dosyaya kaydetme
with open("tweets.txt", "w", encoding="utf-8") as file:
    for tweet in tweets:
        file.write(tweet + "\n")

print(f"{len(tweets)} adet tweet dosyaya kaydedildi.")

# Tarayıcıyı kapat
time.sleep(2)
driver.close()
