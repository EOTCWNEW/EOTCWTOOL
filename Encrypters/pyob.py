import os
import sys
import time
import base64
import zlib
import marshal
import pyarmor

W = '\033[37m' #Information/About/Tuts
R = '\033[31m' #Aggressive/Alert/Caution/Warning/Failed/
B = '\033[34m' #Normal/Questioning/
G = '\033[1;32m' #Process Completed/Success/
Y = '\033[33m' #On Process/Processing/Executing/Deploying/

def banner(text):
    colors = [
        "\033[38;2;255;255;0m",  # Yellow
        "\033[38;2;255;200;0m",  # Orange-Yellow
        "\033[38;2;255;165;0m",  # Orange
        "\033[38;2;255;100;0m",  # Deep Orange
        "\033[38;2;255;50;0m",   # Reddish-Orange
        "\033[38;2;255;0;0m"     # Red
    ]

    lines = text.split("\n")
    num_lines = len(lines)

    for i, line in enumerate(lines):
        color = colors[int((i / num_lines) * (len(colors) - 1))]  # Gradient selection
        print(color + line + "\033[0m")  # Reset color after each line

ascii_art = r"""
        ##### ##         ##### /    ##      # ###        ##### ##
     ######  /###     ######  /  #####    /  /###     ######  /##
    /#   /  /  ###   /#   /  /     ##### /  /  ###   /#   /  / ##
   /    /  /    ### /    /  ##     # ## /  ##   ### /    /  /  ##
       /  /      ##     /  ###     #   /  ###    ###    /  /   /
      ## ##      ##    ##   ##     #  ##   ##     ##   ## ##  /
      ## ##      ##    ##   ##     #  ##   ##     ##   ## ## /
    /### ##      /     ##   ##     #  ##   ##     ##   ## ##/
   / ### ##     /      ##   ##     #  ##   ##     ##   ## ## ###
      ## ######/       ##   ##     #  ##   ##     ##   ## ##   ###
      ## ######         ##  ##     #   ##  ##     ##   #  ##     ##
      ## ##              ## #      #    ## #      /       /      ##
      ## ##               ###      #     ###     /    /##/     ###
      ## ##                #########      ######/    /  ########
 ##   ## ##                  #### ###       ###     /     ####
###   #  /                         ###              #
 ###    /              ########     ###              ##
  #####/             /############  /#
    ###             /           ####/

"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    banner(ascii_art)
    print ("\033[38;2;255;0;0mCoded by UnKnown\033[0m")
    print ("\033[38;2;255;0;0mEOTCW PYTHON OBFUSCATOR V.1\033[0m")
    print ("\033[38;2;255;0;0m[USAGE]: put something like this below '/path/path/example/directory/yourfile.py'\033[0m")
    print (" ")
    print (" ")
    file = input(f"{B}Enter the file/filepath you want to encrypt: ")
    if os.path.isfile(file):
        print (" ")
        found = f"{G}[+]SUCCESS! PYTHON FILE IS FOUND!!!"
        for char in found:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
    else:
        print ("\033[38;2;255;0;0m[!]ERROR: 404 file not found! Check if you have a typo!")
        time.sleep(2)
        main()
    time.sleep(0.05)
    print (f"""{B}

    Obfuscation Types:{W}
        1.  Compile.                                         
        2.  b85.                                             
        3.  b64.                                             
        4.  b32.                                             
        5.  b16.                                             
        6.  b64 urlsafe.                                     
        7.  b32 hex encode.                                  
        8.  a85.                                             
        9.  z85.                                             
        10. b85 w/ b.                                        
        11. b85 reversed.                                    
        12. b85 & b64.                                       
        13. b85 & b32.                                       
        14. b85 & b16.                                       
        15. b85 & b64 urlsafe.                               
        16. b85 & b32 hex encode.                            
        17. b85 & a85.                                       
        18. b85 & z85.                                       
        19. b85 w/ b & reversed.                             
        20. b85 & b64 w/ b.                                  
        21. b85 & b32 w/ b.                                  
        22. b85 & b16 w/ b.                                  
        23. b85 & b64 urlsafe w/ b.                          
        24. b85 & b32 hex encode w/ b.                       
        25. b85 & a85 w/ b.                                  
        26. b85 & z85 w/ b.                                  
        27. b85 & b64 reversed.                              
        28. b85 & b32 reversed.                              
        29. b85 & b16 reversed.                              
        30. b85 & b64 urlsafe reversed.                      
        31. b85 & b32 hex encode reversed.                   
        32. b85 & a85 reversed.                              
        33. b85 & z85 reversed.                              
        34. b85 & b64 w/ b + reversed.                       
        35. b85 & b32 w/ b + reversed.                       
        36. b85 & b16 w/ b + reversed.                       
        37. b85 & b64 urlsafe w/ b + reversed.               
        38. b85 & b32 hex encode w/ b + reversed.            
        39. b85 & a85 w/ b + reversed.                       
        40. b85 & z85 w/ b + reversed.                       
        41. b64 w/ b.                                        
        42. b64 reversed.                                    
        43. b64 & b85.                                       
        44. b64 & b32.                                       
        45. b64 & b16.                                       
        46. b64 & b64 urlsafe.                               
        47. b64 & b32 hex encode.                            
        48. b64 & a85.                                       
        49. b64 & z85.                                       
        50. b64 w/ b & reversed.                             
        51. b64 & b85 w/ b.                                  
        52. b64 & b32 w/ b.                                  
        53. b64 & b16 w/ b.                                  
        54. b64 & b64 urlsafe w/ b.                          
        55. b64 & b32 hex encode w/ b.                       
        56. b64 & a85 w/ b.                                  
        57. b64 & z85 w/ b.                                  
        58. b64 & b85 reversed.                              
        59. b64 & b32 reversed.                              
        60. b64 & b16 reversed.                              
        61. b64 & b64 urlsafe reversed.                      
        62. b64 & b32 hex encode reversed.                   
        63. b64 & a85 reversed.                              
        64. b64 & z85 reversed.                              
        65. b64 & b85 w/ b + reversed.                       
        66. b64 & b32 w/ b + reversed.                       
        67. b64 & b16 w/ b + reversed.                       
        68. b64 & b64 urlsafe w/ b + reversed.               
        69. b64 & b32 hex encode w/ b + reversed.            
        70. b64 & a85 w/ b + reversed.                       
        71. b64 & z85 w/ b + reversed.                       
        72. b32 w/ b.
        73. b32 reversed.
        74. b32 & b85.
        75. b32 & b64.
        76. b32 & b16.
        77. b32 & b64 urlsafe.
        78. b32 & b32 hex encode.
        79. b32 & a85.
        80. b32 & z85.
        81. b32 w/ b & reversed.
        82. b32 & b85 w/ b.
        83. b32 & b64 w/ b.
        84. b32 & b16 w/ b.
        85. b32 & b64 urlsafe w/ b.
        86. b32 & b32 hex encode w/ b.
        87. b32 & a85 w/ b.
        88. b32 & z85 w/ b.
        89. b32 & b85 reversed.
        90. b32 & b64 reversed.
        91. b32 & b16 reversed.
        92. b32 & b64 urlsafe reversed.
        93. b32 & b32 hex encode reversed.
        94. b32 & a85 reversed.
        95. b32 & z85 reversed.
        96. b32 & b85 w/ b + reversed.
        97. b32 & b64 w/ b + reversed.
        98. b32 & b16 w/ b + reversed.
        99. b32 & b64 urlsafe w/ b + reversed.
        100. b32 & b32 hex encode w/ b + reversed.
        101. b32 & a85 w/ b + reversed.
        102. b32 & z85 w/ b + reversed.
        103. b16 w/ b.
        104. b16 reversed.
        105. b16 & b85.
        106. b16 & b64.
        107. b16 & b32.
        108. b16 & b64 urlsafe.
        109. b16 & b32 hex encode.
        110. b16 & a85.
        111. b16 & z85.
        112. b16 w/ b & reversed.
        113. b16 & b85 w/ b.
        114. b16 & b64 w/ b.
        115. b16 & b32 w/ b.
        116. b16 & b64 urlsafe w/ b.
        117. b16 & b32 hex encode w/ b.
        118. b16 & a85 w/ b.
        119. b16 & z85 w/ b.
        120. b16 & b85 reversed.
        121. b16 & b64 reversed.
        122. b16 & b32 reversed.
        123. b16 & b64 urlsafe reversed.
        124. b16 & b32 hex encode reversed.
        125. b16 & a85 reversed.
        126. b16 & z85 reversed.
        127. b16 & b85 w/ b + reversed.
        128. b16 & b64 w/ b + reversed.
        129. b16 & b32 w/ b + reversed.
        130. b16 & b64 urlsafe w/ b + reversed.
        131. b16 & b32 hex encode w/ b + reversed.
        132. b16 & a85 w/ b + reversed.
        133. b16 & z85 w/ b + reversed.

    """)

    choice = input(f"{B}Pick your obfuscation choice: ")

    if choice == "1":
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        os.system(f"python3 -m py_compile {file}")
        print (" ")
        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED in __pycache__")
        ask()

    elif choice == "2":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

	[1-100] LOW
        [101-500] DECRYPTABLE
	[501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode('{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "3":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode('{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "4":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode('{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "5":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode('{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "6":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.urlsafe_b64encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode('{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "7":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32hexencode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode('{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "8":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.a85encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode('{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "9":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.z85encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode('{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "10":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(b'{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "11":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(zlib.compress(data)[::-1]).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode('{obs}')[::-1]));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "12":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b85decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "13":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b32encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b85decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "14":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b16encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b85decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "15":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.urlsafe_b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b85decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "16":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b32hexencode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b85decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "17":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.a85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b85decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "18":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.z85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b85decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "19":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(zlib.compress(data)[::-1]).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(b'{obs}')[::-1]));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "20":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b85decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "21":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b32encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b85decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "22":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b16encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b85decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "23":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.urlsafe_b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b85decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "24":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b32hexencode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b85decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "25":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.a85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b85decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "26":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.z85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b85decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "27":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b85decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "28":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b32encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b85decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "29":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b16encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b85decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "30":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.urlsafe_b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b85decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "31":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b32hexencode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b85decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "32":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.a85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b85decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "33":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.z85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b85decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "34":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b85decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "35":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b32encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b85decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "36":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b16encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b85decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "37":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.urlsafe_b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b85decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "38":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.b32hexencode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b85decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "39":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.a85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b85decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "40":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b85encode(base64.z85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b85decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "41":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(b'{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "42":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(zlib.compress(data)[::-1]).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode('{obs}')[::-1]));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "43":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b64decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "44":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b32encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b64decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "45":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b16encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b64decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "46":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.urlsafe_b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b64decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "47":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b32hexencode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b64decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "48":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.a85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b64decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "49":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.z85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b64decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "50":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(zlib.compress(data)[::-1]).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(b'{obs}')[::-1]));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "51":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b64decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "52":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b32encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b64decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "53":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b16encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b64decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "54":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.urlsafe_b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b64decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "55":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b32hexencode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b64decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "56":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.a85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b64decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "57":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.z85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b85decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "58":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b64decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "59":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b32encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b64decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "60":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b16encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b64decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "61":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.urlsafe_b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b64decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "62":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b32hexencode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b64decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "63":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.a85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b64decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "64":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.z85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b64decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "65":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b64decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "66":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b32encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b64decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "67":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b16encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b64decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "68":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.urlsafe_b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b64decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "69":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.b32hexencode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b64decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "70":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.a85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b64decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "71":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b64encode(base64.z85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b64decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "72":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(b'{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "73":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(zlib.compress(data)[::-1]).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode('{obs}')[::-1]));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "74":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b32decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "75":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b32decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "76":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b16encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b32decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "77":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.urlsafe_b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b32decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "78":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b32hexencode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b32decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "79":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.a85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b32decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "80":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.z85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b32decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "81":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(zlib.compress(data)[::-1]).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(b'{obs}')[::-1]));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "82":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b32decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "83":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b32decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "84":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b16encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b32decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "85":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.urlsafe_b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b32decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "86":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b32hexencode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b32decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "87":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.a85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b32decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "88":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.z85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b32decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "89":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b32decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "90":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b32decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "91":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b16encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b32decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "92":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.urlsafe_b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b32decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "93":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b32hexencode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b32decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "94":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.a85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b32decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "95":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.z85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b64decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "96":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b32decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "97":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b32decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "98":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b16encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__import__('base64').b32decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "99":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.urlsafe_b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b32decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "100":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.b32hexencode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b32decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "101":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.a85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b32decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "102":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b32encode(base64.z85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b32decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "103":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(zlib.compress(data)).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(b'{obs}')));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "104":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(zlib.compress(data)[::-1]).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode('{obs}')[::-1]));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "105":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b16decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "106":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b16decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "107":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b32encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b16decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "108":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.urlsafe_b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b16decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "109":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b32hexencode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b16decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "110":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.a85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b16decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "111":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.z85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b16decode('{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "112":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(zlib.compress(data)[::-1]).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(b'{obs}')[::-1]));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "113":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b16decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "114":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b16decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "115":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b32encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b16decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "116":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.urlsafe_b64encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b16decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "117":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b32hexencode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b16decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "118":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.a85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b16decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "119":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.z85encode(zlib.compress(data))).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b16decode(b'{obs}'))));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "120":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b16decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "121":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b16decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "122":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b32encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b16decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "123":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.urlsafe_b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b16decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "124":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b32hexencode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b16decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "125":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.a85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b16decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "126":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.z85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b16decode('{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "127":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__import__('base64').b16decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "128":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__import__('base64').b16decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "129":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b32encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__import__('base64').b16decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "130":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.urlsafe_b64encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').urlsafe_b64decode(__import__('base64').b16decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "131":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.b32hexencode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32hexdecode(__import__('base64').b16decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "132":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.a85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').a85decode(__import__('base64').b16decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

    elif choice == "133":
        outfile = input(f"{B}Enter your desired obfuscated file name: ")
        strength = int(input(f"""{B}

Strength Levels:

        [1-100] LOW
        [101-500] DECRYPTABLE
        [501-1000] SECURED
        [1000-10000] HIGHLY SECURED
        [10000-99999] EXTREME
        [100000-INFINITE] SUPER STRONG BUT SLOW TO FINISH OBFUSCATE

[ USAGE ]: Enter a number below without comma and dont use chars for example "10k" or "1m"

.
Amount of Strength: """))
        message = f"{Y}[*]Obfuscating..... \n"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()
        for i in range(1,strength):
            data = marshal.dumps(code)
            obs = base64.b16encode(base64.z85encode(zlib.compress(data)[::-1])).decode('utf-8')
            obfuscated_code = f"_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').z85decode(__import__('base64').b16decode(b'{obs}')[::-1])));exec(_(_))"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print (f"{G}[+]SUCCESS! YOUR PYTHON CODE IS SUCCESSFULLY OBFUSCATED AND SAVED TO {outfile} :)")
        ask()

def ask():
    ans = input(f"{B}Do you want to go back to menu?(y/n): ")
    if ans in ["Y","y","YES","Yes","yes"]:
        main()
    else:
        print (" ")
        alert = f"{R}Exiting..... "
        for char in alert:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(2)
        exit()

main()
