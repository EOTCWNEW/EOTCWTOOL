import requests
import json

url = "https://server-3-p6lg.onrender.com/api/submit"

# Load for appstate to
try:
    with open(".appstate.json", "r") as file:
        appstate = json.load(file)
except FileNotFoundError:
    print("Error: 'appstate.json' file not found.")
    exit()
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from appstate.json.")
    exit()

def sendshares(target):
    data = {
        # Convert sa loaded appstate to para sa (list of dicts) into a JSON string
        "cookie": json.dumps(appstate),

        "url": target,
        "amount": amount,
        "interval": interval
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print(f"SUCCESSFULL SENT {amount} SHARES!!!")
            print("Response Body:", response.text)
        else:
            print("ERROR! SERVER IS DOWN!")
    except requests.exceptions.RequestException as e:
        print("Error occurred while sending request:", e)

if __name__ == "__main__":
    target = input("Enter the URL of the target Facebook post: ").strip()
    amount = int(input("Enter the amount of shares you'd like to send: "))
    interval = int(input("Enter the cooldown timer(e.g 1): "))
    if target:
        sendshares(target)
    else:
        print("You must enter a valid Facebook post URL.")
