import os, sys, platform,time
os.system('xdg-open https://chat.whatsapp.com/FhDYYIBSxwVI5m3zoaUnH3')
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    import data64    
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    import data32
    
