attempts = 0

while attempts < 3:
    password = input("Enter password!: ")

    if password == "Cyber":
        print("Access Granted")
        break

    attempts += 1
    print("Incorrect Password")

if attempts == 3:
    print("Account Locked")
