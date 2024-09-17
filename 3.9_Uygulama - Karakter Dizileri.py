"""
Bu ders string üzerinden uygulamalar yaptım.
Öncelikle elimde iki değişken olsun 
"""
website = "https://www.furoftheweak.com"
course =  "Sıfırdan ileri düzey python programlama ve makine öğrenmesinin aşamarlı"

#-------------------------------------------------------------------
#  1- 'Course' karakter dizisinde kaç karkater bulunmaktadır ?
#  2- 'Website' karakter dizisindeki www karakterlerini alın.
#  3- 'Website' içerisinde .com karakterlerini alın.
#  4- 'Course' içindeki ilk 15 ve son 15 karakterleri alın.
#  5- 'Course' ifadesindeki karakterleri tersten yazdır 
#-------------------------------------------------------------------

"""
1.örenği çözecek olursam
"""
lenght = len(course)
print("Course dizisinde {0} karakter bulunmaktadır" .form(lenght))


"""
2.örneği çözecek olursam
"""

print(website[8:11])

"""
3.örneği çözecek olursam
"""
print(website[23:26])

"""
4.örneği çözecek olursam
"""
print(course[:15])
print(course[40:])

"""
5.örneği çözecek olursam
"""

print(course[::-1])


#-------------------------------------------------------------------
# 6- Aşağıdaki değerleri .forum ile yazın
#-------------------------------------------------------------------
name,surname,age,job = "furkan","gül",20,"software engeener"

print("My name is {0} {1}. I'm {2} years old and i'm a {3}.")

#-------------------------------------------------------------------
# 7- Hello World ifadesindeki W ifadesini w ile değiştir.
#-------------------------------------------------------------------

word = "Hello World !"

word[7] = "w"

print(word)

#-------------------------------------------------------------------
# 8- abc ifadesini yanyana 3 defa yazdırın
#-------------------------------------------------------------------

word = "abc" * 3
print(word)






