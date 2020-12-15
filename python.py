def main():

    print("Perbandingan Bilangan")
    print("-"*25)

    a = int(input("Masukkan Bilangan : "))
    b = int(input("Masukkan Bilangan : "))
    c = int(input("Masukkan Bilangan : "))

    if a == b:
        if a == b and a < c:
            print("Bilangan", a, "dan", b, "Lebih Kecil dari", c)
        elif a == b and a > c:
            print("Bilangan", a, "dan", b, "Lebih Besar dari", c)

    elif a == c:
        if a == c and a < b:
            print("Bilangan", a, "dan", c, "Lebih Kecil dari", b)
        elif a == c and a > b:
            print("Bilangan", a, "dan", c, "Lebih Besar dari", b)

    elif b == c:
        if b == c and b < a:
            print("Bilangan", b, "dan", c, "Lebih Kecil dari", a)
        elif b == c and b > a:
            print("Bilangan", b, "dan", c, "Lebih Besar dari", a)

    elif a > b and a > c:
        print("Bilangan Terbesar", a)

    elif b > a and b > c:
        print("Bilangan Terbesar", b)

    else:
        print("Bilangan Terbesar", c)


if __name__ == "__main__":
    main()
