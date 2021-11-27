## Faktoriyel Hesaplama Birinci Yol

faktoriyel = 1

sayi = int(input("Sayı Giriniz: "))

if sayi == 0:
    print("Cevap 1")

elif sayi < 0:
    print("Negatif Sayıların Faktoriyeli Yoktur.")


for i in range(1,sayi+1):
    faktoriyel = faktoriyel * i
    print("Cevap: ",faktoriyel)

## Faktoriyel Hesaplaması için İkinci Yol

sayi=int(input("Faktoriyeli alınacak sayıyı giriniz : "))
carpim=1

for i in range(sayi):
    carpim*=i+1

print(carpim)


## Faktoriyel Hesaplama Üçüncü Yol

def faktoriyel():
    faktoriyel = 1

    sayi = int(input("Sayı Giriniz: "))

    if sayi == 0:
        print("Cevap 1")
    elif sayi < 0:
        print("Negatif Sayıların Faktoriyeli Yoktur.")

    for i in range(1,sayi+1):
        faktoriyel = faktoriyel * i
        print("Cevap: ",faktoriyel)        

faktoriyel()



