"""
Task 1: In this mini project, you are first asked to implement a simple Vigenère Cipher.
• The algorithm for encryption: EK(m) = m + K mod 26
• The algorithm for decryption: DK(m) = m - K mod 26
Format: (1) the plaintext/ciphertext should only contain letters (but you do not need to check the
validity of the input. We assume that the input is always valid). (2) Spaces in the plaintext should be
removed. (3) Your input/output should be text strings, with both uppercase and lowercase letters. The
same letter in upper and lower cases are treated as the same. That is, both "A" and "a" must be
converted to "1" (or "0") in your program.
"""

BASE = ord("a")
MOD = 26

class VigenereCipher:

    def __init__(self, plain_text, key):
        self.plain_text = self.parse_string(plain_text)
        self.key = self.parse_string(key)

    @staticmethod
    def parse_string(string):
        return string.lower().replace(" ", "")

    def recursive_encrypt(self):
        cipher_text = ""
        for index, letter in enumerate(self.plain_text):
            current_key = self.key[index % len(self.key)]
            cipher_text += self._single_encrypt(letter, current_key)
        return cipher_text

    @staticmethod
    def _single_encrypt(letter, key):
        return chr((ord(letter) - BASE + ord(key) - BASE) % MOD + BASE)
    
    def recursive_decrypt(self, cipher_text):
        decoded_text = ""
        for index, letter in enumerate(cipher_text):
            current_key = self.key[index % len(self.key)]
            decoded_text += self._single_decrypt(letter, current_key)
        return decoded_text

    @staticmethod
    def _single_decrypt(letter, key):
        return chr((ord(letter) - ord(key) + MOD) % MOD + BASE)

def main():
    plain_text = "Hello World"
    key = "Test"
    vigenere_cipher = VigenereCipher(plain_text, key)
    cipher_text = vigenere_cipher.recursive_encrypt()
    print(cipher_text)
    decoded_text = vigenere_cipher.recursive_decrypt(cipher_text)
    print(decoded_text)


if __name__ == "__main__":
    main()