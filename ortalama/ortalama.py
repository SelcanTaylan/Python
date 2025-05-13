liste=[]
toplam=0
for i in range(6):
    liste.append(int(input("ders notu girin:")))

for ders_notu in liste:
    toplam=toplam+ders_notu
ortalama=toplam/6
print("ortalama:",ders_notu)