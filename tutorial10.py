import hashlib

password = input("Enter Password: ")

hashed = hashlib.sha256(
    password.encode()
).hexdigest()

print("Your password Hash is:")
print(hashed)
