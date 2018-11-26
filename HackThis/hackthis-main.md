# HACKTHİS MAİN

Hackthis birbirinden güzel soruların olduğu siber güvenlikle uğraşan insanların mutlaka uğraması gereken bir duraktır. Farklı kategorilerde hazırlanan birbirinden farklı sorular bulunuyor ve her soru ile yeni bir şey öğretiyor.

Ayrıca sitede geliştiricilerin zorlandıkları sorularda yardım almaları  ve soruyu çözen insanların kendi çözüm yöntemlerini paylaştıkları bir forum bulunmakta. Bu sayede takıldığınız bir nokra da yardım almanız kolay ve çok güzel. Ayrıca bu formdan farklı çözümleri görerek birçok şey öğrenebilirsiniz.

Ben ise bu yazımda bu sitenin ilk seviyesi olan MAIN seviyesinin çözümlerini anlatacağım. Bunun için internet'te ingilizce olarak çok şey var ama Türkçe bir şey yok. Bunu da ben yapayım istedim.

**SAKIN SAKINA SORULARA UĞRAŞMADAN BU ÇÖZÜMLERE BAKMAYIN! HAZIRA ALIŞMAYIN! UĞRAŞMAYI ÖĞRENİN!**

## Level 1

Web sitelerinde yapılan en basit hatalardan biri user-pass bilgilerini kaynak koda yazmaktır. Developer geliştirme aşamasında iken kullandığı giriş bilgilerini kaynak koda yorum satırı olarak yazar ve daha sonra silmeyi unutur. Bu yapılan en basit hatalardan biridir. Fakat şundan emin olun hala yapanlar var.

Sayfanın kaynak kodunu incelediğimizde 29. satırda kullanıcı adını ve şifresini hemen görürüz.

```javascript
<!-- username: in, password: out -->
```

Sayfada username-pass yazmasa bile kaynak kod her zaman bize çok şey söyler.

## Level 2

Aynı level 1 deki gibi fakat bu sefer username-password yorum satırında değil. Bunun yerine `span` etiketleri arasında gizlenmiş. Kaynak kodda 868 ve 870. satırlara baktığımızda `label` etiketinin yanında `span` etiketlerinin arasında gizlenmiştir. fakat sayfanın arka planı ile aynı renkte olduğu için gözle görmek mümkün değil. Ama olsun sonuçta kaynak kodda var.  

```javascript
<span style="color: #000000">resu</span>

<span style="color: #000000">ssap</span>
```

**SAKIN UNUTMAYIN KAYNAK KOD BİZE HER ZAMAN ÇOK ŞEY SÖYLER.**

## Level 3

Kaynak kodda username-password var. Sadece javascript kodları arasına gizlenmiş. Javascript istemci tarafından görülebildiği için javascript ile güvenliği sağlamaya çalışmak asla iyi bir fikir değildir. Sayfanın kaynak kodunda 41. satırdaki javascript koduna baktığımızda zaten hemen kendini belli ediyor.

```javascript
        <script type='text/javascript'> $(function(){ $('.level-form').submit(function(e){ if(document.getElementById('user').value == 'heaven' && document.getElementById('pass').value == 'hell') { } else { e.preventDefault(); alert('Incorrect login') } })})</script>
```

## Level 4

Bazen kaynak kodda olukça önemli bilgiler bulunabilir. Username-password gibi. Username-password olmasa bile site ile ilgili önemli bilgilere ulaşabiliriz. Bu örnekte username-password bilgilerini içeren bir dosyanın adresine ulaştık. 872. satırdaki kod:

```javascript
<input type="hidden" name="passwordfile" value="../../extras/ssap.xml">
```

`type="hidden"` olduğundan dolayı sayfada görünmüyor. Fakat kosyanın yolunu yinede bulabiliyoruz.  
"[https://www.hackthis.co.uk/levels/extras/ssap.xml](https://www.hackthis.co.uk/levels/extras/ssap.xml)" adresine gittiğimizde aşağıdaki xml dosyasındaki kodlar bize admin bilgilerini veriyor.

```xml
<user>
    <name>Admin</name>
    <username>999</username>
    <password>911</password>
</user>
```

İşte bu kadar basit.

## Level 5

Javascript kullanıcılar tarafından görülebildiği için güvenlik için username-password gibi önemli bilgileri içeren işlemlerde kullanmak pek iyi olmaz.

Sayfaya ilk girdiğimizde bir alert ile şifre girmemizi istiyor. Fakat alert javascript ile yazıldığı için kodu okumak hiçde zor değil.

```javascript
<script language="JavaScript" type="text/javascript">
    var pass;
    pass=prompt("Password","");
    if (pass=="9286jas") {
        window.location.href="/levels/main/5?pass=9286jas";
    }
</script>
```

Daha sonra sayfayı yenileyerek şifreyi girebiliriz.

## Level 6

Bu soruda "Ronald" olarak giriş yapmamız gerekiyor fakat seçeneklerde ronald yok. Bu sefer sadece kaynak kodu görmek bize yetmez, onu düzenlememiz gerekiyor. Bunu için sayfada seçeneklerin olduğu çubukta sağ tıklayıp incele demeliyiz. Eğer sayfanın başke bir yerine tıklarsak manüel olarak koddan bulmamuz gerekir. Ctrl+F ile arayarakda bulabiliriz. 871. satır.

Buradan yeni bir seçenek ekleyebiliriz yada isimlerden birini "Ronald" olarak değiştirebiliriz. Ben John'u Ronald olarak değiştirdim. Sonrada submit ederek bu seviyeyi geçebiliriz.

```javascript
<select id="user" name="user">
    <option>Ronald</option>
    <option>Petter</option>
    <option>David</option>
    <option>Sam</option>
</select>
```

## Level 7

Bize soruda ipucu olarak şifrenin txt olarak saklandığını ve arama motorlarını kullanarak bile şifreyi bulamayacağımızı söylüyor.

>You wouldn't even find the page by using a search engine as search bots have been excluded.

Peki bu ne demek. Arama motorları `robots.txt` isimli bir dosyadan faydalanarak indexleme yapar. Bu dosyada sitenin taranması istenen ve istenmeyen alanları ile ilgili bilgiler bulunur. Eğer arama motorları ile bulamayacaksak bu dosyada şifrenin yazılı olduğu txt dosyasına taranması istenmeyen olması gerekmez mi?

Hemen rotots.txt dosyasına bakalım.
[https://www.hackthis.co.uk/robots.txt](https://www.hackthis.co.uk/robots.txt)  
Dosyanın içeriği şöyle:

```text
User-agent: *
Allow: /
Disallow: /contact.php
Disallow: /inbox/
Disallow: /levels/
Disallow: /levels/extras/userpass.txt
Disallow: /users/
Disallow: /ctf/8/php/*

User-agent: Mediapartners-Google
Disallow:

Sitemap: https://www.hackthis.co.uk/sitemap.xml
```

`/levels/extras/userpass.txt` kendini hemen belli etmiyor mu?

Bu dosyaya girdiğimizde([https://www.hackthis.co.uk/levels/extras/userpass.txt](https://www.hackthis.co.uk/levels/extras/userpass.txt)):

```text
48w3756
u3qh458
```

1. satır username 2. satır password.

Ayrıca robots.txt dosyaları bize kaynak kod gibi site ile ilgili birçok bilgi verir. Arama otorları ile bulamayacağımız dizinler site haritası vs. Güvenlik testlerinde mutlaka kontrol edilmesi gerekir.

Robots.txt dosyası ile ilgili daha ayrıntılı bilgite [BURADAN][2] ulaşabilirsiniz.

## Level 8

Yine kaynak koda baktığımızda 872. satırda bir dosya görüyoruz.

```javascript
<input type="hidden" name="passwordfile" value="extras/secret.txt">
```

Bu satırdaki yardım ile dosyayı okuyabiliyoruz.
[https://www.hackthis.co.uk/levels/extras/secret.txt](https://www.hackthis.co.uk/levels/extras/secret.txt)

```text
1011 0000 0000 1011
1111 1110 1110 1101
```

Ayrıca sorudaki ipucuna baktığımızda bize geliştiricinin şifreyi korumaya çalıştığını , binary veriyi bir şeye dönüştürmemiz gerektiğini söylüyor.

>The coder has made the same mistake as level 4 but this time at least he has tried to protect the password. The password has been encrypted, convert the binary into something that is easier for humans to read (base 16).

Peki ama neye? Dosyayı incelersek sayılar 4 erli olarak gruplandırılmış. Bu demek oluyor ki verimiz base16. Yani her karakter base16 olarak kodlanmış. Ayrıca bize soruda 16 tabanında olduğunu söylemiş yani base16.  Şimdi her karakteri bulmak için internetten base16 karşılıklarını bulmamız gerekiyor. İnternetten herhangi base16-binary dönüştürücü işimizi görür.

```text
B 0 0 B
F E E D
```

İşte bu kadar. Şimdi şifreyi aralarında boşluk olmadan girebiliriz.

## Level 9

Geliştirici bu sefer şifreyi unutmaya karşı bir buton eklemiş. Tıkladığımızda mail adresini isteyen bir sayfa ile karşılaşıyoruz. Burada kaynak kodu incelersek (870. satır.):

```javascript
<input type="hidden" name="email2" id="email2" value="admin@hackthis.co.uk" autocomplete="off">
```

Gizlenmiş bir input girişi ve bir mail adresi. Normalde bu mail adresini girdiğimizde admine şifresini kurtarmak için mail gönderiyor. Bu mail adresini değiştirerek yani bizim mail adresimizi girersek (yada başka bir mail adresi) maili o adrese gönderiyor(tabiki mail göndermiyor senaryo bu!).

Bunun için sayfada öğeyi incele diyerek mail adresini buluyor ve değiştiriyoruz. Ben `asdf@asdf.com` olarak değiştirdim. İste bu kadar.

## Level 10

Burada dosyayı bulmak biraz uğraştırıcı. Daha önceden bulduğumuz dosyalar extras dizininiz altında idi. Bu dosyada aynen öyle.  
[https://www.hackthis.co.uk/levels/extras/level10pass.txt](https://www.hackthis.co.uk/levels/extras/level10pass.txt)

Dosyanın içeriği ise şu şekilde:

```text
69bfe1e6e44821df7f8a0927bd7e61ef208fdb25deaa4353450bc3fb904abd52:f1abe1b083d12d181ae136cfc75b8d18a8ecb43ac4e9d1a36d6a9c75b6016b61
```

Username:password şeklinde iki nokta ile ayrılmış. Fakat hangi algoritma ile şifrelenmiş? Hangi hash fonksiyonu kullanılmış. Bunun için bu hashi analiz etmeliyiz. Ben burada [md5hashing.net][1] sitesini kullanıdım. Bu siteden "hash type checker" bölümünen hasi check ettikten sonra sha256 olma ihtimalinin yüksek olduğunu gösterdi.

Daha sonra aynı siteden sha256 decoder ile şifreyi çözebiliriz.

```text
carl:guess
```

Bu yöntem ile ancak çok yaygın kullanılan şifreler bulunabilir. Bu yöntemin çalışması için daha önceden bu hashin çözülmüş ve kaydedilmiş olması gerekir. İşte bundan dolayı bilindik şifreleri kırmak çok kolaydır.

Daha basit bir yöntem ise hash'i google'da aratmaktır. bu sayede sonuca daha hızlı ulaşabiliriz.

---

Diğer seviyelerin çözümleri zamanla gelecek. Beklemede kalın...

[1]:https://md5hashing.net
[2]:https://support.google.com/webmasters/answer/6062608?hl=tr
