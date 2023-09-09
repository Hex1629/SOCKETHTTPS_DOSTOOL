import requests
import os,sys
import random
import threading
import platform
from data import HumanBytes
c = __file__
path = ''
if platform.system().upper() == 'WINDOWS':
 path = '\\'
else:
 path = '/'

FILES = ''
SETTING_RE = 0

file_lock = threading.Lock()

WEBSITE = []

data2 = []
try:
    with open(os.path.join(os.path.dirname(c).replace(path+'MODEL', path+'Lst'), FILES), 'r') as f3:
        data2 = f3.readlines()
except:
    pass

def SCANNER(TIMEOUT_SET, MAX_RANDOM):
    global threads,SETTING_RE
    number = 0
    while True:
        number += 1
        IP = f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}'
        try:
            r = requests.get(f'http://{IP}', timeout=TIMEOUT_SET)
            try:
             size = HumanBytes.format(len(r.content.decode()),True)
            except:
             size = HumanBytes.format(len(r.content),True)
            with file_lock:
                WEBSITE.append(f'{IP}')
                print(f"\x1b[38;5;70m[\x1b[38;5;255m{number}\x1b[38;5;70m] \x1b[38;5;64m{IP} \x1b[38;5;255m--> \x1b[38;5;70mFOUND \x1b[38;5;71mSTATUS\x1b[38;5;255m={r.status_code}:{r.reason} \x1b[38;5;72mCONTENT\x1b[38;5;255m={size} . . .\x1b[0m")
        except requests.Timeout:
            print(f"\x1b[38;5;220m[\x1b[38;5;255m{number}\x1b[38;5;220m] \x1b[38;5;226m{IP} \x1b[38;5;255m--> \x1b[38;5;220mTIMEOUT \x1b[38;5;221mSTATUS\x1b[38;5;255m=FAILED \x1b[38;5;221mCONTENT\x1b[38;5;255m=-- B . . .\x1b[0m")
        except requests.RequestException as e:
            print(f'\x1b[38;5;196m[\x1b[38;5;255m{number}\x1b[38;5;196m] \x1b[38;5;196m{IP} \x1b[38;5;255m--> \x1b[38;5;196mERROR \x1b[38;5;197mSTATUS=\x1b[38;5;255mFAILED \x1b[38;5;198mCONTENT=\x1b[38;5;255m-- B . . .\x1b[0m')
        if number == MAX_RANDOM:
            break

    with file_lock:
        with open(os.path.join(os.path.dirname(c).replace('\MODEL', '\Lst'), FILES), 'a') as f:
            for I in WEBSITE:
                if I not in data2:
                    f.write(f'{I}\n')
                    data2.append(I)
    if SETTING_RE == 1:
     thread = threading.Thread(target=SCANNER, args=(TIMEOUT_SET, MAX_RANDOM))
     thread.start()

TIMEOUT_SET = 0
MAX_RANDOM = 0
THREAD_TIME = 0
if len(sys.argv) == 5:
 TIMEOUT_SET = int(sys.argv[1])
 MAX_RANDOM = int(sys.argv[2])
 THREAD_TIME = int(sys.argv[3])
 FILES = str(sys.argv[4])
elif len(sys.argv) == 6:
 TIMEOUT_SET = int(sys.argv[1])
 MAX_RANDOM = int(sys.argv[2])
 THREAD_TIME = int(sys.argv[3])
 FILES = str(sys.argv[4])
 SETTING_RE = int(sys.argv[5])
 if SETTING_RE != 1 and SETTING_RE != 0:
  print(f"{sys.argv[0]} \x1b[38;5;196m<\x1b[38;5;255mTIMEOUT\x1b[38;5;196m> \x1b[38;5;196m<\x1b[38;5;225mIP PER THREAD\x1b[38;5;196m> \x1b[38;5;196m<\x1b[38;5;225mTHREAD\x1b[38;5;196m> \x1b[38;5;196m<\x1b[38;5;225mFILE\x1b[38;5;196m> \x1b[38;5;196m<\x1b[38;5;225m1 OR 0\x1b[38;5;196m>\x1b[0m")
  exit()
else:
 print(f"{sys.argv[0]} \x1b[38;5;196m<\x1b[38;5;255mTIMEOUT\x1b[38;5;196m> \x1b[38;5;196m<\x1b[38;5;225mIP PER THREAD\x1b[38;5;196m> \x1b[38;5;196m<\x1b[38;5;225mTHREAD\x1b[38;5;196m> \x1b[38;5;196m<\x1b[38;5;225mFILE\x1b[38;5;196m>\x1b[0m")

def scanners_thread(THREAD_TIME,TIMEOUT_SET,MAX_RANDOM):
 threads = []
 for _ in range(THREAD_TIME):
    thread = threading.Thread(target=SCANNER, args=(TIMEOUT_SET, MAX_RANDOM))
    thread.start()
    threads.append(thread)

 for thread in threads:
    thread.join()

threading.Thread(target=scanners_thread,args=(THREAD_TIME,TIMEOUT_SET,MAX_RANDOM)).start()