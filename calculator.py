print("Hello , World")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

print("=================================")
print("      MY SIMPLE CALCULATOR")
print("=================================\n")

options = {
    1: "Add",
    2: "Subtract",
    3: "Multiply",
    4: "Divide",
    5: "Quit"
}

while True:

    print("\nChoose an Operation:")

    for key, value in options.items():
        print(f"{key}. {value}")

    choice = int(input("\nEnter your choice (1, 2, 3, 4, 5): "))

    if choice not in options:
        print("Invalid choice... Please re-enter!")
        continue

    if choice == 5:
        print("\nThank you for using My Simple Calculator!")
        print("Have a nice day!")
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
  
    if choice == 1:
        print(f"\n{num1} + {num2} = {add(num1, num2)}")

    elif choice == 2:
        print(f"\n{num1} - {num2} = {sub(num1, num2)}")

    elif choice == 3:
        print(f"\n{num1} * {num2} = {mult(num1, num2)}")

    elif choice == 4:
        print(f"\n{num1} / {num2} = {div(num1, num2)}")
