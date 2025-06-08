import os
import json
import smtplib
import sys
from threading import Thread
from http.server import HTTPServer, SimpleHTTPRequestHandler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

a = os.path.dirname(os.path.abspath(__file__))
b = os.path.join(a, 'html')
c = os.path.join(a, 'txt')
d = os.path.join(a, 'config')

def e():
    os.system('cls' if os.name == 'nt' else 'clear')

def f():
    try:
        with open('banner.txt', 'r', encoding='utf-8') as g:
            print(g.read())
    except:
        print("banner.txt bulunamadı.")

def h(i):
    j = [k for k in os.listdir(i) if not k.startswith('.')]
    if not j:
        print("Hiç dosya bulunamadı.")
    for l, m in enumerate(j, 1):
        print(f"[{l}] {m}")
    return j

def n(o, p="Bir seçim yapın", q=True):
    for r, s in enumerate(o):
        print(f"{r + 1} - {s}")
    t = input(f"{p} (Numara veya isim): ").strip()
    if t.isdigit():
        u = int(t) - 1
        if 0 <= u < len(o):
            return o[u]
    elif q and t in o:
        return t
    print("Geçersiz seçim!")
    return None

def v():
    w = input("Dosya adı (uzantısız): ") + ".txt"
    x = input("İçeriği girin:\n")
    with open(os.path.join(c, w), 'w', encoding='utf-8') as y:
        y.write(x)
    print(f"{w} oluşturuldu.")

def z():
    aa = h(c)
    ab = int(input("Silmek istediğiniz dosyanın numarası: ")) - 1
    os.remove(os.path.join(c, aa[ab]))
    print(f"{aa[ab]} silindi.")

def ac():
    while True:
        print("\n1. Listele\n2. Sil\n3. Oluştur\n4. Geri Dön")
        ad = input("Seçim: ")
        if ad == '1':
            e()
            h(c)
        elif ad == '2':
            e()
            z()
        elif ad == '3':
            e()
            v()
        elif ad == '4':
            e()
            break

def ae():
    af = input("Dosya adı (uzantısız): ") + ".html"
    ag = input("HTML içeriğini girin:\n")
    with open(os.path.join(b, af), 'w', encoding='utf-8') as ah:
        ah.write(ag)
    print(f"{af} oluşturuldu.")

def ai():
    aj = h(b)
    ak = int(input("Silmek istediğiniz dosyanın numarası: ")) - 1
    os.remove(os.path.join(b, aj[ak]))
    print(f"{aj[ak]} silindi.")

def al(am):
    os.chdir(b)
    an = HTTPServer(('0.0.0.0', am), SimpleHTTPRequestHandler)
    print(f"Sunucu başlatıldı: http://localhost:{am}")
    an.serve_forever()

def ao():
    ap = int(input("Port girin: "))
    aq = Thread(target=al, args=(ap,))
    aq.start()

def ar():
    while True:
        print("\n1. Listele\n2. Sil\n3. Oluştur\n4. Test Et\n5. Geri Dön")
        as_ = input("Seçim: ")
        if as_ == '1':
            e()
            h(b)
        elif as_ == '2':
            e()
            ai()
        elif as_ == '3':
            e()
            ae()
        elif as_ == '4':
            e()
            ao()
        elif as_ == '5':
            e()
            break

def at():
    au = input("Config dosyası adı (uzantısız): ") + ".json"
    av = input("SMTP Sunucusu: ")
    aw = int(input("SMTP Portu: "))
    ax = input("TLS kullanılsın mı? (evet/hayır): ").lower() == 'evet'
    ay = input("Gönderen e-posta: ")
    az = input("Şifre: ")
    ba = {
        "smtp_server": av,
        "smtp_port": aw,
        "use_tls": ax,
        "smtp_mail": ay,
        "smtp_password": az
    }
    with open(os.path.join(d, au), 'w', encoding='utf-8') as bb:
        json.dump(ba, bb, indent=4)
    print(f"{au} oluşturuldu.")

def bc():
    bd = h(d)
    be = int(input("Silmek istediğiniz dosyanın numarası: ")) - 1
    os.remove(os.path.join(d, bd[be]))
    print(f"{bd[be]} silindi.")

def bf():
    while True:
        e()
        print("\n1. Listele\n2. Sil\n3. Oluştur\n4. Geri Dön")
        bg = input("Seçim: ")
        if bg == '1':
            e()
            h(d)
        elif bg == '2':
            e()
            bc()
        elif bg == '3':
            e()
            at()
        elif bg == '4':
            e()
            break

def bh(bi):
    try:
        with open(os.path.join(d, bi), "r", encoding="utf-8") as bj:
            return json.load(bj)
    except Exception as bk:
        print(f"Hata oluştu: {bk}")
        return {}

def bl():
    print("Mail Gönderme Modu Seçildi.")
    bm = h(d)
    if bm:
        bn = n(bm, "Config dosyasını seçin")
    else:
        bn = None

    bo = bh(bn) if bn else {}

    if not bo:
        bp = input("SMTP Server: ")
        bq = int(input("SMTP Port: "))
        br = input("SMTP Mail: ")
        bs = input("SMTP Şifresi: ")
        bt = input("TLS (e/h): ").lower() == 'e'
    else:
        bp = bo["smtp_server"]
        bq = bo["smtp_port"]
        br = bo["smtp_mail"]
        bs = bo["smtp_password"]
        bt = bo["use_tls"]

    bu = input("Spooflanacak Gönderen: ")
    bv = input("Alıcı Mail: ")
    bw = input("Konu: ")

    print("İçerik tipi:")
    print("1 - HTML şablon")
    print("2 - TXT içeriği")
    print("3 - Manuel")
    bx = input("Seçim: ")

    by = ""
    if bx == "1":
        bz = h(b)
        ca = n(bz, "HTML dosyası seçin")
        if ca:
            with open(os.path.join(b, ca), "r", encoding="utf-8") as cb:
                by = cb.read()
    elif bx == "2":
        cc = h(c)
        cd = n(cc, "TXT dosyası seçin")
        if cd:
            with open(os.path.join(c, cd), "r", encoding="utf-8") as ce:
                by = ce.read()
    else:
        by = input("İçeriği girin:\n")

    cf = MIMEMultipart()
    cf['From'] = Header(bu, 'utf-8')
    cf['To'] = Header(bv, 'utf-8')
    cf['Subject'] = Header(bw, 'utf-8')
    cf.attach(MIMEText(by, 'html', 'utf-8'))

    try:
        print("SMTP sunucusuna bağlanılıyor...")
        cg = smtplib.SMTP(bp, bq)
        if bt:
            cg.starttls()
        cg.login(br, bs)
        cg.sendmail(bu, bv, cf.as_string())
        print("E-posta gönderildi.")
    except Exception as ch:
        print(f"Hata: {ch}")
    finally:
        cg.quit()

def ci():
    while True:
        f()
        print("\n--- ANA MENÜ ---")
        print("1. HTML Şablonlarını Yönet")
        print("2. TXT Dosyalarını Yönet")
        print("3. Config Dosyalarını Yönet")
        print("4. E-Posta Gönder")
        print("5. Çıkış")
        cj = input("Seçim: ")
        if cj == '1':
            e()
            ar()
        elif cj == '2':
            e()
            ac()
        elif cj == '3':
            e()
            bf()
        elif cj == '4':
            e()
            bl()
        elif cj == '5':
            e()
            break

if __name__ == "__main__":
    ci()