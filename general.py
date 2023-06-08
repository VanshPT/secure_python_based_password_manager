import os
from cryptography.fernet import Fernet
import subprocess
import getpass

class Security:
    def primary_security(self):
        dpass1=getpass.getpass("Enter the password to proceed: ")
        with open(os.path.join(self.k, "pass.key"), "rb") as key_file:
            pkey=key_file.read()

        with open("password.txt", "r") as pass_file:
                epass=pass_file.read()
        fernet=Fernet(pkey)
        dpass=fernet.decrypt(epass)
        if(dpass1==dpass.decode()):
            return 1
        else:
            return 0
        

class General(Security):
    def __init__(self, k, c):
        self.k = k
        self.c = c

    def new_user(self):
        keys = os.listdir(self.k)
        credentials = os.listdir(self.c)
        if (len(keys) == 0) and (len(credentials) == 0):
            dpass = getpass.getpass("As you are a first-time user, enter a security password to access or store all your credentials(WARNING!!!Keep your main password atleast 8 characters long and it should contain mix of alphanumeric and special characters) : ")
            dpass1=getpass.getpass("Confirm Password: ")
            if(dpass==dpass1):
                pkey = Fernet.generate_key()
                fernet = Fernet(pkey)
                epass = fernet.encrypt(dpass.encode())

                with open(os.path.join(self.k, "pass.key"), "wb") as key_file:
                    key_file.write(pkey)

                with open("password.txt", "w") as pass_file:
                    pass_file.write(epass.decode())
            else:
                print("New password and Confirm Password did not match!!!\n")
        # testing
        with open(os.path.join(self.k, "pass.key"),"rb") as key_file:
            pkey=key_file.read()

        with open("password.txt", "r") as pass_file:
            password=pass_file.read()
        

        fernet=Fernet(pkey)
        dpas=fernet.decrypt(password)
        print(dpas.decode())

    def new_credentials(self):
        # the below 6 lines will clear the terminal for a fresh look while working.
        # Define the command to clear the terminal based on the operating system
        # clear_command = "clear"  # for Unix/Linux
        clear_command = "cls"  # for Windows

        # Execute the clear command
        subprocess.call(clear_command, shell=True)

        result=super().primary_security()
        

        if(result==1):
            print("\n (WARNING:\n!!!IF CREDENTIALS OF ALREADY SAVED CREDENTIALS ARE ENTERED THEN THE OLD CREDENTIALS OF THE RESPECTIVE KEY WILL BE OVERRIDEN!!!)\n")
            dkey=input("Enter the key with which you can search your credentials: ")
            print("\nENTER YOUR CREDENTIALS RESPECTIVE TO KEY BELOW\n")
            dmail=input("Enter Email Id: ")
            dpasswd=input("Enter Password: ")
            key=Fernet.generate_key()
            fernet=Fernet(key)
            dcred=dkey+"\n\n"+"Email: "+dmail+"\n"+"Password: "+dpasswd
            ecred=fernet.encrypt(dcred.encode())

            with open(os.path.join(self.k,f"{dkey}.key"),"wb") as key_file:
                key_file.write(key)
            with open(os.path.join(self.c,f"{dkey}.txt"),"wb") as cred_file:
                cred_file.write(ecred)
            subprocess.call("cls",shell=True)# will show credentials on fresh page
            print("New Credentials Saved!!!\n")

        if(result==0):
            print("\n!!!!!Sorry Wrong Password!!!!!\n\n")
            pass


    def get_credentials(self):
        # the below 6 lines will clear the terminal for a fresh look while working.
        # Define the command to clear the terminal based on the operating system
        # clear_command = "clear"  # for Unix/Linux
        clear_command = "cls"  # for Windows

        # Execute the clear command
        subprocess.call(clear_command, shell=True)

        result=super().primary_security()
        if(result==1):
            dkey=input("Enter the key of the credentials you want(Name of the file storing credentials without extention): ")
            if(f"{dkey}.key" in os.listdir(self.k)):
                with open(os.path.join(self.k,f"{dkey}.key"),"rb") as key_file:
                    key=key_file.read()
                with open(os.path.join(self.c,f"{dkey}.txt"),"rb") as cred_file:
                    ecred=cred_file.read()
                fernet=Fernet(key)
                dcred=fernet.decrypt(ecred)
            else:
                print("\nNo such Key Credentials exists!!!\n")
                return


            subprocess.call("cls",shell=True)# will show credentials on fresh page

            print("(WARNING:\n!!!BELOW ARE YOUR CREDENTIALS. MAKE SURE TO ACCESS AND SEE THESE WHILE ALONE!!!)\n\n")
            print(dcred.decode())

        if(result==0):
            print("\n!!!!!Sorry Wrong Password!!!!!\n\n")
            pass

    def change_password(self):
        # the below 6 lines will clear the terminal for a fresh look while working.
        # Define the command to clear the terminal based on the operating system
        # clear_command = "clear"  # for Unix/Linux
        clear_command = "cls"  # for Windows

        # Execute the clear command
        subprocess.call(clear_command, shell=True)

        result=super().primary_security()
        if(result==1):
            dpass = getpass.getpass("Enter New Password : ")
            dpass1=getpass.getpass("Confirm New Password: ")
            if(dpass==dpass1):
                pkey = Fernet.generate_key()
                fernet = Fernet(pkey)
                epass = fernet.encrypt(dpass.encode())

                with open(os.path.join(self.k, "pass.key"), "wb") as key_file:
                    key_file.write(pkey)

                with open("password.txt", "w") as pass_file:
                    pass_file.write(epass.decode())
                print("!!!Password Updated Successfully!!!")
            else:
                print("New password and Confirm Password did not match!!!\n")            

        if(result==0):
            print("\n!!!!!Sorry Wrong Password!!!!!\n\n")
            pass



