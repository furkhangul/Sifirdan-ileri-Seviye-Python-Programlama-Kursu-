"""
Bu dersimizde iterator üzerinde duracağız.
örneğin bir liste oluştururken listedeki elemanlarında gezinmek buna bir örnektri.
"""
from operator import truediv
from string import Formatter

liste = [1,2,3,4,5]
for i in liste:
    print(i)

print(dir(liste))


"""
Veri yapıları dersinde gördüğümüz root ve iter terimleri ile aynı mantığa
gelmektedir. Aynı şeiklde bir değer taşınarak bu değer üzerinden işlem yapılır.
"""
iterator = iter(liste)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

"""
Bu ifadeyi daha basitleştirmiş bi hale getirecek olursak 
"""

while True:
    try:
        element  = next(iterator)
        print(element)

    except Exception:
        print("We founded a error !")
        break
    except StopIteration:
        break

"""
bunun için farklı bir örnek yapacak olursam :
"""

class MyNumbers:
    def __init(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self


    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


list = MyNumbers(10,50)
myiter = iter(list)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))




