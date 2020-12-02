

def main():
    print("PROGRAM MENGHITUNG PEMBELIAN")
    print("----------------------------")

    hsatuan = int(input("Harga Satuan : "))
    jml = int(input("Jumlah Pembelian : "))
    diskon = 10 / 100 * hsatuan*jml
    print("Diskon 10% : ", int(diskon))
    print("-"*28)
    print("Harga Total : Rp", int(hsatuan*jml - diskon))


if __name__ == "__main__":
    main()
