from datetime import datetime

username = input("Username: ")
password = input("Password: ")

if username == "Admin" and password == "Cyber123":
    result = "SUCCESS"
else:
    result = "FAILED"

with open("log.txt", "a") as file:
    file.write(f"{datetime.now()} | {username} | {result}\n")

print("Logged.")
