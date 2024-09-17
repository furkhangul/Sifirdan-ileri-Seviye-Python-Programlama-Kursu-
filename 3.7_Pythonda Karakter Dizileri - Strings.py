#Bu derste string üzerine çalıştım


Name = "Furkan" 
Surname = "Gül"
Age = 20

reading = "My name is " + Name + " " + Surname + " " + ". And I'm " + Age + " " + "years old."

print(reading)

print(reading[2])
"""
Burada yapmak istediğim oluşan yeni cümledeki 2.karakterin ne olduğunu belirlemekti. 
Bu sayede istediğim keliemyi cümleden çekebilme yeteneğine sahip olyorum.
"""
print(reading[7])

print(len(reading))
"""
Bu ifade ise bana okunacak cümlenin kaç karakterden oluştuğunu gösteren kod parçacığıdır.
"""

lenght = len(reading)
print("Karakter sayısı : ", lenght)

print(reading[3:])
"""
Bu ifade ise bize 3. karakterden sonra gelen bütün karakterleri yazdırmamızı sağlar.
"""

print(rading[3,15])

""" 
3'ten 15e kadar bütün karakterleri yazdırır
"""

print(reading[1:15:2])
"""
Bu ifadede ise 1 den 15'e kadar ikişer ikişer giderek karakterlerin yazmasını sağlayan kod parçacığıdır.
"""
