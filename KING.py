import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/3465474777107830/')

bit = platform.architecture()[0]
if bit == '64bit':
    import data64

elif bit == '32bit':
    import data32
