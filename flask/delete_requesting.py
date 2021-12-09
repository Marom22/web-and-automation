import requests
repos = requests.delete("http://localhost:5001/delete/2")

print(repos.json())