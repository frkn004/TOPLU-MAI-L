import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import os

# Ayarları Dışarıdan Okumak (Güvenlik için!)
try:
    with open('email_config.txt', 'r') as config_file:
        smtp_server = config_file.readline().strip()
        smtp_port = int(config_file.readline().strip())
        sender_email = config_file.readline().strip()
        password = config_file.readline().strip()
except FileNotFoundError:
    print("Hata: email_config.txt dosyası bulunamadı!")
    exit(1)  # Programı durdur

# E-posta İçeriği (Değişkenler ile Daha Düzenli)
subject = "Staj Başvurusu"
names = ["Furkan Sevinç", "Nisa Duru", "Mevlüt Kaya"]
phones = ["number"]
emails = ["mail"]
linkedins = ["linkedin"]

body_template = """Sayın Firma Yetkilisi,

Biz, Ostim Teknik Üniversitesi Yapay Zeka Mühendisliği öğrencileri olarak, yazılım alanında staj yapma hedefimiz doğrultusunda firmanızın değerli bir deneyim fırsatı sunabileceğine inanıyoruz. {name1}, {name2} ve {name3} olarak üç arkadaş, teknik bilgi birikimimizi ve öğrendiğimiz teorik bilgileri pratiğe dökme noktasında sizinle çalışmak istiyoruz.

Gelişmiş yazılım projelerinde yer alarak, takım çalışması ve profesyonel ortam tecrübemizi arttırmak, aynı zamanda firmanızın projelerine katkı sağlamak amacındayız. Özellikle Makine Öğrenimi ve Yapay Zeka alanında yetkinliklerimizi geliştirmek istiyoruz.

Staj başvurumuzu değerlendirmeniz ve bir görüşme için zaman ayırmanız bizi çok mutlu edecektir. Ekli dosyada özgeçmişlerimizi ve detaylı bilgileri bulabilirsiniz.

Zaman ayırdığınız için teşekkür eder, olumlu geri dönüşlerinizi bekleriz.

Saygılarımızla,

{name1}
{phone1}
{email1}
{linkedin1}

{name2}
{phone2}
{email2}
{linkedin2}

{name3}
{phone3}
{email3}
{linkedin3}
"""

body = body_template.format(name1=names[0], phone1=phones[0], email1=emails[0], linkedin1=linkedins[0],
                           name2=names[1], phone2=phones[1], email2=emails[1], linkedin2=linkedins[1],
                           name3=names[2], phone3=phones[2], email3=emails[2], linkedin3=linkedins[2])

# Dosya İşlemleri (Dinamikleştirme)
file_paths = [f"{name.lower().replace(' ', '')}.pdf" for name in names]

# E-posta Gönderimi (Hata Yönetimi ile Daha Sağlam)
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, password)

    with open('deneme.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            recipient = row[0]
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            for file_path in file_paths:
                try:
                    with open(file_path, 'rb') as f:
                        attachment = MIMEBase('application', 'pdf')
                        attachment.set_payload(f.read())
                        encoders.encode_base64(attachment)
                        attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
                        msg.attach(attachment)
                except FileNotFoundError:
                    print(f"Uyarı: {file_path} dosyası bulunamadı, e-postaya eklenmedi.")

            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"{recipient} adresine e-posta gönderildi.")

print("Tüm e-postalar başarıyla gönderildi.")
