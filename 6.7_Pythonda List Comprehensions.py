"""
bu derste ise for ve while döngülerine alternatif olarak üretilmiş
diğer döngüleri ele alacağız.
"""
number = []
for x in range(10):
    number.append(x)
    print(x)

""""
fakat bunu daha kolay bir şekilde yapabilmek için:
"""

numbers = [x for x in range(10)]
print(numbers)
"""
şeklinde yazdığımız zaman number adında bize liste oluşturuyor.
Bu benim için çok önemli bu kod ilerde çok iş görür.
"""

"""
örnek yapapcak olursam:
"""

numbers1 = [x*2 for x in range(10)]
print(numbers1)

numbers2 = [x**x for x in range(10)]
print(numbers2)

"""
string ifadeler için ise
"""

myString = "Hello"
myList = []
for letter in myString:
     myList.append(letter)
print(myList)

"""
string ifadeler için de kullanılabilir kod parçacığıdır.
"""

myList2 = [letter for letter in myString]
print(myList2)


"""
diğer örneklere bakcak olursak
"""
years = [1993,1995,2000,2002,2005]
ages = [2024-year for year in years]
print(ages)

"""
veuya
"""

result2 =[x if (x%2==0)  else print("Wrong") for x in range(1,10)]
print(result2)

sonuclar = []
for x in range(3):
    for y in range(3):
        sonuclar.append((x,y))
print(sonuclar)
