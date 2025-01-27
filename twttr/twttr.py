x = input("Input:")
y = list(x)

u = 0


while u<5:
    if "a" in y:
        y.remove("a")
    elif "e" in y:
        y.remove("e")
    elif "i" in y:
        y.remove("i")
    elif "o" in y:
        y.remove("o")
    elif "u" in y:
        y.remove("u")
    else:
        u = u +1




for i in range(0,len(y)-1):
    print(y[i], end="")

print()
