def main():
    name,height,age = getinfo()
    if name == "bhanu":
        height = "0" 
    print(f"{name} is {height} cm long and {age} years old  ")

def getinfo():
    x = input("whats your name? ")
    y = int(input("whats your height? "))   
    z = int(input("how old are you? "))
    return x,y,z

if __name__ == "__main__":
    main()