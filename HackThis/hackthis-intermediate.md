# HACKTHIS INTERMEDIATE WRITEUP

## Level 1

Burada get metodu ile passwordu göndermemizi istiyor. Get metudu url üzerinden gönderilir. Yani tüm bilgiler url üzerindedir ve plaintext hanlinde gönderilir. Güvenli değildir çünkü herkes tarafından okunabilir.

Peki nasıl göndereceğiz. Url ile parametre göndermek için `?` kullanılır. Eğer birden fazla parametre gönderilecek ise parametreler `&` ile birbirinden ayrılır. Örneğin:  
`site.com/biseyler?param1=deneme1&param2=deneme2&...`

Password göndermek ise tamamen benzer. `?password=flubergump`  
`https://www.hackthis.co.uk/levels/intermediate/1?password=flubergump`

Bu kadar basit.  
İsterseniz GET metodu ile ilgili internette araştırma yaparak daha ayrıntılı bilgi bulabilirsiniz.

## Level 2

Post metodu ise get metodundan farklı olarak url üzerinden veri göndermez. Parametreyi http/https requestinin içine gömer. Bu sayede veri güvende kalır.

Post metodu ile veri göndermek için form oluşturabiliriz. Form tagleri arasına bir input bide submit buyonunun olması yeterli. Bide metod post olarak ayarlanmalı elbette :)  
Örnek bir kod aşağıda var:

```html
<!--form tagini post olarak ayarladık ve actiona sitenin linkini verdik-->
<form method="POST" action="https://www.hackthis.co.uk/levels/intermediate/2">

    <!--input alanımız. name password olarak ayarlanmalı-->
    <input type="text" name="password">

    <!--bide submit butonumuz-->
    <input type="submit" value="Send">
</form>
```

Bu kodu sayfanın html kodları arasına korsak ve şifreyi yazıp butona tıklarsak işlem tamam.

![hackthis-intermediate-3](/HackThis/resimler/hackthis-intermediate-2.jpg)

İsterseniz POST metodu ile ilgili internette araştırma yaparak daha ayrıntılı bilgi bulabilirsiniz.

## Level 3

Busoru  cookieler ile ilgili. Sayfadaki resme tıkladığımızda bizi bir sayfaya yönlendiriyor. Eğer `restricted_login` cookie si true ise girişe izin veriyor. aksi taktirde engelliyor ve hata mesajı veriyor.

Bizim bu soruda cookie değerini true olarak değiştirmemiz gerekiyor. Bunun için birçok eklenti var. Ben "Cookie Quick Manager" isimli firefox eklentisini kurdum. Siz de herhangi bir eklenti kurabilirsiniz.

`restricted_login` cookie sinin değerini değiştirdikten sonra resme tıklayarak seviyeyi geçebilirsiniz.

![hackthis-intermediate-3](/HackThis/resimler/hackthis-intermediate-3.jpg)

## Level 4

Bu seviye XSS güvenlik açığı ile ilgili. Eğer XSS nedir bilmiyorsanız internette araştırma yaparak öğrenebilirsiniz.

Sayfadaki inputta XSS açığı var. Yani javascript kodu çalıştırabiliyoruz. Ama bir sorun var. Inputtaki değer işlenmeden önce bir güvenlik kontrolünden geçiyor. Yani filtreleniyor.

Fitrenin nasıl çalıştığını anlamak için birkaç deneme yapabiliriz.  `<script>alert('HackThis!!');</script>` scriptini doğrudan girdiğimizde çıktı `alert('HackThis!!');` şeklinde oluyor. Yani filtre `<script>` taglerini siliyor.

Bunu aşmanın birçok yolu var. Ben içiçe script taglari yazarak çözdüm. Siz internette araştırarak birçok yöntem bulabilirsiniz.

```javascript
<scr<script>ipt>alert('HackThis!!');</scr</script>ipt>
```

## Level 5

Soruyu okuduğumuzda log scriptine yakalanmadan giriş yapmaya çalışmamamız gerekiyor. Buradan anlıyoruz ki soru "log injection" ile ilgili.

Log injection sistemde tutulan log dosyalarını özel girdiler kullanarak değiştirmektir (basit olarak). Bunun bir çok yolu var. Ben araştırırken bulduğum 2 sitede bu konuyu gayet güzel anlatmış. [Burada][1] ve [buradaki][2] siteler.

Şimdi sıra geldi soruu çözmeye. "\n" işimize yarayabilir: `biseyler \n`. Bu kaydın bir sonraki satıra geçmesini sağlayacak yani log dosyası değişmiş olacak. Birazda hayal gücümüzü kullanırsak:  
`foo\r\nSep 11:2018:01:07:13: ApplicationName:Successful Login, Id=admin`

## Level 6

Giriş için konrolün sql yani database ile yapılmadığını biliyoruz. O zaman ne ile yapılıyor. İpucuna baktığımızda xml ile yapıldığını hemen anlayabiliriz.

O zaman "XML injection" nedir öğrenmemiz gerekecek. Ben [buradaki][3] siteden öğrendim, elbette siz başka sitelerede bakabilirsiniz.

soruda adı "Sandra Murphy" olan birisine giriş yapmamızı istiyor. İpucundaki xml kodunu incelersek gerçek isim için 'realname' parametresi kullanılmış.

O zaman username-şifre-realname girişlerimizi şu şekilde yapabiliriz:

```text
biseyler' or realname='Sandra Murphy' or 'a
```

Burada tek tırnak ile girişi sonlandırdık. Or ile yeni parametre verdik yani gerçek ismi. Sonra tekrar or ve `'a` ile bitirdik. bunun sebebi kontrolün yapıldığı programlama dilinde bir syntax hatası olmaması için. Eğer bunu yapmazsak sunucu tarafında kod exception verecek.

Sunucuda kontrol yapan kod yaklaşık buna benzer bi şey.

```php
$query = "//user[login/text() = '" . $login . "' and password/text() = '" . $password . "']";
```

Örnekleri arttırabiliriz ama hepsi aynı mantık.

```text
biseyler' or realname='Sandra Murphy' or 'a'='a
'or realname='Sandra Murphy' or'
```

## Son birkaç not

Saldırılar ile ilgili bilgi bulabileceğiniz kaynak birkaç site:

- [owasp.org][4] birçok konu ve ornek anlatımın bulunduğu bir site.  
- [securityidiots.com][5] web pentest ile ilgini güzel bir anlatımı var. kesinlikle tavsiye ederim.

[1]: https://affinity-it-security.com/what-is-log-injection/
[2]: https://www.owasp.org/index.php/Log_Injection
[3]: https://www.owasp.org/index.php/Testing_for_XML_Injection_(OTG-INPVAL-008)
[4]: https://www.owasp.org/index.php/Category:Attack
[5]: http://securityidiots.com/