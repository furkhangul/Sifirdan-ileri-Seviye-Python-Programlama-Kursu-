"""
Bu derste koşullu ifadeler bloklarını çalıştım.
kısacası if ve else üzerine çalıştık ;)
"""

if 3==2:
    print('hos geldiniz')
else:
    print("pek hoş gelmediniz")

isLoggedn = True

if isLoggedn == True:
    print("Hos geldiniz")

username = input("Username:")
password = int(input("Password:"))

if (username=="Furkan") and (password == 123456):
    print("Succses Login")
else:
    print("Wrong !")


#-------------------------------------------------
username1 = input("Username:")
password1 = int(input("Password:"))

if (username1=="Furkan"):
  if(password1 == 123456):
      print("Succses Login")
  else:
      print("Wrong Password")
else:
    print("Wrong  Username!")
