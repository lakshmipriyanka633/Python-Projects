
# Create a function to perform the desired operation
def SimpleCalc(operator, num1, num2):
    if operator == "+":
        return round(num1 + num2)
    elif operator == "-":
        return round(num1 - num2)
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Invalid Operation!"

# Get input from the user
while True:
    operator = input("Enter an operator (+ - * / %): ").strip()
    if operator == "x":
        print("Come Again!")
        break
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

    # Print the result
    print(SimpleCalc(operator, num1, num2))

