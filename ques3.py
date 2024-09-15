encrypted_code = """
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'} 

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]
    
    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir (ybpny_inevnoyr)
        ybpny_inevnoyr -= 1
    
    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr 
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag (zl_qvpg)
cevag (zl_frg)
"""

def encrypt(text: str, key: int):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):        
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

# def decrypt_simple(text: str, key: int):
#     decrypted_text = ""
#     for char in text:
#         if char.isalpha():
#             shifted = ord(char) + key
#             if char.islower():
#                 if shifted > ord('z'):
#                     shifted -= 26
#                 elif shifted < ord('a'):        
#                     shifted += 26
#             elif char.isupper():
#                 if shifted > ord('Z'):
#                     shifted -= 26
#                 elif shifted < ord('A'):
#                     shifted += 26
#             decrypted_text += chr(shifted)
#         else:
#             decrypted_text += char
#     return decrypted_text

def decrypt_char(char: str, key: int):
    # if char is not an alphabet like _, #, %, this will remain as it is
    if not char.isalpha():
        return char
    
    # only come here if char is an alphabet
    shifted = ord(char) - key # reversing the shifting operation that was performed with encrypt
    shifted_ignorecase = ord(char.lower()) - key # converting the char to lower case and performing the above to avoid two if checks
    if shifted_ignorecase < ord('a'):
        return chr(shifted + 26) # convert the shifted value back to character if its below the value for 'a'
    
    # if the shifted character was already a character as well i.e. >= 'a'
    return chr(shifted)

def decrypt(text: str, key: int):
    # joining all the decrypted characters with the delimiter empty space ('')
    return ''.join([decrypt_char(char, key) for char in text])


total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2

print(f"Key={total}")
print(decrypt(encrypted_code, total))


