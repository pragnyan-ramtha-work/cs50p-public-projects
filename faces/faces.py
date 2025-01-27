def main():
    x = input()
    y = convert(x)
    print(y)

def convert(x):
    e = x.replace(":)","🙂")
    k = e.replace(":(","🙁")
    return k


main()
