import requests
repos = requests.get("https://api.github.com/users/MordechaiTamam/repos")
import json
print(json.dumps(repos.json(), indent=4, sort_keys=True))