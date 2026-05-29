# Monoalphabetic Cipher
import json
import string
import random

alphabet = string.ascii_uppercase
encrypt_key = list(alphabet)
random.shuffle(encrypt_key)
encrypt_key = ''.join(encrypt_key)
with open("key.json","w") as f:
    json.dump(encrypt_key,f)


while True:
    try:
        print("=== Monoalphabetic Cipher ===")
        print("""
        1. Plaintext to Cipher
        2. Cipher to Plaintext
        3. Exit      """)

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            user_input = str(input("Enter your plaintext: ")).upper()

            with open("key.json","r") as f:
                encrypt_key = json.load(f)

            encrypt_dict = {}
            for i in range (len(alphabet)):  
                    encrypt_dict[alphabet[i]] = encrypt_key[i]

            output = ""
            for character in user_input:
                if character in encrypt_dict:
                    output += encrypt_dict[character]
                else:
                    output += character

            print()
            print("=== OUTPUT ===")
            print(f"Plain text: {user_input}")
            print(f"Cipher text: {output}")
            print("\n")


        elif choice == 2:
            user_input = str(input("Enter your ciphertext: ")).upper()

            with open("key.json","r") as f:
                encrypt_key = json.load(f)

            decrypt_dict = {}
            for i in range (len(alphabet)):  
                    decrypt_dict[encrypt_key[i]] = alphabet[i]

            output = ""
            for character in user_input:
                if character in decrypt_dict:
                    output += decrypt_dict[character]
                else:
                    output += character

            print()
            print("=== OUTPUT ===")
            print(f"Cipher text: {user_input}")
            print(f"Plain text: {output}")
            print("\n")


        elif choice == 3:
            print("Exiting...")
            break


        else:
            print("Invalid input!")
            print("\n")

    except ValueError:
        print("Invalid input!")
        print("\n")
