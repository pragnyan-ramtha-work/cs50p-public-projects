
def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    nt = time.split(":")
    a = float(nt[0])
    b = float(nt[-1]) * 1/60
    c = a + b
    return c
    print(c)

if __name__ == "__main__":
    main()
