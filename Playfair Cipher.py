# Playfair Cipher
def make_matrix(key,alphabet):
    key_final = []
    alphabet_final = list(alphabet)
    key = key.upper()
    key = key.replace("J","I")
    for character in key:
        if character in key_final:
            pass
        else:
            key_final.append(character)
            if character in alphabet_final:
                alphabet_final.remove(character)

    combined_letters = key_final + alphabet_final
    matrix = []

    for i in range(0,25,5):
        row = combined_letters[i:i+5]
        matrix.append(row)
    
    return matrix


def find_position(matrix,letter):
    for row in range(0,5):
        for column in range(0,5):
            if matrix[row][column] == letter:
                return row,column



def prepare_plaintext(plaintext):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace("J","I")
    plaintext = ''.join(char for char in plaintext if char.isalpha())

    pairs = []
    i = 0
    while i<len(plaintext):
        first = plaintext[i]

        if i+1 < len(plaintext):
            second = plaintext[i+1]

            if first == second:
                pairs.append(first + "X")
                i += 1

            else:
                pairs.append(first + second)
                i += 2

        else:
            pairs.append(first + "X")
            i += 1

    return pairs


def prepare_ciphertext(ciphertext):
    ciphertext = ciphertext.upper()
    ciphertext = ciphertext.replace("J","I")
    ciphertext = ''.join(char for char in ciphertext if char.isalpha())

    if len(ciphertext) % 2 != 0:
        print("Invalid ciphertext length.")
        return []

    pairs = []
    for i in range(0, len(ciphertext), 2):
        pairs.append(ciphertext[i:i+2])

    return pairs


def encrypt_text(matrix, pairs):
    ciphertext = ""
    for pair in pairs:
        ciphertext += encrypt_pair(matrix,pair)
    return ciphertext


def decrypt_text(matrix,pairs):
    plaintext = ""
    for pair in pairs:
        plaintext += decrypt_pair(matrix,pair)
    return plaintext


def encrypt_pair(matrix,pair):
    first,second = pair

    row1, col1 = find_position(matrix, first)
    row2, col2 = find_position(matrix, second)

    if row1 == row2:
        return (matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5])

    elif col1 == col2:
        return (matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2])

    else:
        return (matrix[row1][col2] + matrix[row2][col1])


def decrypt_pair(matrix,pair):
    first,second = pair

    row1, col1 = find_position(matrix, first)
    row2, col2 = find_position(matrix, second)

    if row1 == row2:
        return (matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5])

    elif col1 == col2:
        return (matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2])

    else:
        return (matrix[row1][col2] + matrix[row2][col1])




import string

while True:
    print("=== Playfair Cipher ===")
    key = input("Enter key: ")

    if key.isalpha():
        break
    else:
        print("Invalid input. Please use letters only (A-Z).")

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
matrix = make_matrix(key,alphabet)


while True:
    try:
        print("""
        1. Plaintext to Cipher
        2. Cipher to Plaintext
        3. Exit      """)

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            plaintext = input("Enter your plaintext: ")
            pairs = prepare_plaintext(plaintext)

            ciphertext = encrypt_text(matrix,pairs)
            print("Your cihphertext:",ciphertext)

        elif choice == 2:
            ciphertext_user = input("Enter your ciphertext: ")
            pairs = prepare_ciphertext(ciphertext_user)

            if pairs:
                plaintext = decrypt_text(matrix, pairs)
                print("Your plaintext:", plaintext)

        elif choice == 3:
            print("Exiting...")
            exit()

    except ValueError:
        print("Invalid input!")
        print("\n")

