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
If one letter remains, X is added,

-------------------------------------------------------------------------------------------------------
