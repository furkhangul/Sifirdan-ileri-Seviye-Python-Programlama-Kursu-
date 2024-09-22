"""
Bu derste python üzerinden döngüleri çalıştım
"""

numbers = [1,2,3,4,5]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

"""
Döngüler olmasa bu şekilde hepsini sıra ile çağırmak zorunda kalacağım
fakat döngüler sayesinde sadece ufak bir kod ile bu işlemi tekrarlayabilirim.
"""

for x in numbers:
    print(x)
"""
birkaç örnek daha yapacak olursam:
"""

for a in numbers:
    print("Hello")

names = ["Furkan" ,"Gül","Erik","Philips","Ronney"]

for name in names:
    print(name)

"""
veya 
"""

for x in names:
    print(f"{x} is my favorite name.")


myname = "Furkan"

for n in myname:
    print(n)

"""
Biraz daha örnek oluşuracak olursam.
"""

tuple1 = 1,2,3,4,5
for t in tuple1:
    print(t)

tuple2 = [(1,2),(1,30),(3,5),(5,7)]
for a,b in tuple2:
    print(a,b)


users = {
    "k1":1,
    "k2":2,
    "k3":3,
    "k4":4
}

for key,value in users:
    print(key,value)
