ASCII_BASE_A = ord("A")
ALPHABET_SIZE = 26

# Remove spaces and ensure string is uppercase.
def parse_string(string):
    return string.upper().replace(" ", "")

# Encrypt plain text given key.
def recursive_encrypt(plain_text, key):
    plain_text = parse_string(plain_text) # Remove spaces and ensure string is uppercase.
    key = parse_string(key) # Remove spaces and ensure string is uppercase.
    cipher_text = "" # Stores ciphered text.
    for index, letter in enumerate(plain_text):
        current_key = key[index % len(key)]
        cipher_text += _single_encrypt(letter, current_key)
    return cipher_text

# Helper method for encrypting.
def _single_encrypt(letter, key):
    return chr((ord(letter) - ASCII_BASE_A + ord(key) - ASCII_BASE_A) % ALPHABET_SIZE + ASCII_BASE_A) # EK(m) = m + K mod 26

# Decrypt cipher text given key.
def recursive_decrypt(cipher_text, key):
    cipher_text = parse_string(cipher_text) # Remove spaces and ensure string is uppercase.
    key = parse_string(key) # Remove spaces and ensure string is uppercase.
    decoded_text = "" # Stores decoded text.
    for index, letter in enumerate(cipher_text):
        current_key = key[index % len(key)]
        decoded_text += _single_decrypt(letter, current_key)
    return decoded_text

# Helper method for decrypting.
def _single_decrypt(letter, key):
    return chr((ord(letter) - ord(key) + ALPHABET_SIZE) % ALPHABET_SIZE + ASCII_BASE_A) # DK(m) = m - K mod 26
