# Palindrome Checker
import string

def is_palindrome(text):
    # Convert to lowercase
    text = text.lower()

    # Remove spaces and punctuation
    cleaned_text = ""
    for char in text:
        if char.isalnum():   # keeps only letters and numbers
            cleaned_text += char

    # Check palindrome
    return cleaned_text == cleaned_text[::-1]


# use while loop to continuously ask for input until the user decides to quit

while True:
    word = input("Enter a string: ")
    if is_palindrome(word):
        print(f"It is a palindrome because '{word}' reads the same backward and forward.")
        break
    else:
        print(f"Not a palindrome because '{word}' does not read the same backward and forward.")
        