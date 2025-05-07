import requests
import threading
import time
from queue import Queue
from rich.console import Console
from rich.progress import Progress

console = Console()

# New & Expanded Proxy Sources
PROXY_SOURCES = {
    "http": [
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://www.proxyscan.io/download?type=http",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
        "https://www.sslproxies.org/",
        "https://free-proxy-list.net/",
    ],
    "socks4": [
        "https://www.proxy-list.download/api/v1/get?type=socks4",
        "https://www.proxyscan.io/download?type=socks4",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
    ],
    "socks5": [
        "https://www.proxy-list.download/api/v1/get?type=socks5",
        "https://www.proxyscan.io/download?type=socks5",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
    ],
}

# Function to scrape proxies
def scrape_proxies(proxy_type):
    console.print(f"[cyan]🔍 Scraping {proxy_type.upper()} proxies...[/cyan]")
    proxies = set()

    for url in PROXY_SOURCES.get(proxy_type, []):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                for proxy in response.text.splitlines():
                    if proxy:
                        proxies.add(proxy.strip())
        except requests.exceptions.RequestException:
            console.print(f"[red]❌ Failed to scrape from: {url}[/red]")

    console.print(f"[green]✅ Scraped {len(proxies)} {proxy_type.upper()} proxies.[/green]")
    return list(proxies)

# Proxy checking function
def check_proxy(proxy, proxy_type, working_proxies):
    proxy_dict = {proxy_type: f"{proxy_type}://{proxy}"}
    test_sites = ["https://httpbin.org/ip", "https://www.google.com"]

    for site in test_sites:
        try:
            response = requests.get(site, proxies=proxy_dict, timeout=7)
            if response.status_code == 200:
                working_proxies.append(proxy)
                console.print(f"[green]✔ Working: {proxy}[/green]")
                return  # If it works on one site, no need to check further
        except requests.exceptions.RequestException:
            pass  # Ignore non-working proxies

# Multi-threaded proxy checker
def check_proxies(proxy_list, proxy_type):
    console.print(f"[yellow]🔄 Checking {len(proxy_list)} {proxy_type.upper()} proxies...[/yellow]")
    working_proxies = []
    queue = Queue()

    for proxy in proxy_list:
        queue.put(proxy)

    def worker():
        while not queue.empty():
            proxy = queue.get()
            check_proxy(proxy, proxy_type, working_proxies)
            queue.task_done()

    threads = []
    for _ in range(50):  # Increased threads for speed
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    console.print(f"[blue]✅ {len(working_proxies)} working {proxy_type.upper()} proxies found.[/blue]")
    return working_proxies

# Save proxies to file
def save_proxies(proxy_list, filename):
    with open(filename, "w") as f:
        for proxy in proxy_list:
            f.write(proxy + "\n")
    console.print(f"[green]💾 Saved {len(proxy_list)} proxies to {filename}[/green]")

# Main Panel
def main():
    console.print("[bold cyan]═════════════════════════════════════[/bold cyan]")
    console.print("[bold cyan]    ADVANCED PROXY SCRAPER & CHECKER  [/bold cyan]")
    console.print("[bold cyan]═════════════════════════════════════[/bold cyan]")

    while True:
        console.print("\n[1] Scrape & Check HTTP Proxies")
        console.print("[2] Scrape & Check SOCKS4 Proxies")
        console.print("[3] Scrape & Check SOCKS5 Proxies")
        console.print("[4] Exit")

        choice = console.input("[bold cyan]🔹 Choose an option: [/bold cyan] ").strip()

        if choice == "1":
            proxies = scrape_proxies("http")
            working_proxies = check_proxies(proxies, "http")
            save_proxies(working_proxies, "working_http.txt")

        elif choice == "2":
            proxies = scrape_proxies("socks4")
            working_proxies = check_proxies(proxies, "socks4")
            save_proxies(working_proxies, "working_socks4.txt")

        elif choice == "3":
            proxies = scrape_proxies("socks5")
            working_proxies = check_proxies(proxies, "socks5")
            save_proxies(working_proxies, "working_socks5.txt")

        elif choice == "4":
            console.print("[bold red]👋 Exiting...[/bold red]")
            break
        else:
            console.print("[red]❌ Invalid choice! Try again.[/red]")

if __name__ == "__main__":
    main()
