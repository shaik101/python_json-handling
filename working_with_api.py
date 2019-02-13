

import requests

resp = requests.get("https://api.github.com/emojis")

data = resp.json()

print(type(data)