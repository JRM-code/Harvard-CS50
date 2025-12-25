# --- GET EXPRESSION FROM USER AND ASSIGN TO X, Y, Z VARIABLES --- #
expression = input("Enter your expression: ")
x, y, z = expression.split(" ")

# --- CONVERT STR TO INT --- #
x = int(x)
z = int(z)

# --- USE THE VARIABLES TO EVALUATE THE EXPRESSION --- #
if y == "+":
    answer = float(x + z)
elif y == "-":
    answer = float(x - z)
elif y == "*":
    answer = float(x * z)
elif y == "/":
    answer = float(x / z)
print(answer)    
