import time
import random as ra

# Combine letters and symbols into one list
letters = list("abcdefghijklmnopqrstuvwxyz")
symbols = list("!@#$%^&*()-_+=[]{}:;<>?,.|")
all_chars = letters + symbols

# Input from user
word = input("encryption: ")
word_len = len(word)

# Initialize the decrypted word with placeholders
decrypted = ["_" for _ in range(word_len)]  # Underscores represent undeciphered characters
indices_to_decrypt = list(range(word_len))  # List of all indices yet to be decrypted

print("Decrypting...\n")

# Animation loop
while indices_to_decrypt:
    # Randomly choose an index to decrypt
    random_index = ra.choice(indices_to_decrypt)
    decrypted[random_index] = word[random_index]  # Decrypt the letter at this index
    indices_to_decrypt.remove(random_index)  # Remove the index from the undeciphered list

    # Display the current state of the decrypted word
    for i in range(word_len):
        if i in indices_to_decrypt:  # Undeciphered characters are random
            print(ra.choice(all_chars), end="")
        else:  # Decrypted characters are shown
            print(decrypted[i], end="")
    print()

    time.sleep(0.3)  # Adjust the animation speed as needed

# Final Output
print("\nDecryption Complete!")
print(f"Decrypted Word: {word}")

time.sleep(5)  # Wait 5 seconds before exiting
