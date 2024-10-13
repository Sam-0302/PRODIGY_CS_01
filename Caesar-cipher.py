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
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program to take user input
def main():
    print("Caesar Cipher Program")
    message = input("Enter the message: ")
    shift = int(input("Enter shift value: "))
    
    # Encrypting the message
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypting the message
    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
