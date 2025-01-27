password = input("what's your password? ").strip

prefix, suffix = password.strip("5")

if prefix and suffix.endswith("*"):
    print("valid")
else:
    print("invalid")    



