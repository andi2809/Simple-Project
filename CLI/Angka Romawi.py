def calculate_roman(angka):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    for num in range(len(angka)):
        if num < len(angka) - 1 and roman[angka[num]] < roman[angka[num + 1]]:
            total -= roman[angka[num]]
        else:
            total += roman[angka[num]]
    return total


# Jadi ketika sudah sampai di len akhir, kondisi bernilai false lalu ditambah

print("Hasil dari MMXXII adalah: ", calculate_roman("MMXXII"))
