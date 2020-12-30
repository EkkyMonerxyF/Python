print("PROGRAM MENGHITUNG X^y")
print("=======================")

a = 0

while a == 0:
    a = float(input("Masukkan Bilangan Real (X) : "))
    if a == 0:
        print("Ini Bukan Bilangan Real")
    elif a > 0 and a < 0:
        break

    b = int(input("Masukkan Bilangan Bulat Positif : "))
    c = a**b
    print("X pangkat Y adalah = ", c)
