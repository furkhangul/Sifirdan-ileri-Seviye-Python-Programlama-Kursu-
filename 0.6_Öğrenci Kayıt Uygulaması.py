import os
import csv


def ortalama_oku():
    if not os.path.exists("Liste.txt"):
        print("Liste.txt dosyası bulunamadı.")
        return

    with open("Liste.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())


def not_gir():
    studentName = input("Öğrenci adı: ")
    studentSurname = input("Öğrenci soyadı: ")
    studentNumber = input("Öğrenci okul numarası: ")

    while True:
        try:
            not1 = int(input("Birinci sınav notu: "))
            not2 = int(input("İkinci sınav notu: "))
            sozlu = int(input("Sözlü notu: "))
            break  # Geçerli notlar alındıysa döngüden çık

        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    ortalama = (not1 + not2 + sozlu) / 3

    with open("Liste.txt", "a", encoding="utf-8") as file:  # Append mode
        file.write(f"Öğrenci adı: {studentName}\n")
        file.write(f"Öğrenci soyadı: {studentSurname}\n")
        file.write(f"Öğrenci okul numarası: {studentNumber}\n")
        file.write(f"Birinci sınav notu: {not1}\n")
        file.write(f"İkinci sınav notu: {not2}\n")
        file.write(f"Sözlü notu: {sozlu}\n")
        file.write(f"Öğrenci ortalaması: {ortalama:.2f}\n")
        file.write("---------------------------------\n")

    print("Notlar başarıyla kaydedildi!")


def not_kayit():
    if not os.path.exists("Liste.txt"):
        print("Liste.txt dosyası bulunamadı, not kaydedilemiyor.")
        return

    with open("Liste.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open("Notlar.csv", "w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
            ["Öğrenci Adı", "Öğrenci Soyadı", "Okul Numarası", "Birinci Sınav Notu", "İkinci Sınav Notu", "Sözlü Notu",
             "Ortalama"])

        for i in range(0, len(lines), 7):  # 7 satırda bir yeni öğrenci kaydı
            try:
                studentName = lines[i].split(": ")[1].strip()
                studentSurname = lines[i + 1].split(": ")[1].strip()
                studentNumber = lines[i + 2].split(": ")[1].strip()
                not1 = int(lines[i + 3].split(": ")[1].strip())
                not2 = int(lines[i + 4].split(": ")[1].strip())
                sozlu = int(lines[i + 5].split(": ")[1].strip())
                ortalama = float(lines[i + 6].split(": ")[1].strip())

                csv_writer.writerow([studentName, studentSurname, studentNumber, not1, not2, sozlu, ortalama])

            except IndexError:
                continue  # Eğer satır eksikse devam et

    print("Notlar başarıyla Notlar.csv dosyasına kaydedildi!")


while True:
    print("\n1- Notları Oku")
    print("2- Not Gir")
    print("3- Notları Kayıt Et")
    print("4- Çıkış")

    while True:
        try:
            islem = int(input("Mod Seç: "))
            if islem in [1, 2, 3, 4]:
                break
            else:
                print("Lütfen 1-4 arasında bir seçim yapın.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    if islem == 1:
        ortalama_oku()
    elif islem == 2:
        not_gir()
    elif islem == 3:
        not_kayit()
    elif islem == 4:
        print("Programdan çıkılıyor...")
        break
