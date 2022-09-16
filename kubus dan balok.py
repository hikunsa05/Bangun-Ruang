print("Menghitung Bangun Ruang Kubus Dan Balok")
print("---------------------------------------")
print("[1] Keliling, Luas, Dan Volume Kubus")
print("[2] Keliling, Luas, Dan Volume Balok")
print("---------------------------------------")
pilihan = int(input("pilih salah satu program (1-2): "))

if pilihan == 1:
    print("Menghitung Bangun Ruang Kubus")
    print("-----------------------------")

    s = int(input("Masukkan nilai Sisi = "))

    keliling = 12 * s 
    luas     = 6 * s * s
    volume   = s * s * s
    print("-----------------------------")
    print("keliling kubus adalah   = ", keliling)
    print("luas kubus adalah       = ", luas)
    print("volume kubus adalah     = ", volume)

elif pilihan == 2:
    print("Menghitung Bangun Ruang Balok")
    print("-----------------------------")

    p = int(input("Masukkan nilai Panjang = "))
    l = int(input("Masukkan nilai Lebar   = "))
    t = int(input("Masukkan nilai Tinggi  = "))

    keliling = 4 * (p + l + t) 
    luas     = 2 * (p*l + p*t + l*t)
    volume   = p * l * t
    print("-------------------------------")
    print("keliling balok adalah   = ", keliling)
    print("luas balok adalah       = ", luas)
    print("volume balok adalah     = ", volume)

else:
    print("Error: Inputkan angka yang benar..")