#in case of input beyond range use try and except
while True:
    try:
        y = input("give me x ") 
        x = int(y)
        print("x is",x)
    except ValueError:
        print( y + " is not an integer lmao")    
    else:
        break
#we can use *pass* instead of line 8 to avoid scary message
