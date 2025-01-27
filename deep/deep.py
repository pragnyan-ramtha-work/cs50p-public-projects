def main():
    x = input("What is the Answer to the great Question of Life, the Universe and Everything? ").lower().replace(" ","")
    if x =="42"or x =="forty-two" or x == "fortytwo":
        print("Yes")
    else:
        print("No")

main()
