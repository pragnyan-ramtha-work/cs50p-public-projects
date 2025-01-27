
units = input("mention the units ur temperature is in (F or C or K) :  ")
temp = int(input("whats the tempreture?: "))

# F = 9/5 C + 32
# K = C + 273

def cel():
    C = c = temp
    F = (9/5) * C + 32
    K = C  + 273
    print(f"{C} celsius is {F} farenheit,{K}kelvin")

def far():
    F = f = temp
    C = (F  - 32)*(5/9)
    K = (F  - 32)*(5/9) + 273
    print(f"{F} farenheit is {C} celsius,{K}kelvin")    

def kel():
    K = k = temp
    F = (9/5) * (k - 273) + 32
    C = k - 273
    print(f"{K} kelvin is {F} farenheit,{C}celsius")


def iden_run():
    if units == "k" or units == "K":
        kel()
    elif units == "C" or units == "c":
        cel()
    elif units == "F" or units == "f":
        far()
    else:
        print(f"{units} is not a recognized temperature scale plz try again")  
        while True:
         iden_run()    
    
iden_run()