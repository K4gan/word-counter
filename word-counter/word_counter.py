#!/usr/bin/env python3
"""
Kelime Sayacı ve Frekans Analizi
Verilen bir metin dosyasındaki her kelimenin kaç kez geçtiğini sayar ve en sık kullanılan kelimeleri listeler.
"""

import re
import sys
from collections import Counter
from pathlib import Path


class WordAnalyzer:
    def __init__(self):
        self.word_count = Counter()
        self.total_words = 0
        self.unique_words = 0
        
    def clean_word(self, word):
        """Kelimeyi temizler - noktalama işaretlerini kaldırır"""
        return re.sub(r'[^\w]', '', word.lower())
    
    def analyze_file(self, file_path):
        """Dosyayı analiz eder"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                return self.analyze_text(content)
        except FileNotFoundError:
            print(f"❌ Dosya bulunamadı: {file_path}")
            return False
        except UnicodeDecodeError:
            print(f"❌ Dosya okunamadı (kodlama hatası): {file_path}")
            return False
        except Exception as e:
            print(f"❌ Dosya okuma hatası: {e}")
            return False
    
    def analyze_text(self, text):
        """Metni analiz eder"""
        # Kelimeleri ayır ve temizle
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Kelime sayımını yap
        self.word_count = Counter(words)
        self.total_words = len(words)
        self.unique_words = len(self.word_count)
        
        return True
    
    def get_top_words(self, n=10):
        """En sık kullanılan N kelimeyi döndürür"""
        return self.word_count.most_common(n)
    
    def get_word_frequency(self, word):
        """Belirli bir kelimenin frekansını döndürür"""
        return self.word_count.get(word.lower(), 0)
    
    def print_statistics(self):
        """İstatistikleri yazdırır"""
        print("=" * 60)
        print("📊 KELİME ANALİZİ İSTATİSTİKLERİ")
        print("=" * 60)
        print(f"📝 Toplam kelime sayısı: {self.total_words:,}")
        print(f"🔤 Benzersiz kelime sayısı: {self.unique_words:,}")
        print(f"📈 Ortalama kelime tekrarı: {self.total_words/self.unique_words:.2f}")
        print()
    
    def print_top_words(self, n=10):
        """En sık kullanılan kelimeleri yazdırır"""
        top_words = self.get_top_words(n)
        
        print(f"🏆 EN SIK KULLANILAN {n} KELİME")
        print("-" * 40)
        for i, (word, count) in enumerate(top_words, 1):
            percentage = (count / self.total_words) * 100
            print(f"{i:2d}. {word:<15} {count:>6} kez ({percentage:5.2f}%)")
        print()
    
    def search_word(self, word):
        """Belirli bir kelimeyi arar"""
        count = self.get_word_frequency(word)
        if count > 0:
            percentage = (count / self.total_words) * 100
            print(f"🔍 '{word}' kelimesi {count} kez geçiyor ({percentage:.2f}%)")
        else:
            print(f"❌ '{word}' kelimesi bulunamadı")
    
    def export_results(self, output_file):
        """Sonuçları dosyaya aktarır"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("KELİME FREKANS ANALİZİ\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Toplam kelime sayısı: {self.total_words}\n")
                f.write(f"Benzersiz kelime sayısı: {self.unique_words}\n\n")
                
                f.write("EN SIK KULLANILAN KELİMELER\n")
                f.write("-" * 30 + "\n")
                for word, count in self.get_top_words(50):
                    percentage = (count / self.total_words) * 100
                    f.write(f"{word:<20} {count:>6} ({percentage:5.2f}%)\n")
            
            print(f"✅ Sonuçlar '{output_file}' dosyasına kaydedildi")
        except Exception as e:
            print(f"❌ Dosya yazma hatası: {e}")


def main():
    """Ana program fonksiyonu"""
    print("=" * 60)
    print("📚 KELİME SAYACI VE FREKANS ANALİZİ")
    print("=" * 60)
    
    analyzer = WordAnalyzer()
    
    while True:
        print("\n📋 MENÜ:")
        print("1. 📄 Dosya analiz et")
        print("2. 📝 Metin analiz et")
        print("3. 🔍 Kelime ara")
        print("4. 📊 İstatistikleri göster")
        print("5. 🏆 En sık kullanılan kelimeleri göster")
        print("6. 💾 Sonuçları dosyaya kaydet")
        print("7. ❌ Çıkış")
        
        try:
            choice = input("\nSeçiminizi yapın (1-7): ").strip()
            
            if choice == '1':
                file_path = input("📁 Analiz edilecek dosya yolunu girin: ").strip()
                if file_path and Path(file_path).exists():
                    if analyzer.analyze_file(file_path):
                        print(f"✅ '{file_path}' dosyası başarıyla analiz edildi!")
                        analyzer.print_statistics()
                else:
                    print("❌ Geçersiz dosya yolu!")
            
            elif choice == '2':
                print("📝 Analiz edilecek metni girin (bitirmek için 'END' yazın):")
                lines = []
                while True:
                    line = input()
                    if line.strip() == 'END':
                        break
                    lines.append(line)
                
                text = '\n'.join(lines)
                if text.strip():
                    analyzer.analyze_text(text)
                    print("✅ Metin başarıyla analiz edildi!")
                    analyzer.print_statistics()
                else:
                    print("❌ Boş metin!")
            
            elif choice == '3':
                if analyzer.total_words == 0:
                    print("❌ Önce bir dosya veya metin analiz edin!")
                    continue
                
                word = input("🔍 Aranacak kelimeyi girin: ").strip()
                if word:
                    analyzer.search_word(word)
                else:
                    print("❌ Geçersiz kelime!")
            
            elif choice == '4':
                if analyzer.total_words == 0:
                    print("❌ Önce bir dosya veya metin analiz edin!")
                    continue
                analyzer.print_statistics()
            
            elif choice == '5':
                if analyzer.total_words == 0:
                    print("❌ Önce bir dosya veya metin analiz edin!")
                    continue
                
                try:
                    n = int(input("Kaç kelime gösterilsin? (varsayılan: 10): ") or "10")
                    analyzer.print_top_words(n)
                except ValueError:
                    analyzer.print_top_words()
            
            elif choice == '6':
                if analyzer.total_words == 0:
                    print("❌ Önce bir dosya veya metin analiz edin!")
                    continue
                
                output_file = input("💾 Çıktı dosya adı (varsayılan: word_analysis.txt): ").strip()
                if not output_file:
                    output_file = "word_analysis.txt"
                analyzer.export_results(output_file)
            
            elif choice == '7':
                print("👋 Programdan çıkılıyor...")
                break
            
            else:
                print("❌ Geçersiz seçim! Lütfen 1-7 arası bir sayı girin.")
        
        except KeyboardInterrupt:
            print("\n👋 Programdan çıkılıyor...")
            break
        except Exception as e:
            print(f"❌ Hata oluştu: {e}")


if __name__ == "__main__":
    main()
