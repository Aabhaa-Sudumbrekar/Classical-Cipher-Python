Classical Cipher Implementations (Python)

This repository contains Python implementations of classical encryption techniques. Each program demonstrates how traditional ciphers work using substitution and transformation methods.

-------------------------------------------------------------------------------------------------------
Implemented Ciphers:
1. Caesar Cipher
A substitution cipher where each letter is shifted by a fixed number of positions in the alphabet.

Encryption and decryption,
Custom shift key,
Preserves spaces and symbols,
Uppercase handling,

-------------------------------------------------------------------------------------------------------

2. Monoalphabetic Cipher
A substitution cipher where each alphabet letter maps to a randomly shuffled alphabet.

Random key generation,
Encryption and decryption,
Key storage using JSON,
Preservation of spaces and symbols,
Uppercase text handling

-------------------------------------------------------------------------------------------------------

3. Playfair Cipher
A digraph substitution cipher using a 5×5 key matrix (I/J combined).

Rules:
Same row → replace each letter with the one to its right (wrap around if needed),
Same column → replace each letter with the one below it (wrap around if needed),
Rectangle → replace each letter with the one in the same row but the other letter’s column,

Notes:
Text is processed in pairs of letters,
Repeated letters in a pair are separated using X,
If one letter remains, X is added

-------------------------------------------------------------------------------------------------------

4. Rail Fence Cipher
A transposition cipher where characters are written in a zig-zag pattern across multiple rails.

Rules:
Plaintext is written in a zig-zag pattern across 3 rails,
Characters move diagonally down and up between rails,
Ciphertext is formed by reading each rail sequentially,
Decryption rebuilds the zig-zag pattern using the same rail order,

Notes:
Spaces are removed before processing,
Input is converted to uppercase,
Works using pattern reconstruction during decryption

-------------------------------------------------------------------------------------------------------

Vigenère Cipher
A polyalphabetic substitution cipher that uses a repeating keyword to shift letters.

Rules:
Each letter of plaintext is shifted based on the corresponding letter of the repeating key,
Encryption: (Plaintext + Key) mod 26,
Decryption: (Ciphertext - Key) mod 26,
Key is repeated to match the length of the message

Notes:
Only uppercase letters A–Z are used,
Key is automatically repeated to match message length,
Spaces are removed before processing
