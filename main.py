import vigenere_cipher # Import Vigenere Cipher. 

import time # Import time.

ALPHABET = [chr(i) for i in range(65, 91)] # Array containing letters A-Z.
WORD_DICT = set() # Set containing words from dictionary.

# Generates possible keys and attempts a crack with generated key.
def generate_possible_keys(cipher_text, length, first_word_length):
    keys = [''] # Empty key array.
    possible_keys = [] # Keys that are a possible match.

    start = time.time() # Start time.
    
    # Generate possible keys.
    for _ in range(length):
        new_keys = []
        for key in keys:
            for letter in ALPHABET:
                new_key = key + letter
                new_keys.append(new_key)
                if attempt_brute_force(cipher_text, new_key, first_word_length): # Attempt a crack.
                    possible_keys.append(new_key) # If it hits, add it to possible keys.
                
        keys = new_keys

    end = time.time() # End time.
    print(f"Elapsed Time: {end - start}")
    return possible_keys # Return all possible keys that were a hit.

# Attempt a crack. 
def attempt_brute_force(cipher_text, key, first_word_length):
    decoded_text = vigenere_cipher.recursive_decrypt(cipher_text, key) # Decrypt text given key.
    first_word = decoded_text[:first_word_length]

    if first_word in WORD_DICT: # If the word exist in the dictionary, its a hit.
        print(f"Possible Key Found: {key}, Plaintext: {decoded_text}")
        return True
    
    return False

# Loads dictionary from file.
def load_dictionary():
    global WORD_DICT
    with open("MP1_dict.txt") as file:
        WORD_DICT = set(word.strip().upper() for word in file) 

def main():
    print("Loading Dictionary.")
    load_dictionary()
    print("Loaded Dictionary.\n")

    cipher_texts = ["MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", "PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC",
                    "MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", "SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG", "LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS", 
                    "VVVLZWWPBWHZDKBTXLDCGOTGTGRWAQWZSDHEMXLBELUMO"]
    key_lengths = [2, 3, 4, 5, 6, 7]
    first_word_lengths = [6, 7, 10, 11, 9, 13]


    for index, cipher_text in enumerate(cipher_texts):
        print(f"Generating Possible Keys For {cipher_text}.")
        possible_keys = generate_possible_keys(cipher_text, key_lengths[index], first_word_lengths[index])
        print(f"Generated Possible Keys For {cipher_text}.: {possible_keys}\n")


if __name__ == "__main__":
    main()