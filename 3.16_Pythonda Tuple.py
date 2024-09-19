list = [1,2,3]
tuple =1 , 2 , 3 , 5
"""
Tuple de list gibi listelemeyi sağlıyor
"""
print(tuple)
print(list)
"""
fakat listede mesela list[0]= "ayşe" yazarsak 1. eleman ayşe olurken tuplede
böyle bi durum söz konusu değildir."""

"""
ayşeden kaç tane var diye bakalım
"""
print(tuple.count("ayşe"))

"""
2 sayısının indexine bakacak olursak
"""

indexi = tuple.index(2)
print(indexi)
