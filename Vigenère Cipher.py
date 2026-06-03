# Vigenère Cipher

def prepare_key(key, text):
    # Repeat key to match length of text
    new_key_list = []
    for i in range(len(text)):
        new_key_list.append(key[i % len(key)])

    # Convert repeated key to uppercase string
    new_key = "".join(new_key_list).upper()
    return new_key


def encrypt(plaintext, key):
    # Map A–Z → 0–25 and 0–25 → A–Z
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict_alpha = {}
    dict_num = {}

    for i in range(26):
        dict_alpha[alphabet[i]] = i
        dict_num[i] = alphabet[i]

    ciphertext = []
    i = 0

    # Vigenère encryption: (P + K) % 26
    for char in plaintext:
        position = (dict_alpha[char] + dict_alpha[key[i]]) % 26
        ciphertext.append(dict_num[position])
        i += 1

    print("Ciphertext:", ''.join(ciphertext))


def decrypt(ciphertext, key):
    # Same mapping as encryption
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict_alpha = {}
    dict_num = {}

    for i in range(26):
        dict_alpha[alphabet[i]] = i
        dict_num[i] = alphabet[i]

    plaintext = []
    i = 0

    # Vigenère decryption: (C - K) % 26
    for char in ciphertext:
        position = (dict_alpha[char] - dict_alpha[key[i]]) % 26
        plaintext.append(dict_num[position])
        i += 1

    print("Plaintext:", ''.join(plaintext))


import string

# Take valid key input (only letters allowed)
while True:
    print("=== Vigenère Cipher ===")
    key = input("Enter key: ")

    if key.isalpha():
        key = key.upper()   
        break
    else:
        print("Invalid input. Use letters only.")


while True:
    try:
        print("""
        1. Plaintext to Cipher
        2. Cipher to Plaintext
        3. Exit
        """)

        choice = int(input("Enter your choice: "))

        if choice == 1:
            plaintext_user = input("Enter your plaintext: ")
            plaintext_user = plaintext_user.replace(" ", "").upper()

            new_key = prepare_key(key, plaintext_user)
            encrypt(plaintext_user, new_key)

        elif choice == 2:
            ciphertext_user = input("Enter your ciphertext: ")
            ciphertext_user = ciphertext_user.replace(" ", "").upper()

            new_key = prepare_key(key, ciphertext_user)
            decrypt(ciphertext_user, new_key)

        elif choice == 3:
            print("Exiting...")
            exit()

    except ValueError:
        print("Invalid input!\n")


    ''' 

    Sample Key: deceptive 
    Sample Plaintext: wearediscoveredsaveyourself 
    Sample Ciphertext:ZICVTWQNGRZGVTWAVZHCQYGLMGJ 
    
    '''