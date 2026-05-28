#Caesar cipher
def convert_cipher (user_input, user_key, alphabet):
    letter_to_num = {}
    num_to_letter = {}
    for (i,item) in enumerate(alphabet):  
            letter_to_num[item] = i
            num_to_letter[i] = item

    output = ""
    for character in user_input:
        if character in letter_to_num:
            count = int((letter_to_num[character]+user_key)%26)
            output += num_to_letter[count]
        else:
             output += character

    print()
    print("=== OUTPUT ===")
    print(f"Plain text: {user_input}")
    print(f"Cipher text: {output}")


def convert_plaintext(user_input, user_key, alphabet):
    letter_to_num = {}
    num_to_letter = {}
    for (i,item) in enumerate(alphabet):
        letter_to_num[item] = i
        num_to_letter[i] = item

    output = ""
    for character in user_input:
        if character in letter_to_num:
            count = int((letter_to_num[character]-user_key)%26)
            output += num_to_letter[count]
        else:
             output += character

    print()
    print("=== OUTPUT ===")
    print(f"Cipher text: {user_input}")
    print(f"Plain text: {output}")


import string
alphabet = list(string.ascii_uppercase)
print("=== CAESAR CIPHER ===")
while True:
    try:
        choice = int(input(""" 
        1. Convert plaintext to ciphertext
        2. Covert ciphertext to plaintext
        3. Exit 
    Please enter choice: """))

        if choice == 1:
            user_input = str(input("Enter your plaintext: ")).upper()
            while True:
                try:
                    key = int(input("Enter key: "))
                    break
                except ValueError:
                    print("Please enter an integer value!")
            convert_cipher(user_input,key,alphabet)

        elif choice == 2:
            user_input = str(input("Enter your ciphertext: ")).upper()
            while True:
                try:
                    key = int(input("Enter key: "))
                    break
                except ValueError:
                    print("Please enter an integer value!")
            convert_plaintext(user_input,key,alphabet)

        elif choice == 3:
            print("Exiting...")
            break

    except ValueError:
        print("Please enter an integer value!")

