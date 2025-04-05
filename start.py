import os
import sys
import time
import math
import colorama

members = ['ZEROTWO','ZERO','Z3R0TW0','Z3R0','z3r0tw0','z3r0','zerotwo','zero','Zerotwo','Zero','Z3r0tw0','Zerotwo','ZeroTwo','Z3r0Tw0','PhantomX','Ph4nt0mX','phantomX','ph4nt0mX','Mr.Cl4y','Mr.Clay','mr.cl4y','mr.clay','Sh1su1','sh1su1','shisui','Shisui','SH1SU1','SHISUI','cutie']
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
commands = f'''

{B}[--------LIST OF COMMANDS IN EYE TERMINAL--------]{rc}


• {G}about{rc} >>> know the org.
• {Y}chatroom{rc} >>> EOTCW chatroom {Y}[🔒coming soon!]{rc}.
• {G}dox{rc} >>> view or add someone to your d0xxed list.
• {G}exit{rc} >>> leave the eye terminal.
• {G}hacked{rc} >>> view or add something to your hacked list.
• {G}learn{rc} >>> view tutorial files to learn.
• {G}mal{rc} >>> malware samples (text-only).
• {R}Mr.KasakiX{rc} >>> special tools {R}(🔐authorized person only){rc}.
• {G}pics{rc} >>> see picture files.
• {G}play{rc} >>> play hacker games.
• {Y}surf{rc} >>> browse using your terminal {Y}[🔒coming soon!]{rc}.
• {G}tools{rc} >>> show list of tools.
• {Y}unkmode{rc} >>> use ip changer {Y}[🔒coming soon!]{rc}.

'''
maltextfilename = f'''

{R}[-------LIST OF MALWARE SAMPLES-------]{W}


• infohook1 {G}[low]{W}
• infohook2 {G}[low]{W}
• lockforever {O}[CRITICAL]{W}
• trojaneye {DO}[DESTRUCTIVE]{W}
• UnKware {R}[HIGHLY DESTRUCTIVE]{W}

'''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    os.system("cd && cd EOTCW/pics && jp2a EOTCWLOGO.jpeg --colors")
    message = f"{B}EOTCW AI[</>]: to use, type HELP or help to view commands. have fun and enjoy!(>_•){rc}"
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1.5)
    clear()

def banner():
    os.system("cd && cd EOTCW/pics && jp2a EOTCWLOGO.jpeg --colors")
    if name in ['UnK','UnKnown','3xp053','Mr.KasakiX']:
        print (f"{B}EYE OF THE CYBER WORLD..... Welcome {name}[FOUNDER]!")
        print (f"{B}[(USAGE)]: type HELP or help to view commands. :)")
        print (" ")
        print (" ")
    elif name in ['H4SHP4P1','HASHPAPI','hashpapi','Hashpapi','h4shp4p1','H4shp4p1']:
        print (f"{B}EYE OF THE CYBER WORLD..... Welcome {name}[CO-FOUNDER]!")
        print (f"{B}[(USAGE)]: type HELP or help to view commands. :)")
        print (" ")
        print (" ")
    elif name in members:
        print (f"{B}EYE OF THE CYBER WORLD..... Welcome {name}!")
        print (f"{B}[(USAGE)]: type HELP or help to view commands. :)")
        print (" ")
        print (" ")

def progress_bar(color=colorama.Fore.BLUE):
    numbers = [x * 5 for x in range(0, 1100)]
    results = []
    message = f"{B}Entering.....{rc}\n"
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    for i, x in enumerate(numbers):
        results.append(math.factorial(x))
        progress = i + 1
        total = len(numbers)
        percent = 100 * (progress / float(total))
        bar = '█' * int(percent) + '-' * (100 - int(percent))
        print (color + f"\r|{bar}| {percent:.2f}%", end="\r")
        if progress == total:
            clear()
            print (colorama.Fore.GREEN + "SUCCESS!")
            print (colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")

    print (colorama.Fore.RESET)
    time.sleep(1)

def main():
    if name in ['UnK','UnKnown','3xp053','Mr.KasakiX']:
        commandline = input(f'''{Y}┌─{OY}─{O}({W}{name}{DO}㉿{B}eye{RO})-{R}[FOUNDER]
{Y}└{OY}─{O}${rc} ''')
    elif name in ['H4SHP4P1','HASHPAPI','hashpapi','Hashpapi','h4shp4p1','H4shp4p1']:
        commandline = input(f'''{Y}┌─{OY}─{O}({W}{name}{DO}㉿{B}eye{RO})-{R}[CO-FOUNDER]
{Y}└{OY}─{O}${rc} ''')
    else:
        commandline = input(f'''{Y}┌─{OY}─{O}({W}{name}{DO}㉿{B}eye{RO})-{R}[<©>]
{Y}└{OY}─{O}${rc} ''')
    if commandline == "help" or commandline == "HELP":
        print (commands)
        main()
    elif commandline == "about":
        os.system("cd && cd EOTCW && cat .about.txt")
        main()
    elif commandline == "chatroom":
        print("coming soon!")
        main()
    elif commandline == "dox":
        os.system("cd && cd EOTCW && chmod +x DOX && ./DOX")
        main()
    elif commandline == "exit":
        message = f"{B}EOTCW AI[</>]: Thank you so much! see you again! bye!(◉⁠‿⁠◉)/\n{rc}"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        print(f"{R}exiting..... ")
        time.sleep(2)
        exit()
    elif commandline == "hacked":
        os.system("cd && cd EOTCW && chmod +x HACKED && ./HACKED")
        main()
    elif commandline == "learn":
        os.system("cd && cd EOTCW/tuts && ls")
        learnfile = input("pick a tutorial file to open and learn: ")
        if "." not in learnfile:
           print("ERROR: please add the file extension too!")
           main()
        else:
           os.system("cd && cd EOTCW/tuts && xdg-open {file}")
           main()
    elif commandline == "mal":
        os.system("cd && cd EOTCW/Malwares && ls")
        print(maltextfilename)
        main()
    elif commandline == "Mr.KasakiX":
        os.system("cd && cd EOTCW/Mr.KasakiX && chmod +x START && ./START")
        main()
    elif commandline == "pics":
        os.system("cd && cd EOTCW/pics && ls")
        main()
    elif commandline == "play":
        os.system("cd && cd EOTCW/games && python game.py")
        main()
    elif commandline == "surf":
        print("coming soon")
        main()
    elif commandline == "tools":
        print("currently in development")
        main()
    elif commandline == "unkmode":
        print("coming soon")
        main()
    else:
        print("INVALID COMMAND! TYPE HELP TO SEE ALL COMMANDS!")
        main()

if __name__ == '__main__':
    name = input(f"""{B}EOTCW AI[</>]: Who are you?{rc}

{W}ENTER YOUR CODENAME:{rc} """)
    if name in ['UnK','UnKnown','3xp053','Mr.KasakiX']:
        clear()
        print (f"""{B}
EOTCW AI[</>]: Who are you?
{W}YOU: {name}""")
        time.sleep(0.5)
        print (f"{B}EOTCW AI[</>]: Welcome my master, {name}(FOUNDER)!{rc}")
        time.sleep(1)
        clear()
        progress_bar()
        clear()
        intro()
        banner()
        main()

    elif name in ['H4SHP4P1','HASHPAPI','hashpapi','Hashpapi','h4shp4p1','H4shp4p1']:
        clear()
        print (f"""{B}
EOTCW AI[</>]: Who are you?
{W}YOU: {name}""")
        time.sleep(0.5)
        print (f"{B}EOTCW AI[</>]: Welcome my master, {name}(CO-FOUNDER)!{rc}")
        time.sleep(1)
        clear()
        progress_bar()
        clear()
        intro()
        banner()
        main()

    elif name in members:
        clear()
        print (f"""{B}
EOTCW AI[</>]: Who are you?
{W}YOU: {name}""")
        time.sleep(0.5)
        print (f"{B}EOTCW AI[</>]: Welcome, {name}!{rc}")
        time.sleep(1)
        clear()
        progress_bar()
        clear()
        intro()
        banner()
        main()

    else:
        clear()
        print (f"""{B}
EOTCW AI[</>]: Who are you?
{W}YOU: {name}""")
        time.sleep(0.5)
        print (f"{B}EOTCW AI[</>]: FORBIDDEN(403)! WE DON'T KNOW YOU! GET OUT!(>_<){rc}")
        time.sleep(1)
        exit()
