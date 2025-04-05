from urllib.parse import urljoin
import os
import requests
import threading
from bs4 import XMLParsedAsHTMLWarning
import warnings
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
from bs4 import BeautifulSoup

bbg = '\033[44m'  # BLUE BACKGROUND
W = '\033[37m'  # Information/About/Tuts
R = '\033[38;2;255;0;0m'  # Aggressive/Alert/Caution/Warning/Failed/
B = '\033[34m'  # Normal/Questioning/
G = '\033[1;32m'  # Process Completed/Success/
Y = '\033[33m'  # On Process/Processing/Executing/Deploying/
O = '\033[38;2;255;165;0m'  # Orange
OY = '\033[38;2;255;200;0m'  # Orange-Yellow
DO = '\033[38;2;255;100;0m'  # Deep Orange
RO = '\033[38;2;255;50;0m'  # Reddish-Orange
rc = '\033[0m'  # RESET COLOR
visited_urls = set()

def banner():
    os.system("cd && cd EOTCW/pics && jp2a spider.png | lolcat")
    print(f"{DO}Spider Bot V.1")
    print(f"{DO}Coded by Gl1tch3d & PROFESSOR-H3X.{rc}")
    print(" ")

def levels():
    level = input(f"""
{W}LEVELS:
• NORMAL
• DEEP
• ADVANCED

CHOOSE[1/2/3]:{rc} """)
    return level

def crawl(url, keyword, visited_urls):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)

        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                url_join = urljoin(url, urls2)
                if keyword in url_join:
                    print(url_join)
                    crawl(url_join, keyword, visited_urls)
            else:
                pass

def deepcrawl(url, keyword, visited_urls):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.find_all('a')
    urls = []
    for tag in a_tag:
        href = tag.get("href")
        if href is not None and href != "":
            urls.append(href)

    for urls2 in urls:
        if urls2 not in visited_urls:
            visited_urls.add(urls2)
            url_join = urljoin(url, urls2)
            if keyword in url_join:
                print(url_join)
                deepcrawl(url_join, keyword, visited_urls)
        else:
            pass

def advancedcrawl(url,keyword, visited_urls):
    try:
        filteredcodes, allowedcodes = chooseamethod()
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    if response.status_code in allowedcodes:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)

        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                url_join = urljoin(url, urls2)
                if keyword in url_join:
                    print(url_join)
                    advancedcrawl(url_join, keyword, visited_urls)
            else:
                pass

    elif response.status_code in filteredcodes:
        pass

    else:
        pass

def chooseamethod():
    method = input(f"""
{W}METHODS:
• FILTER SOME HTTP RESPONSE CODES
• CHOOSE SOME RESPONSE CODES

CHOOSE[1/2]:{rc} """)
    if method == "1":
        tobefilteredcodes = input(f"{B}ENTER THE RESPONSE CODES SEPARATED BY SPACE TO BE FILTERED:{rc} ")
        strcodes = [str(fcode) for fcode in tobefilteredcodes.split()]
        filteredcodes, allowedcodes = filtercodes(strcodes)
    elif method == "2":
        tobeallowedcodes = input(f"{B}ENTER THE RESPONSE CODES SEPARATED BY SPACE TO BE ALLOWED:{rc} ")
        strcodes = [str(acode) for acode in tobeallowedcodes.split()]
        filteredcodes, allowedcodes = allowcodes(strcodes)
    else:
        print(f"{R}ERROR: INVALID CHOICE! TO CHOOSE, TYPE A NUMBER BETWEEN 1-2!")
        exit()

    for i in range(threadamount):
        t = threading.Thread(target=deepcrawl, args=(url, keyword, visited_urls))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return (filteredcodes, allowedcodes)

def filtercodes(strcodes):
    filtered_codes = []
    allowed_codes = ['100','101','102','200','201','202','203','204','205','206','207','208','226','300','301','302','303','304','305','306','307','308','400','401','402','403','404','405','406','407','408','409','410','411','412','413','414','415','416','417','418','421','422','423','424','425','426','427','428','429','431','444','451','499','500','501','502','503','504','505','506','507','508','510','511','599']
    for fcode in strcodes:
        filtered_codes.append(fcode)
        allowed_codes.remove(fcode)
    return (filtered_codes, allowed_codes)

def allowcodes(strcodes):
    filtered_codes = ['100','101','102','200','201','202','203','204','205','206','207','208','226','300','301','302','303','304','305','306','307','308','400','401','402','403','404','405','406','407','408','409','410','411','412','413','414','415','416','417','418','421','422','423','424','425','426','427','428','429','431','444','451','499','500','501','502','503','504','505','506','507','508','510','511','599']
    allowed_codes = []
    for acode in strcodes:
        allowed_codes.append(acode)
        filtered_codes.remove(acode)
    return (filtered_codes, allowed_codes)

if __name__ == "__main__":
    banner()
    url = input(f"{B}TARGET URL(e.g https://example.com/):{W} ")
    mode = input(f"""
MODES:
• AUTO
• MANUAL

CHOOSE[1/2]:{rc} """)

    if mode == "1": # AUTO MODE
        level = levels()
        if level == "1":
            print(f"{B}MODE CHOSEN ={rc} 1,AUTO {O}| {B}LEVEL CHOSEN ={rc} 1,NORMAL")
        elif level == "2":
            print(f"{B}MODE CHOSEN ={rc} 1,AUTO {O}| {B}LEVEL CHOSEN ={rc} 2,DEEP")
        elif level == "3":
            print(f"{B}MODE CHOSEN ={rc} 1,AUTO {O}| {B}LEVEL CHOSEN ={rc} 3,ADVANCED")
        else:
            print(f"{R}ERROR: INVALID CHOICE! TO CHOOSE, TYPE A NUMBER BETWEEN 1-3!")
            exit()

        keyword = url.split("//")[-1].replace("www.", "").replace(".com", "").replace("/", "")
        print(f"{W}NOTE: PLEASE DO NOT ENTER AN EXTREMELY HIGH AMOUNT OF THREADS SO THAT YOUR TERMINAL WON'T CRASH.")
        threadamount = int(input(f"{B}AMOUNT OF THREADS:{W} "))

        threads = []
        if level == "1":
            for i in range(threadamount):
                t = threading.Thread(target=crawl, args=(url, keyword, visited_urls))
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

        elif level == "2":
            for i in range(threadamount):
                t = threading.Thread(target=deepcrawl, args=(url, keyword, visited_urls))
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

        elif level == "3":
            chooseamethod()

        print(f"{G}Attack sent successfully!{rc}")

    elif mode == "2":  # MANUAL Mode
        level = levels()
        if level == "1":
            print(f"{B}MODE CHOSEN ={rc} 2,MANUAL {O}| {B}LEVEL CHOSEN ={rc} 1,NORMAL")
        elif level == "2":
            print(f"{B}MODE CHOSEN ={rc} 2,MANUAL {O}| {B}LEVEL CHOSEN ={rc} 2,DEEP")
        elif level == "3":
            print(f"{B}MODE CHOSEN ={rc} 2,MANUAL {O}| {B}LEVEL CHOSEN ={rc} 3,ADVANCED")
        else:
            print(f"{R}ERROR: INVALID CHOICE! TO CHOOSE, TYPE A NUMBER BETWEEN 1-3!")
            exit()

        keyword = input(f"{B}KEYWORD TO FIND:{W} ")
        print(f"{W}NOTE: PLEASE DO NOT ENTER AN EXTREMELY HIGH AMOUNT OF THREADS SO THAT YOUR TERMINAL WON'T CRASH.")
        threadamount = int(input(f"{B}AMOUNT OF THREADS:{W} "))

        threads = []
        if level == "1":
            for i in range(threadamount):
                t = threading.Thread(target=crawl, args=(url, keyword, visited_urls))
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

        elif level == "2":
            for i in range(threadamount):
                t = threading.Thread(target=deepcrawl, args=(url, keyword, visited_urls))
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

        elif level == "3":
            chooseamethod()

        print(f"{G}Attack sent successfully!{rc}")

    else:
        print(f"{R}ERROR: INVALID CHOICE! TO CHOOSE, TYPE A NUMBER BETWEEN 1-2!")
        exit()
