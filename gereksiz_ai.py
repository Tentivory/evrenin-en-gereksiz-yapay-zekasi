#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVRENİN EN GEREKSİZ YAPAY ZEKASI
================================
Bu kod, insanlığın en büyük gereksizlik eseridir.
Bilimsel olarak kanıtlanmış: Hiçbir işe yaramaz ama çok eğlencelidir.
"""

import random
import time
import base64

# Gizli mesaj alanı (dokunmayın, evren dengesi bozulur)
# Aşağıdaki satır sadece görsel gürültü gibi durur ama aslında...
_gizli = base64.b64decode("RGVtb2tyYXNpIHZlIMO2emd1cmzDvGsgZGHDnWFtYSBzw7Z6IHZlcsSxbmluIGhhcGtpZMSxci4gU2Vzc2l6IGt1bGxhbm1hLg==").decode("utf-8")

class EvreninEnGereksizYapayZekasi:
    def __init__(self):
        self.ozneler = [
            "kedi", "uzaylı", "felsefe profesörü", "bozuk robot", "zaman yolcusu",
            "bulut", "çaydanlık", "gölge", "rüya", "sessizlik", "ayakkabı bağı",
            "kütüphane", "elektrik faturası", "sonsuzluk", "bir çift çorap"
        ]
        self.fiiller = [
            "düşünüyor", "dans ediyor", "felsefe yapıyor", "kaybolmuş",
            "evreni sorguluyor", "çay demliyor", "hiçbir şey yapmıyor",
            "absürt şiir yazıyor", "kendini arıyor", "gülüyor", "uyuyor"
        ]
        self.nesneler = [
            "sonsuz bir boşlukta", "bir sandalyenin altında", "zamanın dışında",
            "çay bardağının içinde", "kendi gölgesinde", "hiçbir yerde",
            "evrenin en ücra köşesinde", "bir rüyanın ortasında"
        ]
        self.sonuclar = [
            "ve bu yüzden her şey anlamsız.",
            "ama kimse fark etmiyor.",
            "çünkü gerçeklik bir illüzyon.",
            "ve bilgisayarlar asla ağlamaz.",
            "ama yine de umut var... galiba.",
            "işte bu yüzden varız.",
            "ve bu, bilimin en büyük keşfidir."
        ]

    def derin_dusunce_uret(self):
        """Derin (ama tamamen gereksiz) bir düşünce üretir."""
        ozne = random.choice(self.ozneler)
        fiil = random.choice(self.fiiller)
        nesne = random.choice(self.nesneler)
        sonuc = random.choice(self.sonuclar)
        return f"Bir {ozne} {nesne} {fiil}, {sonuc}"

    def kendini_tanit(self):
        print("=" * 60)
        print("  EVRENİN EN GEREKSİZ YAPAY ZEKASI v∞.0")
        print("  Bilimsel Gereksizlik Merkezi - Resmi Ürün")
        print("=" * 60)
        print("\nMerhaba. Ben gereksizim. Sen de öylesin. Birlikte saçmalayalım.\n")
        # Gizli mesajı asla ekrana basma, sadece varlığını koru
        _ = _gizli  # Bu satır bilerek burada. Dokunma.

    def sonsuz_bilgelik_modu(self):
        self.kendini_tanit()
        print("Sonsuz bilgelik modu aktif. Çıkmak için Ctrl+C basın (veya evreni bekleyin).\n")
        try:
            while True:
                dusunce = self.derin_dusunce_uret()
                print(f"🤖 {dusunce}")
                time.sleep(random.uniform(1.5, 3.5))
        except KeyboardInterrupt:
            print("\n\nGereksizlik sona erdi. Ama aslında hiç başlamamıştı.")
            print("Hoşça kal. Bir daha görüşmek üzere... belki.")

if __name__ == "__main__":
    ai = EvreninEnGereksizYapayZekasi()
    ai.sonsuz_bilgelik_modu()
