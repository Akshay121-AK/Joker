from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt_file(file_path, output_path):
    # Generate a random 256-bit key
    key = get_random_bytes(32)

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_EAX)

    with open(file_path, "rb") as file:
        plaintext = file.read()

    # Encrypt the file
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # Save the encrypted file
    with open(output_path, "wb") as file:
        file.write(cipher.nonce)
        file.write(tag)
        file.write(ciphertext)

    print(f"File encrypted and saved as {output_path}")

def find_internal_storage():

    directory = "/storage/emulated/0/"

    if os.path.exists(directory):
        return directory

    raise FileNotFoundError("Internal storage not found")

def main():
    try:
        internal_storage = find_internal_storage()
        file_to_encrypt = os.path.join(internal_storage, "example.txt")
        encrypted_file = os.path.join(internal_storage, "encrypted_example.txt")

        encrypt_file(file_to_encrypt, encrypted_file)

    except FileNotFoundError as e:
        print(f"Error: {e}")


main()
