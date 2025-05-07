import geocoder
import os

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

def ip_tracer(ip_address):
    g = geocoder.ip(ip_address)
    print(f"{B}IP Address:{rc}", ip_address)
    print(f"{B}Country:{rc}", g.country)
    print(f"{B}City:{rc}", g.city)
    print(f"{B}Latitude:{rc}", g.lat)
    print(f"{B}Longitude:{rc}", g.lng)
    print(f"{B}Organization:{rc}", g.org)

def print_design():
    print(f"{R}=======================================")
    print(f"  {bbg}Created by PHANTOMX MR.CLAY  PH{rc}")
    print(f"{R}======================================={rc}")
    print("""
───────────────████████ ★
────────────██████████████ ★
──────────█████────────█████ ★
────────████─────████─────████ ★
───────███───███████████────███ ★
──────██────███████░░░████───███ ★
─────██───█████████░░░░░░██───███ ★ 
────██───██████████░░░░░░░██───███ ★
────██───██████████░░░░░░░░░█───███ ★
───██───███████████░░░░░░░░░░█───██ ★
──██───████████████░░░░░░░░░░█───███ ★
──█████████████████░░░░░░░░░░░██████ ★
──███▓▓████████████░░░░░░░░░░░█▓▓███ ★
─██▓▓▓█████████████░░░░░░░░░░░░█▓▓▓██ ★
─█▓▓▓▓█████████████░░░░░░░░░░░░█▓▓▓▓█ ★
█▓▓▓▓▓█████████████░░░░░░░░░░░░█▓▓▓▓▓█ ★
█▓▓▓▓▓████████░░░░█░████░░░░░░░█▓▓▓▓▓█ ★
█▓▓▓▓▓████████░░░░█░████░░░░░░░█▓▓▓▓▓█ ★
█▓▓▓▓▓████████░░░░█░████░░░░░░░█▓▓▓▓▓█ ★
█▓▓▓▓▓█████████░░██░░██░░░░░░░██▓▓▓▓▓█ ★
─█▓▓▓▓▓████████████░░░░░░░░░░░█▓▓▓▓▓█ ★
─██▓▓▓▓████████████░░░░░░░░░░░█▓▓▓▓██ ★
──██▓▓▓████████████░░░░░░░░░░░█▓▓▓██ ★
────█████████████░░██░░░░░░░██████ ★
─────────██████████░░░░░░░░██ ★
──────────████████░█░░░░░███ ★
───────────███████░█░░░████ ★
─────────────████████████ ★
───────────────████████ ★

""")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_design()
    ip_address = input("=>Enter the IP address: ")
    ip_tracer(ip_address)

if __name__ == "__main__":
    main()
