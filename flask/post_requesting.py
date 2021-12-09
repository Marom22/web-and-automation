import requests
repos = requests.post("http://localhost:5001/add",json={"id": '2',"first":"17","second":"2"})

print(repos.json())