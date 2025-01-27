x =  int(input("how amy numbers of the sequence?; "))

fib = [0,1]

def fibb():
    for i in range(x):
        fibb[i+1] = fib[i-1] + fib[i]
    return fib[i+1]

for i in range(x):
    print(fib[0])
    print(fib[1])
    print(fibb[i])