import requests
import os
import sys
import getpass
import time

url = 'https://zen-api.up.railway.app/api/sms'
bbg = '\033[44m' #BLUE BACKGROUND
W = '\033[37m' #Information/About/Tuts
R = '\033[38;2;255;0;0m' #Aggressive/Alert/Caution/Warning/Failed/
B = '\033[34m' #Normal/Questioning/
G = '\033[1;32m' #Process Completed/Success/
Y = '\033[33m' #On Process/Processing/Executing/Deploying/
O = '\033[38;2;255;165;0m' #Orange
OY = '\033[38;2;255;200;0m' #Orage-Yellow
DO = '\033[38;2;255;100;0m' #Deep Orange
RO = '\033[38;2;255;50;0m' #Reddish-Orange
rc = '\033[0m' #RESET COLOR

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    os.system("cd && cd EOTCW/pics && jp2a Mr.KasakiX.png --colors")
    print (f" {bbg}{R}CODED BY: Mr.KasakiX        {rc}")
    print (f" {bbg}{R}SMS SPOOFING TOOL USING APIs{rc}")
    print (f" {bbg}{R}HAVE FUN! :)                {rc}")
    print (" ")

def fixed():
    clear()
    banner()

def main():
    fixed()
    first = f"{B}>>> ENTER YOUR TARGET'S PHONE NUMBER (e.g: 9123456789):"
    for char in first:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    fixed()
    number = input(f"""
{B}>>> ENTER YOUR TARGET'S PHONE NUMBER (e.g: 9123456789):


{Y}TARGET NUMBER:{rc} """)

    if number.isalpha():
        print (f"{R}ERROR: WE ARE ASKING FOR PHONE NUMBER AND NOT LETTER.")
        time.sleep(1)
        main()

    elif number.startswith("+63"):
        print (f"{W}USAGE: ENTER NUMBER THAT STARTS WITH 9 LIKE THE EXAMPLE.")
        time.sleep(1)
        main()

    elif number.startswith("0"):
        print (f"{W}USAGE: ENTER NUMBER THAT STARTS WITH 9 LIKE THE EXAMPLE.")
        time.sleep(1)
        main()

    elif number.startswith("63"):
        print (f"{W}USAGE: ENTER NUMBER THAT STARTS WITH 9 LIKE THE EXAMPLE.")
        time.sleep(1)
        main()

    fixed()

    print (f"{B}TARGET NUMBER:{rc} {number}")

    second = f"{B}>>> ENTER THE MESSAGE YOU WANT TO SEND TO YOUR TARGET: "
    for char in second:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    fixed()

    print (f"{B}TARGET NUMBER:{rc} {number}")

    message = input(f"""
{B}>>> ENTER THE MESSAGE YOU WANT TO SEND TO YOUR TARGET:


{Y}MESSAGE:{rc}
""")

    fixed()

    print (f"{B}TARGET NUMBER:{rc} {number}")

    print (f"""{B}MESSAGE:{rc}
{message}""")

    third = f"{B}>>> ENTER YOUR CODENAME:"
    for char in third:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    fixed()

    print (f"{B}TARGET NUMBER:{rc} {number}")

    print (f"""{B}MESSAGE:{rc}
{message}
""")
    time.sleep(0.5)
    print (f"{W}NOTE: DON'T ENTER YOUR REALNAME BELOW!!!{rc}")
    time.sleep(0.5)
    sender = input(f"""
{B}>>> ENTER YOUR CODENAME:


{Y}CODENAME:{rc} """)
    fixed()

    print (f"{B}TARGET NUMBER:{rc} {number}")

    print (f"""MESSAGE:
{message}""")
    print (f"CODENAME: {sender}")
    print (" ")

    finalmessage = f"'{message}' ~{sender}"
    params = {
    'number': number,
    'message': finalmessage
        }

    try:
        final = f"[*]SENDING MESSAGE TO THE NUMBER {number}....\n"

        for char in final:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char == ".":
                time.sleep(0.5)
            else:
                time.sleep(0.05)

        r = requests.get(url, params=params)

        if r.status_code == 200:
            print ("[+]MESSAGE SUCCESSFULLY SENT!!! :)")
            print (" ")
            goback()

        else:
            print(f"[!]Error sending SMS: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"[!]Error sending SMS: {e}")

def goback():
    ans = input("want to go back?(y/n) ")
    if ans in ['y','Y','yes','Yes','YES']:
        print ("please wait.....")
        time.sleep(2)
        main()
    elif ans in ['n','N','no','No','NO']:
        print ("exiting.....")
        time.sleep(2)
        exit()
    else:
        print ("ERROR: PLEASE ANSWER Y OR N")
        time.sleep(1.5)
        goback()

if __name__ == '__main__':
    print ("LOGIN REQUIRED!")
    time.sleep(0.5)
    username = input("USERNAME: ")
    password = getpass.getpass("PASSWORD: ")
    if username == "Mr.KasakiX" and password == "Kupal si UnK":
        print ("LOGIN SUCCESSFULL!!!")
        main()
    else:
        print ("INCORRECT USERNAME OR PASSWORD!!!")
        time.sleep(1)
        exit()
