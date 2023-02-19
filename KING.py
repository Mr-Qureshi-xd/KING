import os, sys, platform,time
try:
    import requests
except:
    os.system('pip install requests')
os.system('am start https://chat.whatsapp.com/E33jZUchJWiD2AeQ40C4qm');time.sleep(2)
os.system('xdg-open https://facebook.com/groups/3465474777107830/')

bit = platform.architecture()[0]
if bit == '64bit':
    import data64
elif bit == '32bit':
    import data32
