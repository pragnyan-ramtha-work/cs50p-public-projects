print("welcome to pikki's calculator")
print("")
print("press one(1) for addition\n\npress two(2) for subtraction\n\npress three(3) for multiplication\n\npress four(4) for division")
print("")

def main():
    if x == 1:
        print(a + b) 
    elif x == 2:
        print(a - b)
    elif x == 3:
        print(a * b)
    elif x == 4:
        print(a / b)
    
def identify_func_and_input():
     x = int(input("what mathematical operation do want to do today? "))
     if x == 1:
        y = "added to"
     elif x == 2:
        y = "subtracted by"
     elif x == 3:
        y = "multiplied with"
     elif x == 4:
        y = "divided by"
     print("")
     a = int(input("what the first number? "))
     b = int(input(f"is,{y}"))
     return x,a,b

x,a,b = identify_func_and_input()
main()




