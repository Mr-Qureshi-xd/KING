import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/3465474777107830/')

bit = platform.architecture()[0]
if bit == '64bit':
    print('tool is off bcause of some security reason wait for a while and don't use any cammands..')
elif bit == '32bit':
    print('tool is off bcause of some security reason wait for a while and don't use any cammands..')
