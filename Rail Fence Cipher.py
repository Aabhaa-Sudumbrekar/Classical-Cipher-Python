# Rail Fence Cipher
def encrypt(plaintext):

    rail1, rail2, rail3 = [], [], []   # 3 rails for zig-zag
    rails = [rail1, rail2, rail3]

    current_rail = 0   # start from top rail
    direction = 1      # 1 = down, -1 = up

    for char in plaintext:
        rails[current_rail].append(char)  # place char in current rail

        # change direction at boundaries
        if current_rail == 0:
            direction = 1
        elif current_rail == 2:
            direction = -1

        current_rail += direction  # move zig-zag

    # join all rails row-wise
    encrypted_text = ""
    for rail in rails:
        encrypted_text += ''.join(rail)

    print("Encrypted Text:", encrypted_text)



def decrypt(ciphertext):

    rail1, rail2, rail3 = [], [], []   # 3 rails
    rails = [rail1, rail2, rail3]

    pattern = []  # stores zig-zag path

    current_rail = 0
    direction = 1

    # rebuild zig-zag pattern
    for char in ciphertext:
        pattern.append(current_rail)

        if current_rail == 0:
            direction = 1
        elif current_rail == 2:
            direction = -1

        current_rail += direction

    # count how many letters per rail
    counts = [pattern.count(0), pattern.count(1), pattern.count(2)]

    index = 0

    # split ciphertext into rails using counts
    for r in range(3):
        rails[r] = list(ciphertext[index:index + counts[r]])
        index += counts[r]

    rail_ptr = [0, 0, 0]  # pointer for each rail
    decrypted_text = ""

    # rebuild original text using pattern
    for rail in pattern:
        decrypted_text += rails[rail][rail_ptr[rail]]
        rail_ptr[rail] += 1

    print("Decrypted Text:", decrypted_text)



while True:
    try:
        print("=== Rail Fence Cipher ===")
        print("""
        1. Plaintext to Cipher
        2. Cipher to Plaintext
        3. Exit      """)

        choice = int(input("Enter your choice: "))

        if choice == 1:
            plaintext_user = input("Enter your plaintext: ")
            plaintext_user = plaintext_user.replace(" ", "").upper()
            encrypt(plaintext_user)

        elif choice == 2:
            ciphertext_user = input("Enter your ciphertext: ")
            ciphertext_user = ciphertext_user.replace(" ", "").upper()
            decrypt(ciphertext_user)

        elif choice == 3:
            print("Exiting...")
            exit()

    except ValueError:
        print("Invalid input!")
        print("\n")


'''
Sample plaintext: THISISASECRETMESSAGE  
Sample ciphertext: TACSHSIERTMSAEISSEEG
'''