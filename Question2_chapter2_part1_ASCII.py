# QUESTION 2
# CHAPTER 2: THE CHAMPER OF STRINGS
# Part 1

def process_string(s):
    # Check if the string length is at least 16 characters
    if len(s) < 16:
        return "The length of the string must be at least 16."

    # Initialize lists for collecting results
    even_numbers = []
    uppercase_letters = []
    even_numbers_ascii = []
    uppercase_letters_ascii = []
    
    # Extract all digits and letters from the input string
    digits = [char for char in s if char.isdigit()]
    letters = [char for char in s if char.isalpha()]

    # Process each character in the string
    for char in s:
        # Check if the character is a digit and if it's even
        if char.isdigit() and int(char) % 2 == 0:
            even_numbers.append(char)
            even_numbers_ascii.append(str(ord(char)))  # Store ASCII code of even number as string
        
        # Check if the character is an uppercase letter
        elif char.isupper():
            uppercase_letters.append(char)
            uppercase_letters_ascii.append(str(ord(char)))  # Store ASCII code of uppercase letter as string

    # Return the results in a dictionary
    return {
        "Number string": ''.join(digits),
        "Letter string": ''.join(letters),
        "Even Numbers": ', '.join(even_numbers),
        "ASCII codes of Even Numbers": ', '.join(even_numbers_ascii),
        "Uppercase Letters": ', '.join(uppercase_letters),
        "ASCII codes of Uppercase Letters": ', '.join(uppercase_letters_ascii)
    }

# Example input
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'

# Call the function and store the result
result = process_string(s)

# Display the results
for key, value in result.items():
    print(f"{key}: {value}")
