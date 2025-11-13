import json
import requests

request = "https://api.chucknorris.io/jokes/random"

try:
    ans = requests.get(request)
    if ans.status_code==200:
        ans = requests.get(request).json()
        print(ans["value"])

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")


