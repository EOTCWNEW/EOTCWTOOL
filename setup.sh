#!/bin/bash

# ANSI escape codes for colors
colors=("\e[38;5;21m" "\e[38;5;57m" "\e[38;5;93m" "\e[38;5;129m" "\e[38;5;165m" "\e[38;5;201m")

clear

# ASCII Art
lines=(
  "____________   __________________________________"
  "____  _/__  | / /_  ___/__  __/__    |__  /___  /"
  " __  / __   |/ /_____ \\__  /  __  /| |_  / __  /"
  "__/ /  _  /|  / ____/ /_  /   _  ___ |  /___  /___"
  "/___/  /_/ |_/  /____/ /_/    /_/  |_/_____/_____/"
)

# Print with gradient effect
for i in "${!lines[@]}"; do
  echo -e "${colors[i % ${#colors[@]}]}${lines[i]}\e[0m"
done

echo " "
echo -e "\e[38;5;201mCoded by Mr.KasakiX...\e[0m"
echo -e "\e[38;5;201mInstaller Version 2.1.5\e[0m"
echo " "
echo " "

pkg install python -y
pkg install python3 -y
pkg install golang -y
pkg install clang -y
pkg install nodejs -y
pkg install steghide -y
pkg install jhead -y
pkg install hping3 -y
pip install os
pip install sys
pip install time
pip install aiohttp
pip install requests
pip install asyncio
pip install random
pip install subprocess
pip install colorama
pip install terminaltables
pip install python-nmap
pip install cryptography
pip install pyencrypt
pip install ssl
pip install http.client
pip install threading
pip install multiprocessing
npm fund
npm install axios && socks-proxy-agent && https-proxy-agent && readline
