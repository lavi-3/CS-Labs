import string

# Define the alphabet
LETTER_ALPHABET = string.ascii_uppercase


# Function to remove spaces and convert to uppercase
def clean_input(input_str):
    return input_str.replace(" ", "").upper()


# Function to validate input text
def validate_input(text):
    if not all(char in LETTER_ALPHABET for char in text):
        raise ValueError("Invalid characters in the input text. It must contain only Latin alphabet letters.")
    return text


# Function to validate key 2
def validate_key(key2):
    if len(key2) < 7 or not all(char in LETTER_ALPHABET for char in key2):
        raise ValueError("Key 2 must have at least 7 characters and contain only Latin alphabet letters.")
    return key2


# Function to generate a shifted alphabet based on key 2
def generate_shifted_alphabet(key2):
    unique_chars = ''.join(dict.fromkeys(key2))
    shifted = unique_chars + ''.join(char for char in LETTER_ALPHABET if char not in unique_chars)
    return shifted


# Function for Caesar cipher encryption
def caesar_encrypt(text, key):
    result = ''.join(LETTER_ALPHABET[(LETTER_ALPHABET.index(char) + key) % 26] for char in text)
    return result


# Function for Caesar cipher decryption
def caesar_decrypt(text, key):
    result = ''.join(LETTER_ALPHABET[(LETTER_ALPHABET.index(char) - key) % 26] for char in text)
    return result


# Function for encryption using 2 keys
def encrypt_with_2_keys(text, key1, key2):
    encrypted_text = caesar_encrypt(text, key1)
    shifted_alphabet = generate_shifted_alphabet(key2)
    result = ''.join(shifted_alphabet[LETTER_ALPHABET.index(char)] for char in encrypted_text)
    return result


# Function for decryption using 2 keys
def decrypt_with_2_keys(text, key1, key2):
    shifted_alphabet = generate_shifted_alphabet(key2)
    intermediate_text = ''.join(LETTER_ALPHABET[shifted_alphabet.index(char)] for char in text)
    result = caesar_decrypt(intermediate_text, key1)
    return result


# Main function
def main():
    global ENCRYPTED_MESSAGE

    while True:

        print("\nSelect an operation:")
        print("--------------------")
        print("1 - Encryption")
        print("2 - Decryption")
        print("3 - Encryption with 2 keys")
        print("4 - Decryption with 2 keys")
        print("q - Exit")
        print("--------------------")
        print("The text for encryption/decryption must contain only Latin alphabet letters and optionally spaces.")
        print("The first key must be an integer between 1 and 25 and the second key must have at least 7 characters.")

        choice = input("Enter your choice: ")

        if choice == 'q':
            break

        if choice in ['1', '3']:
            message = input("Enter the text for encryption: ")
            sanitized_message = clean_input(message)

            try:
                validate_input(sanitized_message)
            except ValueError as e:
                print(e)
                continue

            key1 = int(input("Enter key 1: "))
            if not 1 <= key1 <= 25:
                print("Invalid key 1. Please enter a value between 1 and 25.")
                continue

            if choice == '1':
                ENCRYPTED_MESSAGE = caesar_encrypt(sanitized_message, key1)
                print("Encrypted text:", ENCRYPTED_MESSAGE)
            else:
                key2 = input("Enter key 2: ")
                try:
                    key2 = validate_key(clean_input(key2))
                except ValueError as e:
                    print(e)
                    continue

                shifted_alphabet = generate_shifted_alphabet(key2)
                ENCRYPTED_MESSAGE = encrypt_with_2_keys(sanitized_message, key1, key2)
                print("Shifted alphabet based on key 2:", shifted_alphabet)
                print("Encrypted text with 2 keys:", ENCRYPTED_MESSAGE)

        elif choice in ['2', '4']:
            encrypted_message = input("Enter the encrypted text for decryption: ")
            sanitized_message = clean_input(encrypted_message)

            try:
                validate_input(sanitized_message)
            except ValueError as e:
                print(e)
                continue

            key1 = int(input("Enter key 1: "))
            if not 1 <= key1 <= 25:
                print("Invalid key 1. Please enter a value between 1 and 25.")
                continue

            if choice == '2':
                decrypted_message = caesar_decrypt(sanitized_message, key1)
                print("Decrypted text:", decrypted_message)
            else:
                key2 = input("Enter key 2: ")
                try:
                    key2 = validate_key(clean_input(key2))
                except ValueError as e:
                    print(e)
                    continue

                decrypted_message = decrypt_with_2_keys(sanitized_message, key1, key2)
                print("Decrypted text with 2 keys:", decrypted_message)

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    ENCRYPTED_MESSAGE = ""
    main()
