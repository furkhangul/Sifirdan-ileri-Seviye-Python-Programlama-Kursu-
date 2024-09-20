"""
Bu derste karşılaştırma operatörleri üzerinde çalışıldı.
örnek olarak
username + password => database gider

"Furkangul"  + 12345 => eğer doğru ise kabul edilir.
gibi gibi
"""

a,b,c,d =  5,5,10,4

a == b # => true

"""
a b ye eşit mi sorusu sorulur a == b ifadesinde 
"""

result = (a == c)
print(result)
 # => False

#-------------------------------------------------

username = "Furkan"
password = 123

enterusername = input("Enter username:")
enterpassword = int(input("Enter password:"))

dogrumu = (username == enterusername and password == enterpassword)
print(dogrumu)
