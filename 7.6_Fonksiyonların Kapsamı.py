"""
Bu derste tanımlanan değişkenlerin lokal veya global olup olmadığı üzerine
örnekler ve tanımlamalar yapıldı.
"""

"""
elimizde bir değişken olsun
"""
x = "Global x"

def function():
    x = "Local x"

function()
print(x) #cevap => "global x"
"""
örnekte olduğu gibi fonkisyon dışında kalan x değişkeni ile fonksiyon
içinde kalan x değişkeninden etkilenmiyor.
yani fonksiyon dışındaki değişken global iken fonksiyon içindeki x değişkeni
ise local şekilde kalır.
 biz de x değişkenini çağırdığımızda ise global olan x değeri çağrılır.
 """

name = "Furkan"
def changeName(new_name):
    name = new_name
    print(name)

changeName("Fahrettin")

"""
Bu durumda ise fonksiyon içindeki değeri çağırdığımız için artık local 
değer içinde kalan değeri gösterir.
"""
name1 = "Global String"

def greeting():
    name = "Çınar"

    def hello():
        name = "Furkan"
        print("Hello " + name)
    hello()
greeting()
"""
Burada da artık localin locali şeklinde ifade edebileceğimiz bir 
örnek gösterildi iç içe fonksiyonlara da bir örnek olabilir.
"""

x = 50
def test(x):
    print(f"x = {x}")

    x = 100
    print (f"change x to {x}")

test(5)
