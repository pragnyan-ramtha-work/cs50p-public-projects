name = input("gimme name ")

file = open("name.txt","a")
#"w " writes and erases the prev doc ,"a" appends i.e adds to existing
file.write (f"{name}\n")
file.close()

# these 3 lines are opening a doc and writing  the doc and saveing'