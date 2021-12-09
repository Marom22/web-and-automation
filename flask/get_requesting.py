import requests
try:
    repos = requests.get("http://127.0.0.1:5001/2")
    print(repos.text)
    print(repos.status_code)
except BaseException as ex:
    print(ex)
