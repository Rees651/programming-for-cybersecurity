def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = float(input("First Number is: "))
num2 = float(input("Second Number is: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose: ")

if choice == "1":
    print(add(num1, num2))
elif choice == "2":
    print(subtract(num1, num2))
elif choice == "3":
    print(multiply(num1, num2))
elif choice == "4":
    print(divide(num1, num2))
