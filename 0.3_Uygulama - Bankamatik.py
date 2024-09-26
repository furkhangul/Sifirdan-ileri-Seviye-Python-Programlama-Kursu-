"""
Bu bölümde bankamaetik uygulaması yapıldı.
"""
users = {}


def modular():
    print("[0] Add User")
    print("[1] List Users")
    print("[2] Search User Information")
    print("[3] Login")
    mod = int(input("Please enter a mod: "))

    if mod == 0:
        adduser()
    elif mod == 1:
        listuser()
    elif mod == 2:
        searchuser()
    elif mod == 3:
        login()
    else:
        print("Please enter a valid mod")
        modular()


def adduser():
    username = input("Username: ")
    password = input("Password: ")
    number = input("Number: ")
    email = input("Email: ")
    balance = int(input("Balance: "))
    users[username] = {
        "Password": password,
        "Number": number,
        "Email": email,
        "Balance": balance
    }
    modular()


def listuser():
    if users:
        for username, info in users.items():
            print(f"Username: {username}, Info: {info}")
    else:
        print("No users found.")
    modular()


def searchuser():
    username = input("Enter username to search: ")
    if username in users:
        print(f"Found user: {users[username]}")
    else:
        print("User not found.")
    modular()


def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]["Password"] == password:
        print("Login successful.")
        manage_balance(username)
    else:
        print("Invalid username or password.")
        modular()


def manage_balance(username):
    while True:
        print("[0] Add Money")
        print("[1] Withdraw Money")
        print("[2] Exit")
        choice = int(input("Choose an option: "))

        if choice == 0:
            amount = float(input("Enter amount to add: "))
            users[username]["Balance"] += amount
            print(f"New balance: {users[username]['Balance']}")
        elif choice == 1:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= users[username]["Balance"]:
                users[username]["Balance"] -= amount
                print(f"New balance: {users[username]['Balance']}")
            else:
                print("Insufficient balance.")
        elif choice == 2:
            modular()
            break
        else:
            print("Invalid option.")


modular()
