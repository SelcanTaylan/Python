liste = []
toplam = 0

for i in range(8):
    liste.append(int(input("Bir sayı girin: ")))

for sayi in liste:
    if sayi % 2 == 0:  # Sayının çift olup olmadığını kontrol ediyoruz
        toplam += sayi

print("Toplam:", toplam)
