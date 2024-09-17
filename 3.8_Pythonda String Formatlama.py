name = "Furkan"
surname = "Gül"

print('My name is {} {}' .format(name,surname))
"""
Bu format ise bi önceki derste sıra ile yazmak yerine daha pratik bi şekilde değikenleri çıktı olarak çıkarmamıza yardım ediyor 
"""
print('My name is {1} {0}' .format(name,surname))
"""
Şeklindeki örnekte ise my name is gül furkan şeklinde olur çünkü sayıya duyarıldır.
"""


result = 200/500

print("the result is {r:5.4}".format(r=result))
""" 
bu örnekte resut değerini r olarak atadım r karşısındaki 5 virgülden önce ne kadar alan bırakılması gerektiğini yazmamızı sağlıyor
fakat 4 ise virgülden sonraki 4 haneyi göstermesi gerektiğini ifade ediyor
"""
