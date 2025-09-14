# Rasya Aditya Ramadani (Rasya)
# NIM : 2509116082
# Kelas : Sistem Informasi (C) 
# Sistem Peminjaman & Pengembalian Buku Perpustakaan FKIP Banggeris Universitas Mulawarman

peminjaman_buku = [ ]

print("===== MENU SISTEM PERPUSTAKAAN =====")
print("1. Input Data Peminjaman (CREATE)")
print("2. Pengembalian Buku (READ)")
print("3. Lihat Data Peminjaman (READ)")
print("===================================")

pilihan = input("Pilih menu (1-3): ")

# CREATE
if pilihan == "1":
    Nama = input("Masukkan nama peminjam: ")
    Judul_Buku = input("Masukkan Judul Buku: ")
    Hari_Pinjam = int(input("Masukkan Lama Pinjam Bukunya (hari): "))

    peminjaman_buku.append([Nama, Judul_Buku, Hari_Pinjam])
    print("\nData Peminjaman Berhasil Disimpan")

    # Setelah create, langsung tanya mau apa
    print("\nPilih menu selanjutnya:")
    print("2. Pengembalian Buku")
    print("3. Lihat Data Peminjaman")
    pilihan2 = input("Pilih menu (2/3): ")

    if pilihan2 == "2":
        Nama_Kembali = input("Masukkan nama peminjam: ")
        Judul_Kembali = input("Masukkan judul buku: ")

        if (peminjaman_buku[0][0] == Nama_Kembali) and (peminjaman_buku[0][1] == Judul_Kembali):
            Lama_Pinjam_Asli = peminjaman_buku[0][2]
            Lama_Sebenarnya = int(input("Masukkan lama peminjaman sebenarnya (hari): "))

            if Lama_Sebenarnya == Lama_Pinjam_Asli:
                print("Buku dikembalikan tepat waktu. Tidak ada denda.")
            elif Lama_Sebenarnya == Lama_Pinjam_Asli:
                print("Buku dikembalikan lebih awal. Tidak ada denda.")
            else:
                terlambat = Lama_Sebenarnya - Lama_Pinjam_Asli
                denda = 2500 * terlambat
                print("Buku terlambat dikembalikan selama", terlambat, "hari.")
                print("Denda yang harus dibayar: Rp", denda)
        else:
            print("Data tidak ditemukan.")

    elif pilihan2 == "3":
        print("\n=== DAFTAR DATA PEMINJAMAN ===")
        print("1.", peminjaman_buku[0])
    else:
        print("Pilihan tidak valid.")

# READ (langsung pilih menu 2)
elif pilihan == "2":
    print("Belum ada data, silakan input dulu di menu 1.")

# READ (langsung pilih menu 3)
elif pilihan == "3":
    print("Belum ada data, silakan input dulu di menu 1.")

else:
    print("Pilihan tidak valid.")

print("n\Terima kasih telah menggunakan Sistem Perpustakaan FKIP Banggeris Universitas Mulawarman")