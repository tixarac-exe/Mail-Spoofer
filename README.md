# TOOL
Bu bir mail spoofing (sahte e-posta gönderme) aracıdır. Python ile yazılmıştır ve komut satırı üzerinden çalışır. Temel amacı, kullanıcı tarafından belirlenen sahte bir gönderici adı ve e-posta adresiyle alıcıya HTML veya metin içerikli e-posta göndermektir.

Araç şu şekilde çalışır:

Kullanıcıdan sahte gönderici adı (örneğin: "Apple Destek"), gerçek alıcı adresi, e-posta konusu ve içerik tipi (HTML şablon, metin dosyası veya manuel içerik) istenir.

İçerikler daha önce hazırlanmış dosyalardan seçilebileceği gibi anlık yazılarak da oluşturulabilir.

SMTP ayarları (sunucu, port, TLS, kullanıcı adı, şifre) ya yapılandırma dosyalarından alınır ya da kullanıcıdan girilir.

Ardından, SMTP sunucusuna bağlanılarak girilen bilgilerle alıcıya e-posta gönderilir. E-postada görünen “Gönderen” bilgisi, aslında maili gönderen hesabın değil, kullanıcı tarafından sahte olarak girilen addır.


Bu tür araçlar siber güvenlik testlerinde, phishing simülasyonlarında veya farkındalık eğitimlerinde kullanılır; ancak izinsiz kullanımı yasa dışı ve etik dışıdır. 

Tüm Kullanım Senaryolarından Kullanıcı Sorumludur.



## Özellikler

- **E-posta Gönderimi:** Gerçek bir e-posta adresinden gönderilmiş gibi görünen sahte e-postalar gönderilebilir.
- **SMTP Entegrasyonu:** Güçlü SMTP sunucusu desteği ile kullanıcılar istedikleri adreslerden e-posta gönderebilir.
- **Özelleştirilebilir Konu ve İçerik:** E-posta konusu ve içeriği tamamen özelleştirilebilir, bu sayede daha etkili phishing saldırıları düzenlenebilir.
- **Kimlik Gizleme:** Gönderen e-posta adresi ve ismi taklit edilebilir, gerçek göndereni gizler.
- **Entegrasyon:** Kullanmak İçin Tek Yapmanız Gereken Toolu Çalıştırıp Linki Oluşturduktan Sonra m3.py yi çalıştıran seçeneği seçip kurbanın maili yazmanız Instagram Şifre Yenileme Email Şablonu Kullandığı İçin Instagram Gibi Davranabilirsiniz



## Config Nasıl Ayarlanmalı
 - **smtp_server:** Bu Kısıma Smtp Serverinizin Adresi Girmeniz Lazım Ücretsiz Ve En Kolay Yöntem Gmail Smtp Kullanmak.
 
- **smtp_port:** Bu Kısıma Serverinizin Smtp Portunu Girmeniz Lazım Eğer Gmail Kullanıyorsanız Buraya 587 Vermeniz Lazım.

- **use_tls:** Bu Kısımda Tls Kullanılmasını İstiyorsanız true'de kalsın Tls Daha Güvenli İletişim Sağlar.

- **from_adress:** Bu Kısım Smtp Serverinize Login Olmak İçin Gereken Mail Veya Kullanıcı Adı Girebilirsiniz Gmail Kullanıyorsanız Bu Servisi Açtığınız Mail Adresidir.

- **password:** Bu Kısıma Smtp Şifrenizi Girmeniz Lazım Eğer Gmail Kullanıyorsanız Gmail Tarafından Hizmet Oluşturulduğunda Verilen Şifreyi girmeniz gerekir.


## Gmail SMTP Kullanma

**Birinci Yol**


- **1**-Öncelikle Gmail Uygulamasına Girip 2 Faktörlü Doğrulamayı Açmanız Lazım Güvenlik Sekmesinden Açabilirsiniz.


- **2**-Gmail Ayarlarında Arama Kısmına Uygulama Şifresi Yazıp Yeni Uygulama Oluşturun Ve Verilen Şifreyi Kaydedin.


- **3**-Configde From Adress Kısmına Sifreyi Oluşturduğunuz Maili Girin.


- **4**-Password Kısmında Verilen Şifreyi Girin.

- **5**-Smtp Port Kısmına 587 (SSL Kullanıcaksanız 465)


- **6**-Smtp Server Kısmında smtp.gmail.com girin.


 **İkinci Yol**


- **1**-Arama Kısmına Daha Az Güvenli Erişim Yazıp Erişime İzin Verin Eğer Çıkmazsa Güvenlik Sekmesinde Bulabilirsiniz.

- **2**-Smtp Port Ve Smtp Server Kısımları Aynı Olucak.

- **3**-From Adressde Aynı Olucak.

- **4**-Password Kendi Mail Şifreniz Olucak.

- **5**-Mail Şifreniz Güvendedir Çünkü Config Dosyası Sadece Sizin Cihazınızda Yer Alır Ve Rat Yemeden Dışardan Erişilmesi Çok Zordurki Zaten Cihazınıza Erişildiyse Muhtemelen Mailiniz Çoktan Ele Geçirilmiştir

## HTML Şablon Ayarlanması
İlk Olarak html şablonları /html altında durmaktadır şablonları toolun kendi clisi üzerinden veya manuel olarak herhangi bir dosya yöneticisi veya Termux üzerinden şablonları yönetebilirsiniz. Tool 2 tane hazır şablonla birlikte gelmektedir biraz eski olsalar bile işlevselikleri sona ermemiştir hazır gelen şablonlardaki yönlendirme linkini kendinize göre düzenlemeniz gerekmektedir. html şablonları daha gerçekçi ve daha güçlü iletiler oluşturmanıza yardımcı olur.

## Kurulum
```
git clone https://github.com/tixarac-exe/Mail-Spoofer/
cd Mail-Spoofer
python sender.py
```
## Sorumluluk Red Beyanı 

Bu Tool Kullanılarak Yapılan Tüm Herşeyden Kullanıcı Sorumludur Bu Tool Sadece Eğitim İçin Kullanılmak Üzere Geliştirildi. Bu Tool İle Yapılan Her İşlemden Kullanıcı Sorumludur.

