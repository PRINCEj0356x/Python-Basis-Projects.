def calculator(num1,operator,num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return(F"Oops, Error!! num1 and num2 should be float ")
    if operator == "+" :
        return (num1 + num2)
    elif operator == "-":
        return (num1 - num2)
    elif operator == "*":
        return (num1 * num2)
    elif operator == "/":
        if num2 == 0:
            return("So!, given operation not done by even an IIIT students")
        else:
            return (num1 / num2)
    else:
# Handle cases where the operator is not recognized.
        return "Error: Invalid operator. Please use +, -, *, or /."

inputs = (input("Enter numbers and operator for proceed:").split())
print(inputs)
if len(inputs)==3:
    result = calculator(inputs[0],inputs[1],inputs[2])
    print(f"Evaluated Answer = {result}")
else:
    print("Please!, enter omly two name and one operator")