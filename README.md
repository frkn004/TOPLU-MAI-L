# Toplu E-Posta Gönderme Script'i

Bu script, bir CSV dosyasındaki alıcılara toplu e-posta göndermek için geliştirilmiştir.

## Nasıl Kullanılır?

1. **Gerekli Kütüphaneleri Yükleyin**:
    - Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:
    ```bash
    pip install -r requirements.txt
    ```

2. **Çevre Değişkenlerini Ayarlayın**:
    - Gönderici e-posta adresinizi ve uygulama şifrenizi çevre değişkenleri olarak ayarlayın:
    ```bash
    export SENDER_EMAIL="your_email@gmail.com"
    export EMAIL_PASSWORD="your_application_password"
    ```

3. **Script'i Çalıştırın**:
    - Script'i çalıştırarak e-postaları gönderin:
    ```bash
    python send_bulk_email_secure.py
    ```

4. **CSV Dosyası**:
    - Alıcıların e-posta adreslerini ve diğer bilgilerini içeren bir CSV dosyası oluşturun.

## Notlar:
- Şifrenizi ve diğer hassas bilgilerinizi kodda tutmayın, çevre değişkenleri kullanın.
- Eğer Google hesabı kullanıyorsanız, iki adımlı doğrulama etkin olmalıdır ve uygulama şifresi kullanmalısınız.

## Gereksinimler

- Python 3.7 veya üzeri
- Aşağıda listelenen kütüphaneler
