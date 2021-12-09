import requests
ret = requests.post("http://127.0.0.1:5001/divide",data={"first":4,"second":6})
print(ret)