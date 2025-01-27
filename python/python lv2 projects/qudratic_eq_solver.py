import math

class Quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b 
        self.c = c

    def solve_eq(self):
        D = (self.b * self.b) - 4 * self.a * self.c
        if D > 0:
            X_1 = ((-self.b) + sqrt(D))/ 2 * self.a
            X_2 = ((-self.b) - sqrt(D))/ 2 * self.a
        elif D < 0 :
            X_1 = f"{(-self.b)/ (2 * self.a)} + {sqrt(-D)/ 2 * self.a} i"
            X_2 = f"{(-self.b)/ (2 * self.a)} - {sqrt(-D)/ 2 * self.a} i"    
        else:
            X_1 = (-self.b)/ 2 * self.a 
        
        if D > 0:
            print(f"your equation has 2 real roots they are \n{X_1}\n{X_2}")
        elif D < 0:
            print(f"your equation has 2 complex roots they are\n{X_1}\n{X_2}") 
        else:
            print(f"u equation only has one root :( \n{X_1}")      

def sqrt(x):
    if x>0:
      return math.sqrt(x) 
    else:
        return{math.sqrt(-x)}


def get_inputs():
    print("-------------------ax^2+bx+c-------------------")   
    A = float(input("a: "))
    B = float(input("b: "))
    C = float(input("C: "))
    return A,B,C

A,B,C = get_inputs()

equation = Quadratic(A,B,C)

equation.solve_eq()


    











