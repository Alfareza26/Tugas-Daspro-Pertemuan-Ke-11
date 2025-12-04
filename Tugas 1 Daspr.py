def harga_tiket(pilihan):
    if pilihan == 1:
        kategori = "Balita"
        harga = 1500
    elif pilihan == 2:
        kategori = "Pelajar"
        harga = 3000
    elif pilihan == 3:
        kategori = "Lansia"
        harga = 2500
    elif pilihan == 4:
        kategori = "Umum"
        harga = 5000
    else:
        kategori = "Tidak valid"
        harga = 0 or "Error"
    return kategori, harga
print("=== PILIHAN TIKET BUS ===")
print("1. Balita               → Rp1.500")
print("2. Pelajar/Mahasiswa    → Rp3.000")
print("3. Lansia               → Rp2.500")
print("4. Umum                 → Rp5.000")
pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
kategori, harga = harga_tiket(pilihan)
print("\nKategori:", kategori)
if kategori == "Tidak valid":
    print("Not Found")
else:
    print("Harga tiket: Rp ", harga)