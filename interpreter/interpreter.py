x = input("Expression: ").split(" ")
a = float(x[0])
b = float(x[2])
d = (x[1])

if d == "+":
    print(a + b)
elif d == "-":
    print(a - b)
elif d == "*":
    print(a * b)
elif d == "/":
    print(a / b)
else:
    pass
