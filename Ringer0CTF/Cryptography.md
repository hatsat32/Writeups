# Cryptography

[Ringzer0ctf](https://ringzer0ctf.com/) sitesinde yer alan CTF sorularının çözümleri ve ayrıntılı açıklamaları. Umarım faydası olur. Başarılar...

## Some martian message

Sezar şifrelemesi. Bilinen en eski şifreleme yöntemlerinden bir tanesidir. Harflarin alfabede belli bir sayı kadar kaydırılması ile oluşturulur. İnternette herhangi bir site ile deşifre edebilirsiniz.

```text
SYNTPrfneVfPbbyOhgAbgFrpher
```

Deşifre edilmiş hali:

```text
FLAGCESARISCOOLBUTNOTSECURE
```

## You're drunk!

Alphabetical Substitution şifrelemesi. Yani herfleri başka bir harfle eşleştirme ile şifrelemesi şifrelenmesidir. Bu şifreleme tekniği frekans saldırısına karşı zafiyeti vardır.

Her neyse. Bu metni [şu adresteki](https://www.dcode.fr/monoalphabetic-substitution) araç yardımı ile decode edebilirsiniz. Bu işlem için biraz ingilizce bilgisi gerekebilir.

```text
Ayowe awxewr nwaalfw die tiy rgw fklf ua xgixiklrw! Tiy lew qwkxinw.
```

Şifrenin çözülmüş hali:

```text
super secret message for you the glag is CHOCOLATE! you are welcome.
```

Ve flag:

```text
CHOCOLATE
```

## File recovery

Tar arşivini indirip dosyaları çıkardıktan sonra `file` komutu ile inceliyorum. Dosyaların ne dosyası olduğunu anlamak için.

```text
┌─[hatsat@HATSAT]─[~/Downloads/flag]
└──╼ $file flag.enc
flag.enc: data
┌─[hatsat@HATSAT]─[~/Downloads/flag]
└──╼ $file private.pem
private.pem: PEM RSA private key
```

Buradan anlıyorum ki flan.enc dosyası rsa algoritması ile şifrelenmiş ve private anahtar elimizde. İnternette biraz araştırma yaptıktan sonra [şu siteden](https://linuxtiwary.com/2018/08/25/public-key-and-private-key-encryption-decryption-labasymmetric-cryptography/) nasıl decrypt edebileceğimi öğrendim. Gerisi sadeco komutları çalıştırmak.

```text
┌─[hatsat@HATSAT]─[~/Downloads/flag]
└──╼ $openssl rsautl -decrypt -inkey private.pem -in flag.enc -out text.txt
┌─[hatsat@HATSAT]─[~/Downloads/flag]
└──╼ $cat text.txt
FLAG-vOAM5ZcReMNzJqOfxLauakHx
```

Flagimizi elde ettik.

```text
FLAG-vOAM5ZcReMNzJqOfxLauakHx
```

## Martian message part 2

Birkaç başarısız deneme ve araştırmadan sonra şifreleme metodunun vinegere cipher olduğunu buldum. Bu andan itibaren tek yapmamız gereken bir araç yardımıyla şifreyi decrypt etmek. Ben bu iş için [dcode](https://www.dcode.fr/vigenere-cipher) sitesini kullandım. Hem şifrelemenin nasıl çalıştığı ile ilgili bir açıklamada var.

```text
metin:
KDERE2UNX1W1H96GYQNUSQT1KPGB

key:
fselkladfklklakl
```

Flag şu şekilde:

```text
FLAGU2JNU1R1X96VOFNKHLB1GEWQ
```

## Fashion Victim

Virual cryptography.

![fashion victim](/Ringer0CTF/resimler/cryptography/fashion-victim-1.png)

## Public key recovery
