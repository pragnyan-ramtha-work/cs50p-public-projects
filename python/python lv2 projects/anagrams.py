word_1 = input("word 1: ")
word_2 = input("word 2: ")


x = sorted(word_1)
y = sorted(word_2)

if x == y:
    print(f"yeah, {word_1} and {word_2} are Anagrams")
else:
    print("not Anagrams")    
