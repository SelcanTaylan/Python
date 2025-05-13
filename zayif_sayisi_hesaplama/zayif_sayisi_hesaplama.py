ders_notlari=[]
toplam=0
zayif_sayisi=0

for i in range (6):
    ders_notlari.append(int(input("ders notu girin:")))

for ders_notu in ders_notlari:
    toplam=toplam+ders_notu
    if ders_notu<50:
        zayif_sayisi=zayif_sayisi +1

ortalama = toplam / len(ders_notlari)  


print("ders notları ortalaması:",ortalama)
print("öğrencinin zayıf sayısı:",zayif_sayisi)