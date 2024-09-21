"""
Bu derste if else elif blokları ile bize verilmiş örnekleri çözdüm.
"""

#---------------------------------------
# 1- kullanıcıdan isim, yaş ve eğitim bilgilerini alıp ehliyet alabilme
# durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
# lise ya da üniversite olmalıdır
#---------------------------------------

username = input("Username:")
userlastname = input("Last name:")
userage = int(input("User age:"))
usereducation = input("User education:")
user = {}
user[username] ={
    "Username":username,
    "User Surname":userlastname,
    "User Age": userage,
    "User Education" : usereducation
}
entername = input("Enter a username for search: ")
if user[entername]["User Age"] >= 18 and user[entername]["User Education"] in ["High School", "University"]:
    print(f"{entername} can take a driving license.")
else:
    print(f"{entername} cannot take a driving license.")
