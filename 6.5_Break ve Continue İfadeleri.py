"""
Bu derste break ve continue kod bloklarını kullanacağız.
"""
name = "Furkan Gül"

for letter in name:
    if letter == "a":
        continue
    print(letter)


"""
while üzerinde çalışacak olursak
"""
x = 0
while x<5:
    x += 1
    if x == 2:
        break
    print(x)

"""
şekildeki gibi 2 ye geldiği anda döngüden çıkar.
"""

"""
1 den 100 tüm tek sayılarının toplamını yaptığımız bir kod yazacak olursak
"""
x = 1

result = 0
while x <= 100:
    if (x%2 == 1):
        result = x + result
    x = x+1


print(f"1 den 100'e kadar tek sayıların toplamı :{result}")
