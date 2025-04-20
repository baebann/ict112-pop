This is my assignement 
"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Using string slicing
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed using slicing:", reversed_string)

# Using a loop
reversed_with_loop = ""
for char in original_string:
    reversed_with_loop = char + reversed_with_loop
print("Reversed using a loop:", reversed_with_loop)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
    # Split the name into parts
    name_parts = full_name.split()
    
    # Get the first letter of each part and convert to uppercase
    initials = [part[0].upper() for part in name_parts]
    
    # Join the initials with dots
    return ".".join(initials)

# Get user input
user_name = input("Enter your full name: ")

# Print the initials
print("Initials:", get_initials(user_name))



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    # Convert to lowercase to make it case-insensitive
    s = s.lower()
    
    # Compare the original string with its reverse
    return s == s[::-1]

# Get user input
user_string = input("Enter a word or phrase: ")

# Check if the input is a palindrome
if is_palindrome(user_string):
    print(f'"{user_string}" is a palindrome!')
else:
    print(f'"{user_string}" is not a palindrome.')



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
    # Split the sentence into words based on spaces
    words = sentence.split()
    
    # Return the number of words
    return len(words)

# Get user input
user_sentence = input("Enter a sentence: ")

# Print the word count
print("Number of words:", count_words(user_sentence))



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Define the original string
original_string = "This is a string and it is an example."

# Replace "is" with "was"
modified_string = original_string.replace("is", "was")

# Print the modified string
print("Modified string:", modified_string)
