import vigenere_cipher

def test_vigenere_cipher():
    plain_text = "Hello World"
    key = "Test"
    
    cipher_text = vigenere_cipher.recursive_encrypt(plain_text, key)
    print(f"Cipher Text: {cipher_text}")

    expected_cipher_text = "AIDEHAGKEH" 
    assert cipher_text == expected_cipher_text, f"Expected {expected_cipher_text}, got {cipher_text}"

    decoded_text = vigenere_cipher.recursive_decrypt(cipher_text, key)
    print(f"Decoded Text: {decoded_text}")

    expected_decoded_text = "HELLOWORLD"
    assert decoded_text == expected_decoded_text, f"Expected {expected_decoded_text}, got {decoded_text}"

def main():
    test_vigenere_cipher()
    print("All tests passed!")

if __name__ == "__main__":
    main()
