def main():

    print("DATA PEGAWAI")
    print("-"*22, "\n")

    nama = input("Nama : ")
    golongan = input("Golongan : ")
    ttj = int(input("Total Jam Kerja : "))
    print("\n")
    print("PERHITUNGAN GAJI")
    print("-"*22, "\n")

    gapok = int(input("Gaji Pokok : "))

    if gapok == 500000:
        tj = int(0.10*gapok)
        print("Tunjangan : ", tj)
        lbr = (ttj - 200) * 5000
        print("Lembur : ", lbr)
        print("-"*22, "\n")
        print("Total : ", gapok+tj+lbr)

    if gapok == 700000:
        tj = int(0.15*gapok)
        print("Tunjangan : ", tj)
        lbr = (ttj - 200) * 7500
        print("Lembur : ", lbr)
        print("-"*22, "\n")
        print("Total : ", gapok+tj+lbr)

    if gapok == 900000:
        tj = int(0.20*gapok)
        print("Tunjangan : ", tj)
        lbr = (ttj - 200) * 10000
        print("Lembur : ", lbr)
        print("-"*22, "\n")
        print("Total : ", gapok+tj+lbr)


if __name__ == "__main__":
    main()
