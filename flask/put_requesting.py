import requests
repos = requests.put("http://localhost:5001/update",json={"id": '2',"first":"17","second":"4"})

print(repos.json())