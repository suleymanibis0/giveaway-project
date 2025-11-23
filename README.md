# 🎲 Modern Giveaway Tool (PyQt6)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![PyQt6](https://img.shields.io/badge/PyQt6-Desktop_GUI-green?style=for-the-badge&logo=qt)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**Python ve PyQt6 kullanılarak geliştirilmiş, modern arayüze sahip, animasyonlu ve veri kalıcılığı (persistence) sağlayan masaüstü çekiliş uygulaması.**

<p align="center">
  <img src="SCREENSHOT_LINKI_BURAYA" alt="Uygulama Ekran Görüntüsü" width="600">
</p>

## 🚀 Proje Hakkında

Bu proje, basit bir çekiliş yapma ihtiyacını profesyonel bir masaüstü deneyimine dönüştürmek için geliştirilmiştir. Standart `random` fonksiyonlarının ötesine geçerek, kullanıcıya heyecan veren bir **yavaşlama animasyonu (deceleration effect)** ve kullanıcı hatalarını önleyen bir **session restore (oturum kurtarma)** mekanizması içerir.

## ✨ Özellikler

* **🎨 Modern Arayüz:** Qt Designer ile tasarlanmış, kullanıcı dostu "Dark Mode" arayüz.
* **⏱️ Akıllı Animasyon Algoritması:** Kazananı hemen göstermek yerine, `QTimer` kullanılarak hızla başlayıp giderek yavaşlayan bir "Çarkıfelek" efekti.
* **💾 Veri Kalıcılığı (Persistence):** Uygulama yanlışlıkla kapatılsa bile katılımcı listesi `participants.txt` üzerinden korunur. Çekiliş tamamlandığında otomatik temizlenir.
* **🛡️ Hata Yönetimi (Error Handling):** Boş girişler, yetersiz katılımcı sayısı ve dosya okuma hatalarına karşı `try-except` blokları ve `QMessageBox` uyarıları.
* **📦 Tek Dosya Dağıtım:** `PyInstaller` ve `sys._MEIPASS` kullanılarak kaynak dosyaları (ikonlar vb.) içine gömülmüş tek bir `.exe` dosyası.
* **🖼️ Windows Entegrasyonu:** Görev çubuğu ikon sorunları `ctypes` kütüphanesi ile çözülmüştür.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.11+
* **GUI Framework:** PyQt6
* **Paketleme:** PyInstaller
* **Diğer:** `random`, `os`, `sys`, `ctypes`

## ⚙️ Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Repoyu klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ.git](https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ.git)
    cd REPO_ADINIZ
    ```

2.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install PyQt6 pyinstaller
    ```

3.  **Uygulamayı başlatın:**
    ```bash
    python main.py
    ```

## 📦 EXE Oluşturma (Build)

Uygulamayı tek bir çalıştırılabilir dosya (.exe) haline getirmek için şu komutu kullanın:

```bash
pyinstaller --noconsole --onefile --icon=app_icon.ico --add-data "app_icon.ico;." main.py
Not: Bu komut, ikon dosyasını exe'nin içine gömer ve dist klasöründe çalışmaya hazır bir dosya oluşturur.



🧠 Koddan Kesitler (Algoritma)
Projenin kalbi olan "Yavaşlama Animasyonu" mantığı:

Python

def on_timer_tick(self):
    # ...
    # Her adımda timer süresini artırarak (yavaşlatarak) gerçekçi bir efekt yaratıyoruz
    self.current_speed += 20 
    self.timer.setInterval(self.current_speed)
    
    # Belirli bir tur sayısı ve yavaşlık seviyesine ulaşınca durur
    if self.counter > self.MIN_STEPS and self.current_speed >= 500:
        self.timer.stop()
        # ... Kazananı ilan et


🤝 Katkıda Bulunma
Bu projeyi Fork'layın.

Yeni bir özellik dalı (branch) oluşturun (git checkout -b feature/YeniOzellik).

Değişikliklerinizi commit edin (git commit -m 'Yeni özellik eklendi').

Dalınızı Push edin (git push origin feature/YeniOzellik).

Bir Pull Request oluşturun.

Developed with ❤️ by [Senin Adın]