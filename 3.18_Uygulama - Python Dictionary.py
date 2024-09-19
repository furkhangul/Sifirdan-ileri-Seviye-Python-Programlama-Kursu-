# Öğrenci bilgilerini tutan sözlük
SchoolNumber = {
    "123": {
        "Name": "Furkan",
        "Surname": "Gül",
        "Age": 20,
        "Class": 2,
        "Department": "Software Engineer",
        "Email": "gl56frkn@gmail.com",
        "Phone": "05418640498"
    },
    "124": {
        "Name": "Sadık",
        "Surname": "Torlu",
        "Age": 21,
        "Class": 2,
        "Department": "Software Engineer",
        "Email": "sadik@gmail.com",
        "Phone": "05418648"
    },
    "125": {
        "Name": "Recep",
        "Surname": "İnan",
        "Age": 22,
        "Class": 2,
        "Department": "Software Engineer",
        "Email": "recepinan@gmail.com",
        "Phone": "05458656048"
    }
}

# Kullanıcıdan öğrenci numarasını alma
school_number = input("Please enter school number: ")
if school_number in SchoolNumber:
    print(SchoolNumber[school_number])
else:
    print("Student not found.")

# Yeni öğrenci eklemek için
Student = {}
number = input("Student number: ")
name = input("Student name: ")
surname = input("Student surname: ")
age = input("Student age: ")
class_number = input("Student class: ")
department = input("Student department: ")
email = input("Student email: ")
phone = input("Student phone: ")

# Yeni öğrenci bilgilerini sözlüğe ekleme
Student[number] = {
    "Name": name,
    "Surname": surname,
    "Age": age,
    "Class": class_number,
    "Department": department,
    "Email": email,
    "Phone": phone
}

# Öğrenciyi ekledikten sonra yeni öğrenci bilgilerini göster
print("New student added:")
print(Student[number])
