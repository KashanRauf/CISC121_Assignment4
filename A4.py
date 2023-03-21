import re

import functions

# Gets user input
plaintext = input("Enter a string: ")
plaintext = plaintext.upper()

# Use a regex to remove non-letters, and take maximum first 10 letters
regex = re.compile('[^A-Z]')
processed_text = regex.sub("", plaintext)
if len(processed_text) > 10:
    processed_text = processed_text[0:10]
# Sort the string using function from functions.py
processed_text = functions.quick_string(processed_text)

# Prints sorted string
print(processed_text)

# Remove duplicate letters from the string
word = ""
for char in processed_text:
    if char not in word:
        word += char

# Prints final string to find permutations for
print(word)

# Prints permutations of the word
print(functions.string_permutations(word))
