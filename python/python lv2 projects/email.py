mail = input("whats ur email bruh: ")
if "@" in mail and mail.count("@") == 1:
     name,domain = mail.split("@")
else:
     print("invalid")


print(f"{name} ur domain is {domain}")