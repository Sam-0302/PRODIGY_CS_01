# Function to encrypt the message
def encrypt(text, shift):
    result = ""
    # Traverse through the message
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep non-alphabet characters unchanged
        else:
            result += char
    return result

# Function to decrypt the message
def decrypt(text, shift, original_shift):
    if shift == original_shift:
        return encrypt(text, -shift)
    else:
        return "Error: Incorrect shift value for decryption!"

# Main program to take user input
def main():
    print("Caesar Cipher Program")
    
    # Encrypt the message
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter shift value for encryption: "))
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypt_shift = int(input("Enter shift value for decryption: "))
    decrypted_message = decrypt(encrypted_message, decrypt_shift, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
