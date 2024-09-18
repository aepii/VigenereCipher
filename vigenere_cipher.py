"""
Task 1: In this mini project, you are first asked to implement a simple Vigenère Cipher.
• The algorithm for encryption: EK(m) = m + K mod 26
• The algorithm for decryption: DK(m) = m - K mod 26
Format: (1) the plaintext/ciphertext should only contain letters (but you do not need to check the
validity of the input. We assume that the input is always valid). (2) Spaces in the plaintext should be
removed. (3) Your input/output should be text strings, with both uppercase and uppercase letters. The
same letter in upper and upper cases are treated as the same. That is, both "A" and "a" must be
converted to "1" (or "0") in your program.
"""

ASCII_BASE_A = ord("A")
ALPHABET_SIZE = 26

def parse_string(string):
    return string.upper().replace(" ", "")

def recursive_encrypt(plain_text, key):
    plain_text = parse_string(plain_text)
    key = parse_string(key)
    cipher_text = ""
    for index, letter in enumerate(plain_text):
        current_key = key[index % len(key)]
        cipher_text += _single_encrypt(letter, current_key)
    return cipher_text

def _single_encrypt(letter, key):
    return chr((ord(letter) - ASCII_BASE_A + ord(key) - ASCII_BASE_A) % ALPHABET_SIZE + ASCII_BASE_A)

def recursive_decrypt(cipher_text, key):
    cipher_text = parse_string(cipher_text)
    key = parse_string(key)
    decoded_text = ""
    for index, letter in enumerate(cipher_text):
        current_key = key[index % len(key)]
        decoded_text += _single_decrypt(letter, current_key)
    return decoded_text

def _single_decrypt(letter, key):
    return chr((ord(letter) - ord(key) + ALPHABET_SIZE) % ALPHABET_SIZE + ASCII_BASE_A)
