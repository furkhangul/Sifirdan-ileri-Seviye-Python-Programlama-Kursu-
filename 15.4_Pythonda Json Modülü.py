"""
Bu dersimizde Json kütüphanesi ile çalışıldı.
Python'da JSON (JavaScript Object Notation) verileriyle çalışmak için json
modülü kullanılır. Bu modül, JSON verilerini Python nesnelerine dönüştürmek
veya tam tersini yapmak için gerekli işlevleri sağlar.
"""

import json

person = {"name" : "Furkan", "Surname":"Gül","Language":["Python","C#"]}
print(person["name"])
"""
Bu örnek bir dictionary örneğidir. fakat biz bunu json ile değiştirebiliriz.
Yukarıda açıkladığımız gibi js kodlarının pythona aktarılması sırasında örnekteki
gibi bir yazı gelirse python direkt olarak bu ifadeyi dictionary olarak almaz
string olarak alır bunu için json methodunu kullanmaktayız.
"""

person_string = '{"name" : "Furkan", "Surname":"Gül","Language":["Python","C#"]}'
degis = json.loads(person_string)
print(degis["name"])
print(degis["Surname"])
print(degis["Language"])
"""
Şekilde olduğu gibi string ifadeyi dictionary şekline çevirdi.
"""

#######################################################################
person_dict =  {
    "name": "Furkan",
    "surname":"Gül",
    "language": ["C#","Python","C","C++"]
}
degistir = json.dumps(person_dict)
print(degistir)
"""
Bu ifade ile dictionary bi ifadeyi string bir ifadeye çeviriyoruz
"""
