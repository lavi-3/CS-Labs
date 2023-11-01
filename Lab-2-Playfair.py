def generate_matrix(key):
    # Create a 6x6 Playfair matrix for the extended Romanian alphabet
    alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZaăâbcdefghiîjklmnopqrsștțuvwxyzăâîșț"
    key = key.upper()
    key = ''.join(dict.fromkeys(key))  # Remove duplicates

    matrix = []
    for char in key:
        if char in alphabet:
            alphabet = alphabet.replace(char, "")
    key += alphabet

    for i in range(0, len(key), 6):
        matrix.append(list(key[i:i+6]))

    return matrix

def print_matrix(matrix):
    print("Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))

def preprocess_text(text):
    # Remove spaces and convert to uppercase
    text = text.replace(" ", "")
    text = text.upper()
    # If the length of the text is odd, add an "X" to the end
    if len(text) % 2 != 0:
        text += "X"
    return text

def encrypt(plaintext, matrix):
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i+1]
        row1, col1, row2, col2 = -1, -1, -1, -1

        # Find the positions of the characters in the matrix
        for r in range(6):
            if char1 in matrix[r]:
                row1, col1 = r, matrix[r].index(char1)
            if char2 in matrix[r]:
                row2, col2 = r, matrix[r].index(char2)

        # Apply Playfair rules to find the new characters
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 6]
            ciphertext += matrix[row2][(col2 + 1) % 6]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 6][col1]
            ciphertext += matrix[(row2 + 1) % 6][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

def decrypt(ciphertext, matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1, row2, col2 = -1, -1, -1, -1

        # Find the positions of the characters in the matrix
        for r in range(6):
            if char1 in matrix[r]:
                row1, col1 = r, matrix[r].index(char1)
            if char2 in matrix[r]:
                row2, col2 = r, matrix[r].index(char2)

        # Apply Playfair rules to find the new characters
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 6]
            plaintext += matrix[row2][(col2 - 1) % 6]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 6][col1]
            plaintext += matrix[(row2 - 1) % 6][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext

def main_menu():
    while True:
        print("Choose an option:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            key = input("Enter the encryption key (at least 7 characters long): ")
            plaintext = input("Enter the text to be encrypted: ")
            if len(key) < 7:
                print("The key should be at least 7 characters long.")
            else:
                matrix = generate_matrix(key)
                print_matrix(matrix)  # Display the Playfair matrix
                plaintext = preprocess_text(plaintext)
                encrypted_text = encrypt(plaintext, matrix)
                print("Encrypted Text:", encrypted_text)
        elif choice == '2':
            key = input("Enter the decryption key: ")
            ciphertext = input("Enter the text to be decrypted: ")
            matrix = generate_matrix(key)
            decrypted_text = decrypt(ciphertext, matrix)
            print("Decrypted Text:", decrypted_text)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
