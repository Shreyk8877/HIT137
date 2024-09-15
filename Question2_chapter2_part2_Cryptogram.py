# List of common words in English
common_words_list = ["the","a", "an", "there","that","and", "is", "am", "are", "in", "at", "on", "you", "he", "she", "it", "was", "were", "for"]

# Function to decrypt Caesar cipher
def caesar_cipher(ciphertext, key):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():  # Shift only letters
            key = key % 26  # Ensure the key is always within the valid range of 0 to 25
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            elif char.islower():
                decrypted_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            decrypted_text += char  # Keep non-letter characters unchanged
    return decrypted_text

# Function to check if a decrypted text contains common words
def common_words(decrypted_text):
    words = decrypted_text.lower().split()
    common_count = sum(1 for word in words if word in common_words_list)
    return common_count

# Given cipher text
cipher_text = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY \nNAQ NG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF \nURYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

best_key = 0
max_common_words = 0
best_decryption = ""

# Loop through all possible shifts from 1 to 26
for key in range(1, 27):
    decrypted_message = caesar_cipher(cipher_text, key)
    common_word_count = common_words(decrypted_message)
    
    # Keep track of the best decryption (with the most common words)
    if common_word_count > max_common_words:
        max_common_words = common_word_count
        best_key = key
        best_decryption = decrypted_message

# Output the best shift and decryption
print(f"Best key: {best_key}")
print(f"Decrypted message:\n{best_decryption}")
