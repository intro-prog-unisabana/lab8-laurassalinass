import sys
if len(sys.argv) != 4:
    print("Invalid usage:")
    print("python3 calculator.py <numero> <operador> <numero2>")
    sys.exit()

numero = sys.argv[1]
operador = sys.argv[2]
numero2 = sys.argv[3]

try:
    num1 = float(numero)
    num2 = float(numero2)
except ValueError:
    print("Error:Invalid number!")
    sys.exit()
 
if operador == "+":
    result = num1 + num2
elif operador == "-":
    result = num1 - num2
elif operador == "x":
    result = num1 * num2
elif operador == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        sys.exit()
    result = num1 / num2
else:
    print("Error: Invalid operator. Use +, -, x, or /.")
    sys.exit()

print("Result:", result)