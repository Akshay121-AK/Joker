from kivy.app import App
from kivy.uix.button import Button
from android.permissions import request_permissions, Permission
import os

class FileCreatorApp(App):
    def build(self):
        # Request external storage write permission
        request_permissions([Permission.WRITE_EXTERNAL_STORAGE])

        # Create a button to trigger the file creation
        button = Button(text='Create Text File in DCIM', on_press=self.create_file)
        return button

    def create_file(self, instance):
        try:
            # Check if the permission is granted
            if Permission.WRITE_EXTERNAL_STORAGE in self.permissions:
                # Specify the DCIM directory path
                dcim_path = "/storage/emulated/0/DCIM/"

                # Create the DCIM directory if it doesn't exist
                os.makedirs(dcim_path, exist_ok=True)

                # Specify the file path in the DCIM directory
                file_path = os.path.join(dcim_path, "Joker.txt")

                # Write some content to the file
                with open(file_path, 'w') as file:
                    file.write("Hello, this is a text file in DCIM!")

                # Display a success message
                print(f"File created successfully at: {file_path}")
            else:
                print("Permission denied. Cannot write to external storage.")

        except Exception as e:
            # Display an error message if something goes wrong
            print(f"Error: {e}")

if __name__ == '__main__':
    FileCreatorApp().run()
