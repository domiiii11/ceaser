# The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
# encrypts letters by shifting them over by a 
# certain number of places in the alphabet. We 
# call the length of shift the key. For example, if the 
# key is 3, then A becomes D, B becomes E, C becomes 
# F, and so on. To decrypt the message, you must shift 
# the encrypted letters in the opposite direction. This 
# program lets the user encrypt and decrypt messages 
# according to this algorithm.

# When you run the code, the output will look like this:

# Do you want to (e)ncrypt or (d)ecrypt?
# > e
# Please enter the key (0 to 25) to use.
# > 4
# Enter the message to encrypt.
# > Meet me by the rose bushes tonight.
# QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


# Do you want to (e)ncrypt or (d)ecrypt?
# > d
# Please enter the key (0 to 26) to use.
# > 4
# Enter the message to decrypt.
# > QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
# MEET ME BY THE ROSE BUSHES TONIGHT.

import string
import re
alphabet = string.ascii_uppercase


def encrypt_or_decrypt():
    answer = input("Do You want to encrypt (type 'e') or decrypt (type 'd')? \n").lower()
    while answer not in ['e','d']:
        print("You have typed wrong symbol, try again.")
        answer = input("Do You want to encrypt (type 'e') or decrypt (type 'd')?\n")
    return answer


def get_validate_key():
    key_ = int(input("Please enter the key (0 to 26) to use.\n"))
    while not isinstance(key_, int) or not (0 <= key_ <= 26):
        print("You have entered an invalid key. Please enter an integer between 0 and 26.")  
        key_ = int(input("Please enter the key (0 to 26) to use.\n"))
    return key_


def get_validate_text():
    text = (input("Enter the message to encrypt.\n")).upper()        
    while not re.match(r'^[\w\s:<>?!"#$%&\'()*+,‑./@]+$', text):
        print("Text must contain latin letters, symbols or numbers.")       
        text = (input("Enter the message to encrypt.\n")).upper()
    return text


def end_dec_again():
    again_answer = input("Do You want to encrypt / decrypt again? (y/n)")  
    while again_answer not in ['y', 'n']:
        print("You have typed wrong symbol, try again (y/n).")
        again_answer = input("Do You want to encrypt / decrypt again? (y/n)")  
    return again_answer

#going through text, checking for spaces and adding spaces to text if found
# going through alphabet checking if letters from text is the same as letter
# from alphabet if yes then counting new index by adding key to index of letter of alphabet.
# Modulo is clarify that newly found index is in the range of alphabet.

def encrypt(text, key_):
    encrypted_text = ""    
    for i in range(len(text)):        
        if text[i] == ' ':
                encrypted_letter = ' '
                encrypted_text += encrypted_letter
                continue
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                encrypted_letter = alphabet[(j + key_) % len(alphabet)]
                encrypted_text += encrypted_letter
                break
    return encrypted_text  

#going through text, checking for spaces and adding spaces to text if found
# going through alphabet checking if letters from text is the same as letter
        # from alphabet if yes then counting new index by adding key to index of letter of alphabet.
        # Modulo is clarify that newly found index is in the range of alphabet.


def decrypt(text, key_):
    decrypted_text = ""
    for i in range(len(text)):       
        if text[i] == ' ':
            decrypted_letter = ' '
            decrypted_text += decrypted_letter
            continue        
        for j in range(len(alphabet)):
            if text[i] ==alphabet[j]:
                decrypted_letter = alphabet[(j - key_) % len(alphabet)]
                decrypted_text += decrypted_letter
                break
    return decrypted_text

#this function runs the programme and performs all needed validation:
# if key is an integer from 0 to 26
# if letters in message only contain characters in alphabet
# receives inputs if user want to continue to use a programme or not


def run_cipher():
    result = ''
    while True:
        answer = encrypt_or_decrypt()
        key_ = get_validate_key()
        text = get_validate_text()        
        if answer == 'e':
            result = encrypt(text, key_)          
        elif answer =='d':
            result = decrypt(text, key_)
        print(result)
        again_answer = end_dec_again()    
        if again_answer =='n':
            break

run_cipher()




    

    
