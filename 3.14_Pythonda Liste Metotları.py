"""
Öncelikle iki tane liste halinde değişken oluşturalım.
"""

numbers = [1,2,5,10,20,25,8,12,3,7,9]
letters = ["a","g","s","b","g","h","r"]

"""
numbers değişkeni içerisindeki en düşük ve en büyük sayıyı bulmak için max 
ve min kodları kullanılır.
"""

result1 = min(numbers)
result2 = max(numbers)
print(result1)
print(result2)

"""
Aynı şeyi letters değişkeni için de yapalım.
"""
result3 = min(letters)
result4 = max(letters)
print(result3)
print(result4)

"""
Diğer string ifadeler gibi bi yerden başlayıp belli bi yere kadar da albiliriz
Örneğin:
"""
newNumbers = numbers[2:5]
print(newNumbers)

"""
Veya daha sonra sayı da değiştirebiliriz.
"""
numbers[2] = 40
print(numbers)

"""
Veya append komutu ile istediğimiz bir sayı veya değişkeni
daha sonradan listemize dahil edebiliyoruz.
"""
numbers.append(45)
print(numbers)

"""
İstediğimiz bi konuma da sayı veya değişken ekleyebiliriz. Bunun için insert 
komutu kullanılır örnek olarak numbers.insert(3,15) şeklinde yazıldığında
 3. değer artık 15 olarak eklendi ondan önce girilmiş olan değer ise 4. olarak
 bi sağa kayıdırıldı.
"""
numbers.insert(3,15)
print(numbers)

"""
Eleman silme işlemi ise pop komutu ile yapılamktadır.
"""
numbers.pop(0)
print(numbers)

"""
Remove methodu ile ise direkt olarak girdiğimiz sayı silinir.
"""

numbers.remove(15)
print(numbers)

"""
Sıralama işlemlerine geçitğimiz zaman ise sort işlemi ile liste sıralanır.
"""
numbers.sort()
letters.sort()
print(numbers)
print(letters)

"""
Tersten yazmak istersek ise reverse methodu kullanılır.
"""
numbers.sort()
numbers.reverse()
print(numbers)

"""
Listede ifadenin ne kadar olduğunu bulmak için count methodu kullanılır.
2 sayısının kaç defa kullanılıdığını öğrenmek için:
"""
print(numbers.count(2))
