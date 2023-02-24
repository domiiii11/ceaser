alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', '<', '=', '>', '?','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', 
            ',', '‑', '.', '/', '@']

def encrypt(text, key_):
    encrypted_text = ""
    for i in range(len(text)):
        if text[i] == ' ':
            encrypted_letter = ' '
            encrypted_text += encrypted_letter
            continue
        if text[i] not in alphabet:
            continue
        encrypted_letter = alphabet[(alphabet.index(text[i]) + key_) % len(alphabet)]
        encrypted_text += encrypted_letter
    return encrypted_text

def decrypt(text, key_):
    decrypted_text = ""
    for i in range(len(text)):
        if text[i] == ' ':
            decrypted_letter = ' '
            decrypted_text += decrypted_letter
            continue
        if text[i] not in alphabet:
            continue
        decrypted_letter = alphabet[(alphabet.index(text[i]) - key_) % len(alphabet)]
        decrypted_text += decrypted_letter
    return decrypted_text

def run_cipher():
    while True:
        answer = input("Do You want to encrypt (type 'e') or decrypt (type 'd')? \n").lower()
        while answer not in ['e', 'd']:
            print("You have typed wrong symbol, try again.")
            answer = input("Do You want to encrypt (type 'e') or decrypt (type 'd')?\n").lower()
        while True:
            try:
                key_ = int(input("Please enter the key (0 to 26) to use.\n"))
                break
            except ValueError:
                print("You have typed not an integer. Type again.")
        if answer == 'e':
            text = input("Enter the message to encrypt.\n").upper()
            result = encrypt(text, key_)
            print(result)
        elif answer == 'd':
            text = input("Enter the message to decrypt.\n").upper()
            result = decrypt(text, key_)
            print(result)
        again_answer = input("Do You want to encrypt / decrypt again? (y/n)")
        
           
print(5%26)

print(2%3)