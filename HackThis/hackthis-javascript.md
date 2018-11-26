# HACKTHİS JAVASCRIPT

Bu yazımda hackthis javascript kategorisini inceleyeceğiz. Bu seviyeye başlamadan önce w3schools dan javascript çalışmanızı tavsiye edrim. Ayrıca sorulara uğraşmadan çözümlere kesinlikle bakmayın.  
Neyse hadi başlayalım.

## Level 1

Bu ilk javascript seviyesinde bir şifre isteniyor. Bu şifre javascript değişkeni olarak tanımlanmış ve kontrol fonksiyonuda javascript. Sayfanın kaynak kodunu incelediğimizde aşağıdaki kodu görüyoruz.

```javascript
<script type='text/javascript'> $(function(){ $('.level-form').submit(function(e){ e.preventDefault(); if(document.getElementById('pass').value == correct) { document.location = '?pass=' + correct; } else { alert('Incorrect password') } })})</script>
```

Bu kodda "pass" id li input değeri corrent değişkeni ile kontrol ediliyor. Yani bizim "correct" değişkeninin değerini bulmamız gerekiyor. Sayfanın en sonunda şu script'i görebiliriz.

```javascript
<script type='text/javascript'> var correct = 'jrules' </script>
```

Buradan corrent değerinin `jrules` olduğunu anlıyoruz.

Yada diğer bir yöntem ise javascript konsolundan değeri yazdırmak. Aşağıdaki gibi.

![hackthis-javascript-1](/HackThis/resimler/hackthis-javascript-1.png)

## Level 2

Sayfanın kaynak kodunu incelersek:

```javascript
<script type='text/javascript'> $(function(){ $('.level-form').submit(function(e){ e.preventDefault(); if ($('.level-form #pass')[0].value.length == length) { document.location = "2?x=" + length; } else { alert('Incorrect Password'); } }); }); </script>
```

Bizim girdiğimiz inputun uzunluğu "length" değerine eşit olması gerekiyor. Bu değer ise bir script ile belirlenmiş:

```javascript
<script type='text/javascript'>
    var length = 5;
    var x = 3;
    var y = 2;
    y = Math.sin(118.13);
    y = -y;
    x = Math.ceil(y);
    y++;
    y = y+x+x;
    y *= (y/2);
    y++;
    y++;
    length = Math.floor(y);
</script>
```

Bu işlemleri ellede yapabilirsiniz fakat hiç gerek yok. Doğrudan javascritp konsolundan yazdırmak daha kolay.

![hackthis-javascript-2](/HackThis/resimler/hackthis-javascript-2.png)

Ben bu seviyeyi geçtiğimde konsoldan yazdırmayı bilmediğim için işlemleri tek tek javascript idesi üzerinden yapıp sonucu bulmuştum fakat siz öyle yapmayın.

## Level 3

Sayfanın kaynak kodunu incelersek:

```javascript
<script type='text/javascript'> var thecode = 'code123'; $(function(){ $('.level-form').submit(function(e){ e.preventDefault(); if ($('.level-form #pass')[0].value == thecode) { document.location = "?pass=" + thecode; } else { alert('Incorrect Password'); } }); }); </script>
```

Bu kodda girdiğimiz şifrenin `thecode` değişkeninin değerine eşit olması gerekiyor. Kodda Bu değişkenin değeri "code123". Bu değeri girersek: **BOOOOM**

Sifre hatalı hatasını alıyoruz. Peki ne oluyor burada!!!  

Bir web sayfası yüklendiğinde aslında html dosyasındaki javascript kodlarından daha fazlası yüklenir. Resimler, belgeler, videolar vs. Aynı zamanda web sayfasının kullanacağı javascript dosyaları! Yani ".js" uzantılı dosyalar. Bizim burada yapmamız gereken web sayfası ile birlikte inen diğer dosyaları yani ".js" uzantılı dosyaları incelememiz gerekiyor.

![hackthis-javascript-3](/HackThis/resimler/hackthis-javascript-3.png)

Bu inen js dosyalarından "main.js" javascript dosyasının içinde bir satırlık kod.

```javascript
var thecode = 'getinthere';
```

Burada `thecode` değişkeni oluşturulmuş ve değeri "getinthere" olarak atanmış. Web sayfası yüklenirken önce html sonra diğer dosyalar yüklenir. Yani html de tanımlanan değişkenin değeri değil main.js dosyasındaki değer geçerli olur. Çünkü son atanan değer geçerlidir.

En kolayı yine konsoldan yazdırmak. Bir sürü dosyayı incelemekten kurtarır :)

## Level 4

Sayfanın kaynak kodunu indelediğimizde bir şey bulamıyoruz. ".js" dosyaları dahil. Peki ne yapacağız?

İpucuna baktığımızda bu sayfanın aradığımız sayfa olmadığını anlıyoruz.
>This isn't the page I was looking for...

Sayfanın urlsine baktığımızda ise bir farklılık var.  **?input** diğer seviyelerde yoktu. "www.hackthis.co.uk/levels/javascript/4?input"

Peki hangi sayfayı arıyoruz. Bu seviyedeki olayı farketmek biraz zor. Bunu anlamanın en iyi yolu sayfanın yüklenişini konsol üzerinden incelemek.

www.hackthis.co.uk/levels/javascript/4

Sayfa yüklenirken sanki yeniden yüklendiğini görmeniz gerekiyor. Peki bu nasıl oluyor. bunun için bu sayfanın kaynak kodunu incelememiz gerekiyor.

"view-source:www.hackthis.co.uk/levels/javascript/4"

```javascript
<script> document.location = '?input'; </script>
<div class='center'>The password is: smellthecheese</div>
```

Burada şifreyi görebiliyoruz: `smellthecheese`  
Şifrenin bir üst satırında `document.location = '?input'` ise bizi diğer sayfaya yönlendiriyor. yani sonu `?input` olan sayfaya. Burada javascript ile başka bir sayfaya yönlendirme yapılmış. Hepsi bu kadar.

Bu soruyu tarayıcıdan javascript'i devre dışı bırakarakta yapabiliriz. bu sayede kodun bizi diğer sayfaya yönlendirmesine engel olmuş oluruz.

## Level 5

Seviye 5 e girer girmez bize bir şifre soruyor. Eğer şifreyi yanlış girersek yada girmezsek bizi seviyelerin olduğu sayfaya atıyor.

Tam şifre girme sırasında sayfanın değişmemesi için tarayıcıdan çarpı işaretine basarak sayfanın bu durumda kalmasını sağlayabiliriz. Yada tarayıcıdan javascript'i devre dışı bırakarak.

Sayfanın kaynak kodunu incelersek doğrudan bir şey bulamıyoruz! Sayfa ile yüklenen diğer ".js" dosyalarını inceleyelim.

```javascript
<script type='text/javascript' src='/files/js/min/main.js?1406192611'></script>
<script type='text/javascript' src='/files/js/min/extra_48d468a93b.js?1406320915'></script>
```

Hadi "extra_48d468a93b.js" dosyasını inceleyelim.

```javascript
a=window.location.host+"";b=a.length;c=4+((5*10)*2);d=String.fromCharCode(c,-(41-Math.floor(1806/13)),Math.sqrt(b-2)*29,(b*8)-29);p=prompt("Password:","");if(p==d){window.location="?pass="+p;}else{window.location="/levels/";
```

Buradaki fonksiyon bu işi gerçekleştiriyor. buradaki "d" değişkeni parola: `hats`

Bu seviyeyi böyle geçmeye çalışmak tam bir angarya. Gelin daha kısa bir yoldan yapalım:

```javascript
Object.keys( window );
```

Bu fonksiyon web sayfasındaki bütün değişkenleri listeler. Konsoldan bunu çalıştırırsak:

```javascript
["top", "window", "location", "external", "chrome", "document", "NREUM", "__nr_require", "$", "jQuery", "io", "html5", "Modernizr", "yepnope", "_gs", "timeSince", "timeString", "PopupCenter", "createCookie", "FavCounter", "loggedIn", "thecode", "_idl", "timer_start", "hljs", "socket", "favcounter", "counter_chat", "counter_notifications", "searchsuggest", "set", "a", "b", "c", "d", "p", "__commandLineAPI"]
```

Değişkenler aslında daha fazla. Ben gerekli olan kısmı yazdım.  
Artık değişkenleri biliyoruz. Buradai a b c d p hemen gözümüze çarpıyor. Bunları sırayla konsoldan yazdırarakta bulabiliriz.

![hackthis-javascript-5](/HackThis/resimler/hackthis-javascript-5.png)
