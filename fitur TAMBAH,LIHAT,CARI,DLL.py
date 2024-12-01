data_mahasiswa = {}

def tambah(nama, nilai):
    if nama in data_mahasiswa:
        print(f"Data dengan nama {nama} sudah ada.")
    else:
        data_mahasiswa[nama] = nilai
        print(f"Data {nama} berhasil ditambahkan.")

def tampilkan():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("\nDaftar Nilai Mahasiswa:")
        print(f"{'Nama':<20} {'Nilai':<10}")
        print("-" * 30)
        for nama, nilai in data_mahasiswa.items():
            print(f"{nama:<20} {nilai:<10}")

def hapus(nama):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data {nama} berhasil dihapus.")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")

def ubah(nama, nilai_baru):
    if nama in data_mahasiswa:
        data_mahasiswa[nama] = nilai_baru
        print(f"Data {nama} berhasil diubah.")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")

while True:
    print("\nMenu: [1] Tambah  [2] Tampilkan  [3] Hapus  [4] Ubah  [5] Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        nilai = input("Masukkan nilai mahasiswa: ")
        tambah(nama, nilai)
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        nilai_baru = input("Masukkan nilai baru: ")
        ubah(nama, nilai_baru)
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
