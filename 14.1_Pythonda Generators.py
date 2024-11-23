"""
Bu bölümde ise Generatörler ile alakalı örnekler üzerinde duracağız.
"""

def cube():
    result = []

    for i in range(5):
        result.append(i ** 3)

    return result
print(cube())

"""
Böyle bir fonksiyon ile küpünü alınan sayıların listelenmesi konusu gayet basit
durmakta fakat eğer bellekte tutulacak sayı 5 değil de 5000 civarı gibi büyük
sayılar ise işte o zaman işler değişmektedir.

bunun için generatorları kullanmaktayız bu sayede bellekte fazladan yer işgalinin
önüne geçmiş bulunuyoruz.
"""


def cube2():
    for i in range(10):
        yield i **3

generator = cube()
iterator = iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))



"""
şekinde yazıldığı zaman yiled methodu bize çıktıyı direkt verdikten sonra silme
işlemini görmektedir. Bu sayede bellek güvenliğini sağlamış oluyoruz.
"""
