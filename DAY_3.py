# Simple Claculator
# Step 1: Get user input for two numbers
number1 = float(input("Enter the first number: "))
operator = (input("Enter the operator: "))
number2 = float(input("Enter the Second number: "))

# Step 2: Perform arithmetic operation
# addition = number1 + number2
# subtraction = number1 - number2
# multiplication = number1 * number2
# division = number1 / number2 if number2 != 0 else "cannot divide by zero"

#step2
if operator == "+":
    addition = number1 + number2
    print(f"Addition:{number1} + {number2} = {addition}")
elif operator == "-":
    subtraction = number1 - number2
    print(f"Subtraction:{number1} - {number2} = {subtraction}")
elif operator == "*":
    multiplication = number1 * number2  
    print(f"Multiplication:{number1} * {number2} = {multiplication}")
elif operator == "/":
    division = number1 / number2 if number2 != 0 else "cannot divide by zero"
    print(f"Division:{number1} / {number2} = {division}")
else:
    "invalid operator"


# Step 3: Display the results
print("\n--- Calculator Results ---")



