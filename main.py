import os 
import subprocess
from general import *

if (not os.path.exists("KEYS")):
    os.mkdir("KEYS")

if (not os.path.exists("CREDENTIALS")):
    os.mkdir("CREDENTIALS")

g=General("KEYS","CREDENTIALS")
g.new_user()#this method will not do anything if you have used password manager before. this will ask for a secure password for your whole password manager if and only if we are using this password manager for the first time.

# the below 6 lines will clear the terminal for a fresh look while working.
# Define the command to clear the terminal based on the operating system
# clear_command = "clear"  # for Unix/Linux
clear_command = "cls"  # for Windows

# Execute the clear command
subprocess.call(clear_command, shell=True)

while(True):
    ch=int(input("Enter your choice(0-4)\n0<--Exit\n1<-- Enter new credentials\n2<-- Get credentials\n3<-- Change Password\n4<-- Delete Credentials\n-->"))
    if(ch==0):
        print("Thank you for using the secure password manager. Be Secure Be Happy :)")
        break
    match ch:
        case 0:
            break
        case 1:
            g.new_credentials()
        case 2:
            g.get_credentials()
            print("\n")
        case 3:
            g.change_password()
        case 4:
            subprocess.call("cls",shell=True)
            print("INSTRUCTION: Delete the file named (your_credentials_key).key from folder KEYS and delete the file named (your_credentials_key).txt from the folder CREDENTIALS.\n\n+++ Total files deleted = 2 +++ \n")
        case _:
            print("Enter a valid Choice!!!\n")
            




