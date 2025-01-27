import re

email = input("whats ur email bro? ").strip()

if re.search(r".+@.+\.edu",email):
    print ("valid")
else:
    print("not valid")    
   
#re.search(pattern,string,flags=0)
# . any character except newline
# *  0 or more repition
# + 1 or more
# ? 0 or 1
# {m} m no. of rep
# {m,n} m-n repetion ex 3 -5 reps
