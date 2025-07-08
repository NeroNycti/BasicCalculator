def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if x == 0 or y == 0:
        print("You cannot divide by zero")
    else:
        return x / y

while True:

    choice = input(f"""1- Add
2- Subtract
3- Multiply
4- Divide
    Select an operation between 1-4: """)
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2) )
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "x", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        while True:
            next_calculation = input("Do you want to continue calculating? (yes/no): ").lower()
            if next_calculation == "yes":
                break
            elif next_calculation == "no":
                exit()
            else:
                print("Invalid Input")
