import js2py
import colorama
import os
import sys
import time

name_translations = {
    'this': 'self',
    'arguments': '*args',
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def make_py_file(python_code, jsfile):
    name = jsfile.replace(".js","")
    with open(f'{name}.py', 'w') as f:
        f.write(python_code)

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print ("Converting.....")
    print (color + f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print (colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")

def ask():
    answer = input(colorama.Fore.BLUE + "Convert again?(Y/N)")
    if answer in ['Y','y','YES','Yes','yes']:
        main()
    elif answer in ['N','n','No','NO']:
        outro = "THANK YOU FOR USING THIS TOOL! HAVE A GREAT DAY!"
        for char in outro:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print (colorama.Fore.RESET)
        time.sleep(1)
        exit()

def main():
    clear()
    jsfile = input("Enter your JavaScript file path: ")
    with open(jsfile, 'r') as f:
        js_code = f.read()
    python_code = js2py.translate_js(js_code, name_translations=name_translations)
    make_py_file(python_code, jsfile)

    total_lines = len(js_code.splitlines())
    converted_lines = 0

    for line in js_code.splitlines():
        converted_lines += 1
        progress_bar(converted_lines, total_lines)
        time.sleep(0.05)
        clear()
    message = (colorama.Fore.GREEN + "[+]Successfully converted your JavaScript file!")
    print (colorama.Fore.RESET)
    ask()

if __name__ == '__main__':
    main()
