print("""
------------------------------------------
SAYI TAHMİN OYUNU
*Bilgisayarın 1 ile 40 Arasında Rastgele Belirlediği Sayıyı 5 Seferde Bulmaya Çalışın
------------------------------------------""")
import random
import time

rastgelesayı=random.randint(1,40)
tahminhakkı=5

while True:
    tahmin=int(input("Lütfen Tahmininizi Giriniz:"))
    print("Bilgiler Sorgulanıyor...")
    time.sleep(1)

    if tahmin>rastgelesayı:
        print("Lütfen Daha Küçük Bir Sayı Giriniz!")
        tahminhakkı-=1
        print("Kalan Tahmin Hakkı:",tahminhakkı)
    elif tahmin<rastgelesayı:
        print("Lütfen Daha Büyük Bir Sayı Giriniz!")
        tahminhakkı-=1
        print("Kalan Tahmin Hakkı:", tahminhakkı)
    else:
        print("Tebrikler Doğru Sayı:",rastgelesayı)

    if tahminhakkı==0:
        print("Tahmin Hakkınız Bitti!!!")
        break

