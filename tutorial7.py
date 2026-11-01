try:
    num1 = float(input("Number 1 is: "))
    num2 = float(input("Number 2 is: "))

    result = num1 / num2

    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Numbers only")
