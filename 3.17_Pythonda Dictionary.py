"""
bu derste pythonda bulunan dictionary listeleme methodunu öğrneceğiz
"""

"""
dictionary listeleme biçimi key - vaue şeklinde çalışır .
örnek olarak plaka şehir özdeşleştirilmesini gösterebiliriz.
56 => Siirt 34 => İstanbul 21 => Diyarbakır
"""

sehir = ["Mersin","İstanbul"]
plaka = [41,34]

"""
şeklinde yazdığımızda eşleştirmek için
"""
print(plaka[sehir.index("Mersin")])
"""
veya 
"""
plakalar = {"Mersin":41,"İstanbul":34,"Siirt":56}

print(plakalar["Siirt"])
"""
eklemek için ise
"""
plakalar["Ankara"] = 6
print(plakalar)
"""
User için denersek 
"""
users = {
    "furkangul" : 20,
    "keremaktürkoğlu":27,
    "serdardursun":23
}
"""
veya furkangul girildiği zaman daha fazla bilgi almak için
"""
users1 = {
    "furkangul":{
        "age": 20,
        "email":"gl56frkn@gmail.com",
        "phone": 54186,
        "roles": ["admin","user"]

    },
    "sadikturan": {
        "age": 25,
        "email": "sadikn@gmail.com",
        "phone": 123456,
        "roles": [ "user"]

    }
}
print(users1["furkangul"])

"""
Şeklinde örnek bi web site apisi kurabiliriz.
"""
