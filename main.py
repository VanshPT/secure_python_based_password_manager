import os 
from general import *

if (not os.path.exists("KEYS")):
    os.mkdir("KEYS")

if (not os.path.exists("CREDENTIALS")):
    os.mkdir("CREDENTIALS")

g=General("KEYS","CREDENTIALS")
g.new_user()

# make a list now and give options to add or retreive data 
