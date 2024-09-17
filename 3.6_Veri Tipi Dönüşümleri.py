'''
Bu derste örnek yaptım. İşte örnekşeler:

Daire : pi * r * r
Daire Çevresi : pi * r * 2

*Yarıçapı verilen dairenin alanını ve çevresini bulunuz: 
'''


yaricap = input("Yarı çap: ")
yaricap = float(yaricap)
pi = 3.14
alan = pi * (yaricap ** 2)
cevre = pi * yaricap * 2

print("Dairenin Alanı:",alan)
print("Dairenin Çevresi:",cevre)
