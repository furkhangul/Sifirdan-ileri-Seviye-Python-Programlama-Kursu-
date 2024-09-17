#----------------------------------------------------------------------------------------------
#1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz. 
#
# müşteri adı
# müşteri soyadı
# müşteri ad + soyad
# müşteri cinsiyet
# müşteri tc kimlik 
# müşteri doğum yılı
# müşteri adres bilgisi
# müşteri yaşı 
#----------------------------------------------------------------------------------------------


CustomerName = "Furkan"
CustomerSurname = "Gül"
Customer = CustomerName + " " + CustomerSurname
CustomerGender = true #Eğer erkekse doğru yanlış ise kadın 
CustomerIdNumber = 43843220278
CustomerBirthdayYearDate = 2004
CustomerAdress = "Yeni Mahalle Yeni Caddesi Yeni Apartmanı Kat 7 No 27"
CustomerAge = 20

#----------------------------------------------------------------------------------------------
#2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız 
# Sipariş 1 => 100 TL
# Sipariş 2 => 1100.5 TL
# Sipariş 3 => 356.95 TL
#----------------------------------------------------------------------------------------------

print(110+1100.5+356.95)

#veya 

Order1 = 100
Order2 = 1100.5
Order3 = 356.95

total = Order1 + Order2 + Order3

print(total)
