"""
Task 2: Next, you are expected to implement a brute force password cracker based on the Vigenère
Cipher you just implemented. Your password cracker is expected to take three parameters: (1) a string
of ciphertext; (2) an integer keyLength that denotes the length of the key; and (3) an integer
firstWordLength that denotes the length of the first word of the plaintext.
Your password cracker will test every possible key that has the length of keyLength: from all "A"s to all
"Z"s. You cannot exploit the dictionary to guess the key, since the key may not be a valid word.
For each key candidate, you will generate a "plaintext", and compare it with the dictionary (provided to
you). In particular, you only need to check if the first word (number of letters of the word is given in
firstWordLength) is a valid word in the dictionary. To do this, you need to load the dictionary into
memory before processing any key, and search if the first word of the "plaintext" is in the dictionary. If
Yes, display the plaintext and the key. However, do not stop, as the "plaintext" might be wrong.
Efficiency is very important in evaluating each "plaintext" candidate. In some cases, a wrong key may
generate a valid first word. Hence, you may get several "plaintexts" after all possible keys are tested.
This is acceptable. You can look at the outputs and determine which key is correct.
"""

import vigenere_cipher

ALPHABET = [chr(i) for i in range(65, 91)]  
WORD_DICT = set()

def generate_possible_keys(cipher_text, length, first_word_length):
    keys = ['']
    possible_keys = []
    
    for _ in range(length):
        new_keys = []
        for key in keys:
            for letter in ALPHABET:
                new_key = key + letter
                new_keys.append(new_key)
                if attempt_brute_force(cipher_text, new_key, first_word_length):
                    possible_keys.append(new_key)
                
        keys = new_keys

    return possible_keys
    
def attempt_brute_force(cipher_text, key, first_word_length):
    decoded_text = vigenere_cipher.recursive_decrypt(cipher_text, key)
    first_word = decoded_text[:first_word_length]

    if first_word in WORD_DICT:
        print(f"Possible Key Found: {key}, Plaintext: {decoded_text}")
        return True
    
    return False
        
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