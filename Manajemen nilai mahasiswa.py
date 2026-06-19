# Penyimpanan data menggunakan List
data_mahasiswa = [
    ["Ahmad", 85],
    ["Budi", 78],
    ["Citra", 90]
]

# Fungsi tampilkan data
def tampilkan():
    if len(data_mahasiswa) == 0:
        print("\nData kosong!")
        return
    print("\nDaftar Nilai Mahasiswa:")
    print("-------------------------")
    for i in range(len(data_mahasiswa)):
        nama = data_mahasiswa[i][0]
        nilai = data_mahasiswa[i][1]
        print(f"{i+1}. Nama: {nama}, Nilai: {nilai}")

# Fungsi tambah data
def tambah():
    nama = input("\nMasukkan nama: ")
    nilai = int(input("Masukkan nilai: "))
    if 0 <= nilai <= 100:
        data_mahasiswa.append([nama, nilai])
        print("Data berhasil ditambahkan!")
    else:
        print("Nilai harus antara 0 - 100!")

# Fungsi ubah data
def ubah():
    nama_cari = input("\nMasukkan nama yang ingin diubah: ")
    for i in range(len(data_mahasiswa)):
        if data_mahasiswa[i][0] == nama_cari:
            nilai_baru = int(input("Masukkan nilai baru: "))
            if 0 <= nilai_baru <= 100:
                data_mahasiswa[i][1] = nilai_baru
                print("Data berhasil diubah!")
                return
            else:
                print("Nilai tidak valid!")
                return
    print("Nama tidak ditemukan!")

# Fungsi hapus data
def hapus():
    nama_cari = input("\nMasukkan nama yang ingin dihapus: ")
    for i in range(len(data_mahasiswa)):
        if data_mahasiswa[i][0] == nama_cari:
            del data_mahasiswa[i]
            print("Data berhasil dihapus!")
            return
    print("Nama tidak ditemukan!")

# Fungsi cari data
def cari():
    nama_cari = input("\nMasukkan nama yang dicari: ")
    for data in data_mahasiswa:
        if data[0] == nama_cari:
            print(f"Ditemukan! Nama: {data[0]}, Nilai: {data[1]}")
            return
    print("Nama tidak ditemukan!")

# Fungsi urutkan nilai dari tertinggi
def urutkan():
    data_mahasiswa.sort(key=lambda x: x[1], reverse=True)
    print("\nData diurutkan dari nilai tertinggi:")
    tampilkan()

# Fungsi hitung rata-rata
def rata_rata():
    if len(data_mahasiswa) == 0:
        print("\nData kosong!")
        return
    total = 0
    for data in data_mahasiswa:
        total = total + data[1]
    hasil = total / len(data_mahasiswa)
    print(f"\nRata-rata nilai: {hasil:.2f}")

# Menu Utama
while True:
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Berdasarkan Nilai")
    print("7. Hitung Rata-rata")
    print("8. Keluar")
    print("====================================")

    try:
        pilihan = int(input("Pilih menu 1-8: "))

        if pilihan == 1:
            tampilkan()
        elif pilihan == 2:
            tambah()
        elif pilihan == 3:
            ubah()
        elif pilihan == 4:
            hapus()
        elif pilihan == 5:
            cari()
        elif pilihan == 6:
            urutkan()
        elif pilihan == 7:
            rata_rata()
        elif pilihan == 8:
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak ada! Masukkan angka 1 sampai 8.")

    except:
        print("Masukkan angka yang benar!")
