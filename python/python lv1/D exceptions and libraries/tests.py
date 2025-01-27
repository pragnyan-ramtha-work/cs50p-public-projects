def main():
    x = int(input("gimme x and i'll square it"))
    print("x squared is",square(x))

def square(n):
    return n*n

#sys commands are used to directly attach the values with  the file name 
if __name__ == "__main__":
    main()