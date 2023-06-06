import os
from cryptography.fernet import Fernet
import subprocess

class General:
    def __init__(self, k, c):
        self.k = k
        self.c = c

    def new_user(self):
        keys = os.listdir(self.k)
        credentials = os.listdir(self.c)
        if (len(keys) == 0) and (len(credentials) == 0):
            dpass = input("As you are a first-time user, enter a security password to access or store all your credentials(WARNING!!!Keep your main password atleast 8 characters long and it should contain mix of alphanumeric and special characters) : ")
            pkey = Fernet.generate_key()
            fernet = Fernet(pkey)
            epass = fernet.encrypt(dpass.encode())

            with open(os.path.join(self.k, "pass.key"), "wb") as key_file:
                key_file.write(pkey)

            with open("password.txt", "w") as pass_file:
                pass_file.write(epass.decode())
        # testing
        # with open(os.path.join(self.k, "pass.key"),"rb") as key_file:
        #     pkey=key_file.read()

        # with open("password.txt", "r") as pass_file:
        #     password=pass_file.read()
        

        # fernet=Fernet(pkey)
        # dpas=fernet.decrypt(password)
        # print(dpas.decode())



    def new_credentials(self):
        # the below 6 lines will clear the terminal for a fresh look while working.
        # Define the command to clear the terminal based on the operating system
        # clear_command = "clear"  # for Unix/Linux
        clear_command = "cls"  # for Windows

        # Execute the clear command
        subprocess.call(clear_command, shell=True)


        pass#write code for accepting new credentials from user and storing it in credentials directory in encrypted format.

    def get_credentials(self):
        # the below 6 lines will clear the terminal for a fresh look while working.
        # Define the command to clear the terminal based on the operating system
        # clear_command = "clear"  # for Unix/Linux
        clear_command = "cls"  # for Windows

        # Execute the clear command
        subprocess.call(clear_command, shell=True)


        pass#write code displaying required credentials asked by the user into plain text.

    def change_password(self):
        # the below 6 lines will clear the terminal for a fresh look while working.
        # Define the command to clear the terminal based on the operating system
        # clear_command = "clear"  # for Unix/Linux
        clear_command = "cls"  # for Windows

        # Execute the clear command
        subprocess.call(clear_command, shell=True)


        pass#write code for changing the main password.




