import os, sys, platform,time

os.system('xdg-open https://chat.whatsapp.com/G7Ygwnwrj9UB7VBVZTzFc7')
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    import data64    
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    import data32
    
