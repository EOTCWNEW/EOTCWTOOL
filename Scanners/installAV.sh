#!/data/data/com.termux/files/usr/bin/bash

echo -e "\e[1;34m[+] Updating Termux packages...\e[0m"
pkg update && pkg upgrade -y

echo -e "\e[1;34m[+] Installing required packages...\e[0m"
pkg install python clang make clamav -y

echo -e "\e[1;34m[+] Creating requirements.txt...\e[0m"
echo "colorama" > requirements.txt

echo -e "\e[1;34m[+] Installing Python dependencies...\e[0m"
pip install -r requirements.txt

echo -e "\e[1;34m[+] Initializing ClamAV database (this may take some time)...\e[0m"
mkdir -p $HOME/.clamav
freshclam

echo -e "\e[1;32m[✓] Setup complete! You can now run your script.\e[0m"
