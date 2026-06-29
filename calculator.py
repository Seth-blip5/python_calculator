# Simple calculator program
while True:
    num1 = float(input("Enter first number: "))
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")         
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    options = int(input("Enter your preferred operation(1/2/3/4/5/6): "))
    num2 = float(input("Enter second number: "))
    if options == 1:
        print(num1 + num2)
    elif options == 2:
        print(num1 - num2)
    elif options == 3:
        print(num1 * num2)
    elif options == 4:
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error")
    elif options == 5:
        print(num1 % num2)
    elif options == 6:
        print(num1 ** num2)
    else:
        print("Invalid input")
    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again != "yes":
        break
print("Thank you for using the calculator!")
