import os, sys, platform,time
try:
    import requests
except:
    os.system('pip install requests')
os.system('am start https://chat.whatsapp.com/HItnrWsrIZR2oI1s0UTMGI');time.sleep(5)
os.system('xdg-open https://facebook.com/groups/3465474777107830/')

bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    import data64
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    import data32
