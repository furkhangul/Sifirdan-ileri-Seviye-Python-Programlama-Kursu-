with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)

"""
Şeklinde yazılan kodda liste bittikten sonra kendi kendine kapanmaktadır.
Bu şekilde close operatörünü kullanmaya ihtiyaç duymayız. 
"""
with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(file.tell())
    content2 = file.read()
    print(content2)
"""
Şeklinde tell methodunu kullandığımızda ise tell methodu bize 
doysa içerisindeki karakter sayısını bize derleyip söymektedir.
"""

with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    file.seek(7)
    print(file.tell())
    content2 = file.read()
    print(content2)
    
"""
Burada ise gördüğümüz gibi seek methodu ile ilk 7 basamağı atlayarak bize
yeni bir dosya vermektedir
"""
