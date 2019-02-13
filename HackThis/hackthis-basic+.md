# HACKTHİS BASİC+

**LÜTFEN SORULARA UĞRAŞMADAN CEVAPLARINA BAKMAYIN. BEN ÇÖZÜMLERİ ANLAYAMAYAN YADA BAŞKA ÇÖZÜM YÖNTEMİ ÖĞRENMEK İSTEYENLER İÇİN BU YAZIYI YAZDIM. HAZIRA KONULSUN DİYE DEĞİL!**

## Level 1

Soruda verilen b1.txt dosyasını indirip açtığımızda bir şey anlayamıyoruz. Acaba ne dosyası? Linux sistemlerde `file` komutu ile dosya türünü görebiliriz.

`file b1.txt`

![hackthis-basic-1a](/assets/hackthis/hackthis-basic-1a.png)

Buradan dosyanın aslında resim dosyası olduğunu ve uzantısının değiştirildiğini görebiliyoruz. Uzantısını .jpg olarak değiştirdikten sonra:

![hackthis-basic-1b](/assets/hackthis/hackthis-basic-1b.jpg)

işte bu kadar.

## Level 2

Bu seviyeye ilk girdiğimizde bizi bu yazı karşılıyor:

>User agent not accepted, only secure_user_agent allowed

Ve bize ipucu olarak belli user-agent lerin doğrulandığını söylüyor.

>The site will only authenticate browsers with the correct user agent.

Peki user-agent ne demek? User-agent web sitelerinin bizim tarayıcımızı, tarayıcı sürümümüzü, işletim sistemimizi tanımak için kullandığı bir veridir. Bu veri siteye giriş isteğinde (GET request) ile birlikte gönderilir. Bu sayede site bize uygun site içeriğini gönderir.

Gelelim asıl soruya. Bu user-agert i nasıl değiştireceğiz? Chrome dan F12 yi tuşlayarak geliştirici konsolunu açıyoruz. Seçenekler(yani üç nokta işareti)->more tools-> network conditions. Gelen pencereden User-agent i değiştirebiliriz.

![hackthis-basic-2](/assets/hackthis/hackthis-basic-2.png)

## Level 3

Flash dosyaları sunucu ile haberleşmek için normal http protokolünü kullanır. Yani bizim tarayıcımız sunucu ile nasıl haberleşiyorsu flash da öyle haberleşir. GET POST gibi metodlarla.

Tarayıcımızdan submit butonuna bastığımız andaki trafiği incelersek neler olduğunu daha iyi anlayabiliriz. F12 ile geliştirici seçeneklerini ardından network(ağ) sekmesini açın ve daha sonra submit butonuna basın. Network trafiğini görüp inceleyebilirsiniz. Ve dikkat ederseniz submit butonuna tıkladığımız anda tarayıcı POST metodu ile sunucuya veri gönderiyor. Sunucuda buna göre sonucu. Bu post metodunu incelersek içindeki Score değişkenini ve değerini görebilirsiniz.

Bu seviyede bizden post motodundaki veriyi (score) değiştirmemizi istiyor. Bunu basit bir eklenti ile çözebiliriz. Burpsuite gibi programlarda kullanılabilir tabikide fakat ben basit olması için bir eklenti kullandım.

"Tamper data" eklentisi ile tarayıcının gönderdiği POST metot içeriğini değiştirebiliyoruz. Bu eklenti maalesef şu anda güncel firefox sürümü ile uyumlu değil. Bu yüzden ben firefox 52 indirdim.

Tamper data eklentisini açıyoruz. start temper dedikten hemen sonra submit butonuna basıyoruz. Tam bu esnada bir pencere açılacak. Submit butonunun POST metod verisi. İşte buradan "score" değerini 194175 olarak değiştirip onalıyoruz. Daha sonra stop temper diyerek programı kapatıyoruz. Kısaca POST metodundaki veriyi değiştirdik. İşte bu kadar.

![hackthis-basic-3a](/assets/hackthis/hackthis-basic-3a.png)

![hackthis-basic-3b](/assets/hackthis/hackthis-basic-3b.png)

## Level 4

Soruda bize bir resim ve ipucu olarakda "bir resim görünmeyen bir çok bilgi turar" diye bir ipucu vermiş. Bu bilgiler aslında metadatalardır. Herhangi siteden metadataları bulan bir araç kullanarak çok rahat bir şekilde sonuca ulaşabilirsiniz.

Ben [METAPİCZ][1] sitesini kullandım. Resmi yükleyip analiz ettirdikten sonra şifreye kolayca ulaşabiliyorsunuz. Artist ve Autor comment bölümleri!

![hackthis-basic-4](/assets/hackthis/hackthis-basic-4.png)

`Artist: james` ve `UserComment: I like chocolate` verilerinden user:`james` password:`chocolate` olduğunu hemen anlıyoruz.

## Level 5

Yine bir resim. Aynı siteden metadatasına baktığımızda işe yarar profil bilgileri bulabiliriz. Fakat hiçbiri bize kullanıcı adını ve şifresini vermiyor. Yani buradan bir şey çıkmıyor.

O zaman resim dosyasını farklı bir yolla açacağız. Metin editorü ile. notepad++ ile. Dosyayı açtıktan sonra yazıları incelersek bazı kısımları okuyabiliriz. Resmin en sonunda user-pass bilgileri yazıyor. CTRL+F ile aratarak daha hızlı bulabilirsiniz. Buradan username:`admin` password:`safe` olduğunu görüyoruz.

![hackthis-basic-5](/assets/hackthis/hackthis-basic-5.png)

## Level 6

Bizden sitenin ip adresini, host server bilgisini ve X-B6-Key header bilgisini istiyor. Ping atarak ip, whois sorgusu ile host bilgilerine ulaşabiliriz. Asıl sorun X-B6-Key.

X-B6-Key mail içerisinde gönderilen eşsiz (unique) bir bilgidir. Bu bilgiyi kayıt olduğumuz sırada gelen onaylama mailini inceleyerek bulabilirsiniz. Bu bilgi mailin header kısmında bulunur, doğrudan görünmez. Gmailde mail seçeneklerinden orjinali göstere tıklayarak bulabiliriz. Diğer mail servislerinde farklı olabilir.

Şimdi www.hackthis.co.uk adresine ping atıyorum ve whois ile sorguluyorum. Ardından bana üye olduğum zaman gelen onay mailini inceliyorum.

![hackthis-basic-6a](/assets/hackthis/hackthis-basic-6a.png)

![hackthis-basic-6b](/assets/hackthis/hackthis-basic-6b.png)

![hackthis-basic-6c](/assets/hackthis/hackthis-basic-6c.png)

Elbette mailde kişisel bilgilerimin olduğu alanlar silik :)

Buradan cevaplar:

```text
85.159.213.101
linode
Lajklsb#!"3jlak
```

## Level 7

>We are running a suspicious looking service. Maybe it will give you the answer.

Serverda şüpheli bir servis çalışıyor. Bunu nasıl bulabiliriz.

Nmap bir sunucuyu (yada bilgisayarı) taramak için kullanılan en bilindik programdır. Bir nmap port taraması ile sunucuda çalışan bütün servisleri bulabiliriz. Fakat bütün portları taramamız gerekiyor. Sonuçta servisin hangi porttan çalıştığını bilemeyiz. Ayrıca bazen farıklı parametrelerle tarama yapmak gerekebilir. Sadece denemeye devam edin :)

`nmap -p 1-65535 -T4 -A -v www.hackthis.co.uk` komutu ile linux sistemlerde nmap taramasını yapabilirsiniz. Ayrıca zenmap kullanarakta aynı taramayı yapabilirsiniz. Ayrıca zenmap kullanması daha kolay.

![hackthis-basic-7a](/assets/hackthis/hackthis-basic-7a.png)

Tarama tamam. şimdi hedef porta bağlanmamız gerekiyor. Bunun için netcat (kısaca nc) programını kullanabiliriz. `netcat www.hackthis.co.uk 6776` Ardından bize şifreyi verecek:

![hackthis-basic-7b](/assets/hackthis/hackthis-basic-7b.png)

`Welcome weary traveller. I believe you are looking for this: mapthat`

Şifre: `mapthat`

## ARAŞTIRMANIZ GEREKEN BAZI ŞEYLER

Bu sebiyede bası teknik bilgiler gerekiyor. Ben bunlardan bazılarını aşağıda listeledim:

1. user-agent nedir.
2. Belgelerdeki metadataler nelerdir?
3. e-mail in içeriği, yapısı
4. Nmap netcat kullanımı

**Bu konuları araştırmadan sonraki seviyeye GEÇMEMENİZİ şiddetle tavsiye ederim.**

[1]:http://metapicz.com
