import re

users = {}

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        email = input("Enter email: ").strip().lower()

        if not re.fullmatch(pattern, email):
            print("Invalid email format ")
            continue

        if email in users:
            print("User already exists ")
            continue

        password = input("Enter password: ").strip()
        
        length_check = len(password) >= 8
        digit_check = re.search(r"\d", password)
        upper_check = re.search(r"[A-Z]", password)
        lower_check = re.search(r"[a-z]", password)
        symbol_check = re.search(r"[@#$%&*!-]", password)


        if all([length_check, digit_check, upper_check, lower_check, symbol_check]):
            print("\nRegistration successful ")
            users[email] = password
        else:
            print("\nWeak password Try again")
            continue
        
    elif choice == "2":
        email = input("Enter email: ").strip().lower()
        password = input("Enter password: ").strip()

        if email in users and users[email] == password:
            print("Login successful ")
        else:
            print("Invalid email or password ")

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid choice ")
