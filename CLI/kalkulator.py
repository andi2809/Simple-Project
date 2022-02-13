# name = "Kurniawan Andi Santoso"
# print(name.startswith("kur")) #false karena k huruf kecil
#
# name = ['Kurniawan', 'Andi', 'Santoso']
# split_ = ' wibu '.join(name)
# print(split_ + '\n')
#
# print(name)
# print(split_.split("Kurniawan"))
# print(split_.split(" wibu "))
# import module
import sys
import time

# mengecek apakah input berupa angka atau tidak
Looping = True
while Looping:
    try:
        userInput = int(input("""
        0. Cara Menggunakan
        1. Penjumlahan
        2. pengurangan
        3. Perkalian
        4. Pembagian
        5. Keluar
        Masukan Input:
        """))
    except:
        print("MOHON MASUKKAN ANGKA!")
        sys.exit(1)

    if userInput > 5:
        print("Maaf angka yang anda masukkan tidak sesuai dengan pilihan")


    # mengecek apakah input berupa angka atau tidak

    def printy(text, delay=0.05):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)
        print()


    if userInput != 0 and userInput != 5:
        try:
            first = int(input("Masukkan angka pertama: "))
            second = int(input("Masukkan angka kedua: "))
            printy("Calculating....")
            time.sleep(1)
        except:
            print("MOHON MASUKKAN ANGKA!")
            sys.exit(1)


    # Fungsi matematika
    def penjumlahan(a, b):
        return a + b


    def pengurangan(a, b):
        return a - b


    def perkalian(a, b):
        return a * b


    def pembagian(a, b):
        return a / b


    # Cara menggunakan
    def penggunaan():
        print("""di kalkulator ini terdapat 4 metode matematika 
        Masukkan angka untuk memilih metode yang ingin digunakan.
        Contoh:
        
        0. Cara Menggunakan
        1. Penjumlahan
        2. pengurangan
        3. Perkalian
        4. Pembagian
        
        Masukan Input: 
        1
        
        Masukkan Angka Pertama: 20
        Masukkan Angka kedua: 20
        """)
        printy("Menghitung...")
        printy("Hasil penjumlahan dari 20 + 20 adalah: 40")
        pass


    # Input memilih metode matematika
    if userInput == 0:
        penggunaan()
    elif userInput == 1:
        penjumlahan = penjumlahan(first, second)
        print(f"Hasil penjumlahan dari {first} + {second} adalah: {penjumlahan:,}")
    elif userInput == 2:
        subtraction = pengurangan(first, second)
        print(f"Hasil pengurangan dari {first} + {second} adalah: {subtraction:,}")
    elif userInput == 3:
        addition = perkalian(first, second)
        print(f"Hasil perkalian dari {first} + {second} adalah: {addition:,}")
    elif userInput == 4:
        divide = pembagian(first, second)
        print(f"Hasil pembagian dari {first} + {second} adalah: {divide:.2f}")
    elif userInput == 5:
        print("Terima Kasih telah menggunakan Program ini")
        break
