import random

print(dir(random))
print(help(random))

result = random.random()
print(result)

result = random.uniform(1,15)
print(result)
"""
uniform ile 1 ile 15 arasında bir sayı verir
"""
result = int(random.uniform(1,150))
print(result)

"""
Şeklinde tam sayıya çevirebiliriz
"""

names = ["Furkan","Kerem","İlyas","Volkan","Canberk","Ramiz","Ömer"]

result = names[random.randint(0,len(names)-1)]
print(result)
"""
Burada ise names listesinden herhangi bir isim çekilmesi isteniyor
"""

result = random.choices(names)
print(result)
"""
Burada ise rastgele bir elemanı bize verir 
daha basittir.
"""

newlist = list(range(15))
random.shuffle(newlist)
result = newlist
print(result)
"""
burada ise rastgele listeyi karıştırıyor
"""

result = random.sample(names,30)
print(result)
"""
burada ise 3 tane eleman çekmesini istiyoruz.
"""

