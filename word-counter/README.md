# Kelime Sayacı ve Frekans Analizi

Bu Python projesi, verilen bir metin dosyasındaki her kelimenin kaç kez geçtiğini sayar ve en sık kullanılan kelimeleri listeler.

## 🎯 Özellikler

- **Dosya Analizi**: Metin dosyalarını otomatik olarak analiz eder
- **Metin Analizi**: Doğrudan metin girişi ile analiz yapar
- **Kelime Arama**: Belirli kelimelerin frekansını bulur
- **İstatistikler**: Detaylı kelime istatistikleri sunar
- **Sıralama**: En sık kullanılan kelimeleri listeler
- **Dışa Aktarma**: Sonuçları dosyaya kaydeder

## 📋 Gereksinimler

- Python 3.6+
- Herhangi bir harici kütüphane gerektirmez

## 🚀 Kurulum ve Çalıştırma

```bash
# Projeyi klonlayın
git clone <repository-url>
cd word-counter

# Programı çalıştırın
python word_counter.py
```

## 💡 Kullanım

### Menü Seçenekleri

1. **📄 Dosya Analiz Et**: Metin dosyasını analiz eder
2. **📝 Metin Analiz Et**: Doğrudan metin girişi ile analiz yapar
3. **🔍 Kelime Ara**: Belirli bir kelimenin frekansını bulur
4. **📊 İstatistikleri Göster**: Genel istatistikleri görüntüler
5. **🏆 En Sık Kullanılan Kelimeler**: Popüler kelimeleri listeler
6. **💾 Sonuçları Dosyaya Kaydet**: Analiz sonuçlarını kaydeder
7. **❌ Çıkış**: Programdan çıkar

### Örnek Kullanım

```
📚 KELİME SAYACI VE FREKANS ANALİZİ
============================================================

📋 MENÜ:
1. 📄 Dosya analiz et
2. 📝 Metin analiz et
3. 🔍 Kelime ara
4. 📊 İstatistikleri göster
5. 🏆 En sık kullanılan kelimeleri göster
6. 💾 Sonuçları dosyaya kaydet
7. ❌ Çıkış

Seçiminizi yapın (1-7): 1
📁 Analiz edilecek dosya yolunu girin: sample.txt
✅ 'sample.txt' dosyası başarıyla analiz edildi!

============================================================
📊 KELİME ANALİZİ İSTATİSTİKLERİ
============================================================
📝 Toplam kelime sayısı: 1,234
🔤 Benzersiz kelime sayısı: 456
📈 Ortalama kelime tekrarı: 2.71

🏆 EN SIK KULLANILAN 10 KELİME
----------------------------------------
 1. python           45 kez ( 3.65%)
 2. programlama      32 kez ( 2.59%)
 3. kod              28 kez ( 2.27%)
 4. veri             25 kez ( 2.03%)
 5. analiz           22 kez ( 1.78%)
```

## 🔧 Teknik Detaylar

- **Metin Temizleme**: Regex ile noktalama işaretlerini kaldırır
- **Kelime Sayımı**: `collections.Counter` ile verimli sayım
- **Dosya İşleme**: UTF-8 kodlama desteği
- **Hata Yönetimi**: Dosya okuma ve yazma hatalarını yakalar
- **Kullanıcı Arayüzü**: İnteraktif menü sistemi

## 📊 Analiz Özellikleri

- **Toplam Kelime Sayısı**: Metindeki tüm kelimelerin sayısı
- **Benzersiz Kelime Sayısı**: Farklı kelimelerin sayısı
- **Ortalama Tekrar**: Kelime başına ortalama tekrar sayısı
- **Frekans Yüzdesi**: Her kelimenin toplam içindeki oranı
- **Sıralama**: En sık kullanılan kelimelerden en az kullanılanlara

## 📁 Desteklenen Dosya Formatları

- `.txt` - Düz metin dosyaları
- `.md` - Markdown dosyaları
- `.py` - Python kod dosyaları
- `.json` - JSON dosyaları (metin içeriği)
- Diğer metin tabanlı dosyalar

## 💾 Çıktı Formatı

Analiz sonuçları şu formatta kaydedilir:
```
KELİME FREKANS ANALİZİ
==================================================

Toplam kelime sayısı: 1234
Benzersiz kelime sayısı: 456

EN SIK KULLANILAN KELİMELER
------------------------------
python              45 ( 3.65%)
programlama         32 ( 2.59%)
kod                 28 ( 2.27%)
```

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.
