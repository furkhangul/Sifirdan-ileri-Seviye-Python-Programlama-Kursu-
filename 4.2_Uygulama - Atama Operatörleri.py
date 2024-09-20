"""
Bu bölümde ise operatörlerin uygulamalı çözümlerini yaptım.
"""
x,y,z = 2, 5, 10
#----------------------------------------------------
# 1-Kullanıcıdan aldığımız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
#----------------------------------------------------
a = input("1.sayıyı giriniz:")
b = input("2.sayıyı giriniz:")

print((int(a)*int(b))-(x+y+z))

#----------------------------------------------------
# 2- y'nin x'e kalansız bölümünü hesaplayınız.
#----------------------------------------------------
print(y//x)

#----------------------------------------------------
# 3-(x,y,z) toplamının mod 3'ü nedir?
#----------------------------------------------------
print((x+y+z)%3)

#----------------------------------------------------
# 4- y'nin x. kuvvetini hesaplayınız.
#----------------------------------------------------
print(y ** x)

#----------------------------------------------------
# 5- x, *y , z = numbers işlemine göre z'nin küpü nedir
#----------------------------------------------------
numbers = 1,5,7,10,6

x,*y,z = numbers
print(y)

#----------------------------------------------------
# 6-x,*y,z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
#----------------------------------------------------
numbers = 1,5,7,10,6
x,*y,z= numbers

result = y[0] + y[1] + y[2]
print(result)
