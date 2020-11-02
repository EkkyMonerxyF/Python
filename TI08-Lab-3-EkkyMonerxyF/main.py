# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
py1 = input('Masukkan player1 : ')
py2 = input('Masukkan player2 : ')

if py1 == 'gunting' and py2 == 'batu':
            print('player2 menang')
elif py1 == 'batu' and py2 == 'gunting':
            print('player1 menang')
elif py1 == 'gunting' and  py2 == 'gunting':
            print('seri')
elif py1 == 'gunting' and py2 == 'kertas':
            print('player1 menang')
elif py1 == 'kertas' and py2 == 'gunting':
            print('player2 menang')
elif py1 == 'kertas' and py2 == 'kertas':
            print('seri')
elif py1 == 'batu' and 'kertas':
            print('player1 menang')
elif py1 == 'kertas' and py2 == 'batu':
            print('player2 menang')
elif py 1 == 'batu' and py2 == 'batu':
            print('seri')


# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini
jumlah = eval(input('Masukkan banyak buku yang akan dibeli : '))
if jumlah > 50:
    print(jumlah * 10000, 'rupiah')
elif jumlah > 25:
    print(jumlah * 15000, 'rupiah')
elif jumlah > 11:
    print(jumlah * 18000, 'rupiah')
elif jumlah <= 10:
    print(jumlah * 20000, 'rupiah')




# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini
A = int(input('Masukkan Bilangan Bulat : '))

for i in range(A):
    for j in range(A):
        if (i % 2 == 0):
            print('#', end=' ')
        else:
            print('$', end=' ')
    print()

