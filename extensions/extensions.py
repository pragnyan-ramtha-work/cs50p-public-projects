x = input("File name: ").lower().replace(" ","")
y = x.split(".")
if "gif" in y or "png" in y:
    print("image/"+y[-1])
elif "jpeg" in y or "jpg" in y:
    print("image/jpeg")
elif "pdf" in y:
    print("application/"+y[-1])
elif "txt" in y:
    print("text/plain")
elif "zip" in y:
    print("application/"+y[-1])
else:
    print("application/octet-stream")
