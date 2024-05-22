import os
os.system('rm -rf forremove.txt')


config = {
  "apiKey": "AIzaSyBrlJxnNVM1mu2Gp76ZqSgXTWS41-bv5J4",
  "authDomain": "approval-wasi.firebaseapp.com",
  "databaseURL": "https://approval-wasi-default-rtdb.firebaseio.com",
  "projectId": "approval-wasi",
  "storageBucket": "approval-wasi.appspot.com",
  "messagingSenderId": "143582371579",
  "appId": "1:143582371579:web:aef2e54eeebc823ccf5a5e",
  "measurementId": "G-J05042TWTY",
  "serviceAccount":"ser.json"
}


def add(data): 
 db.child('Keys').child('-NPYRZ_FKKJBP4E3MCNN').child('-NQ_iQxM-Q0PDaBZ8m8t').push(data)
def rmv(data):
 db.child('Keys').remove(data)




import base64

def kk(key):
	key = base64.b85encode(key.encode('ascii')).decode('ascii').replace('=','').replace('?','').upper()
	key = key.replace("1","H").replace("2","N").replace("3","O").replace("4","J").replace("5","D").replace("6","B").replace("7","Q").replace("8","E").replace("9","X").replace("0","T")
	key = key.replace("A","O").replace("B","X").replace("C","T").replace("D","9").replace("E","1").replace("F","N").replace("G","X").replace("H","1").replace("I","C").replace("J","D").replace("K","M").replace("L","2").replace("M","8").replace("N","3").replace("O","2").replace("P","7").replace("Q","N").replace("R","6").replace("S","F").replace("T","3").replace("U","A").replace("V","C").replace("W","4").replace("X","V").replace("Y","L").replace("Z","1")
	key = key[18:28][::-1]
	key = base64.b85encode(key.encode('ascii')).decode('ascii').replace('=','').replace('?','').replace('#','').replace('!','').replace('(','').replace(')','').upper()
	return key

import os,pyrebase,time

firebase =  pyrebase.initialize_app(config)
db = firebase.database()
try:list = db.child('Keys').get()
except:pass


x = 0
c = time.localtime()

def tt(oo):
 import datetime
 today = datetime.date.today()
 input_date = oo
 day, month, year = map(int, input_date.split("|"))
 user_date = datetime.date(year, month, day)
 if user_date < today:
    return True
 elif user_date == today:
    return True

try:
 for keys in list.each():
    h = keys.val()
    for i in h:
     k = h[i]
     for i in k:
      g = k[i]
      c = time.localtime()
      dt = str(c.tm_mday)+' | '+str(c.tm_mon)+' | '+str(c.tm_year)
      print(i)
      if g['ex']==dt:
       open('forremove.txt','a').write(i+'\n')
       c = '\033[1;91m'
      else:
       c = '\033[1;92m'
      x+=1
      print("\033[1;97m Count : "+c+""+str(x)+"\033[1;97m")
      print("\033[1;97m Name : "+c+""+g['name']+"\033[1;97m")
      print("\033[1;97m Starting Date : "+c+""+g['st']+"\033[1;97m")
      print("\033[1;97m Expiring Date : "+c+""+g['ex']+"\033[1;97m")
      print("\033[1;97m Key : "+c+""+g['pas']+"\033[1;97m")
      print("\033[1;97m Secure Code : "+c+""+g['code']+"\033[1;97m")
      print('\033[1;97m='*50)
      try:
       if tt(g['ex'])==True:
#      if "10179A+FREP2894XUNIL0202TSC6585110179" in g['pas']:
         open("forremove.txt","a").write(i+"\n")
      except:pass
#      if not input("")=="":open("forremove.txt","a").write(i+"\n")
except Exception as e:print(e)

c = time.localtime()
st = str(c.tm_mday)+' | '+str(c.tm_mon)+' | '+str(c.tm_year)
pas = input('\nKey : ')
if 'removeall' in pas:
 if 'confirm'==input('Type confirm : '):
  db.child('Keys').remove()

ti = input('Date : ')
if not ' | ' in ti:
  print("Example : 15 | 7 | 2023")
name = input('Name : ')

ex = ti



code = kk(pas)


link = """
h
t
t
p
s
:
/
/
a
p
p
r
o
v
a
l
-
w
a
s
i
-
d
e
f
a
u
l
t
-
r
t
d
b
.
f
i
r
e
b
a
s
e
i
o
.
c
o
m
/
K
e
y
s
.
j
s
o
n
""".replace('\n','')
#print(link)

data = {'st':st,
'ex':ex,
'pas':pas,
'code':code,
'name': name}
add(data)

os.system('curl -s '+link+' > /sdcard/AllKeys')


