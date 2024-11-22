def usalma(number):
    #two = usalma(2)
    #three = uslama(3)

    def inner(power):
        return number ** power

    return inner

two = usalma(2)
print(two(3))
#three = usalma(3)


"""
Yeni bi örnek yapacak olursak 
"""


def yetki_sorgulama(page):
    def inner(role):
        if role == "Administrator":
            return "{0}rolü {1} sayfasına ulaşılabilir.",format(role,page)
        else:
            return "{0}rolü {1} sayfasına ulaşılabilir.",format(role,page)

user1 =  yetki_sorgulama("Product Edit")
print(user1("Administrator"))
print(user1("User"))


"""
İşlemlere devam edecek olursak
"""

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
            return carpim

    if islem_adi == "toplam":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print(toplama(1,2,3,4,5,7))

carpma = islem("carpma")
print(carpma(5,9,9))

