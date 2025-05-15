import os
import requests

url = "https://app.codeconvert.ai/api/convert-code"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
  print ("""

 #####################################################
 #                ##                ####   #####   ###
 #############   #   ###########   ###   ######   ####
 ############   #   ############   ##   ########   ###
 ###########   #   #############   #   ########   ####
 ####   ####   #   #####   ######      ######   ######
 #####   ###   #       #   #######     ####   ########
 #####   ##   ####   ##   ########    ###   ##########
 ######   #   ###   ###                    ###########
 #######      ##   ####   #############   ############
 #########     #   #####   ############   ############
 ##########       ######   ###########   #############
 ###########     #######   ##########   ##############
 ###########   ########   #########   ################
 ########## #########   ########   ###################
 #####################################################
 #                                                   #
 #              [( TOOL INFORMATION )]               #
 #                                                   #
 # AUTHOR:UnKnown                                    #
 # TOOL_NAME: JSPY....                               #
 # PURPOSE: CONVERTS JS CODE INTO PYTHON             #
 #                                                   #
 #####################################################

""")

def main():
  conv = {
    "inputLang":"JavaScript",
    "outputLang":"Python",
    "inputCode": jscode,
    "customInstructions":"",
    "isReferenceFilesEnabled":"false"
  }
  response = requests.post(url, json = conv)
  print (response.text)

if __name__ == '__main__':
  clear()
  banner()
  filename = input("Place the pathfile of your jscode here: ")

  if os.path.isfile(filename):
    with open(filename, "rb") as jsfile:
      jscode = jsfile.read().decode("utf-8")
    main()

  else:
    print("[FATAL ERROR]: File not found! please check for typos.")
    exit()
