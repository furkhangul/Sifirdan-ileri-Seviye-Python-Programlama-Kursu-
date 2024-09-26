"""
Bu aşamaya kadar normal fonksiyon türlerini öğrendim bu derste ise
lambda expression filtreleme tekniklerini öğrendim.
"""
from turtledemo.sorting_animate import start_qsort


def square(num): return num ** 2
numbers = [1,3,5,7,9]
result =square(2)
print(result)
"""
veya numbers listesini çalıştırmak istersek:
"""

result2 = list(map(square , numbers))
print(result2)

"""
-----------------------------------------
"""
for item in map(square,numbers):
    print(item)

"""
veya 
"""

result3 = list(map(lambda num: num ** 2, numbers))
result4=  list(map(square,numbers))
result5 = square(3)


def check_even(num):return num%2==0

result = list(filter(lambda num : num%2 , numbers))

print(result)

