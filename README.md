# pratikum-6

# Program Daftar Nilai Mahasiswa

Program ini adalah aplikasi sederhana berbasis terminal untuk mengelola daftar nilai mahasiswa.
Program ini memiliki fitur untuk menambah, menampilkan, menghapus, dan mengubah data mahasiswa.


# Program Daftar Nilai Mahasiswa

Program ini adalah aplikasi sederhana berbasis terminal untuk mengelola daftar nilai mahasiswa.
Berikut adalah penjelasan fungsi-fungsi yang terdapat dalam kode program.
## Screenshout vsc

![fitur tambah,cari,lihat,dll](https://github.com/user-attachments/assets/10ef2acb-8396-41d0-9053-ad0e0bf0f196)

## Penjelasan Kode

### 1. Variabel `data_mahasiswa`
```python
data_mahasiswa = {}
```
Variabel ini adalah sebuah dictionary kosong yang digunakan untuk menyimpan data mahasiswa. 
Key adalah nama mahasiswa, dan value adalah nilai mereka.

### 2. Fungsi `tambah(nama, nilai)`
```python
def tambah(nama, nilai):
    if nama in data_mahasiswa:
        print(f"Data dengan nama {nama} sudah ada.")
    else:
        data_mahasiswa[nama] = nilai
        print(f"Data {nama} berhasil ditambahkan.")
```
Fungsi ini digunakan untuk menambahkan data mahasiswa. Jika nama mahasiswa sudah ada, program akan memberi tahu pengguna bahwa data tersebut sudah ada. Jika belum, data baru ditambahkan ke `data_mahasiswa`.

### 3. Fungsi `tampilkan()`
```python
def tampilkan():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("\nDaftar Nilai Mahasiswa:")
        print(f"{'Nama':<20} {'Nilai':<10}")
        print("-" * 30)
        for nama, nilai in data_mahasiswa.items():
            print(f"{nama:<20} {nilai:<10}")
```
Fungsi ini digunakan untuk menampilkan semua data mahasiswa dalam bentuk tabel. 
Jika data kosong, program akan memberi tahu bahwa belum ada data.

### 4. Fungsi `hapus(nama)`
```python
def hapus(nama):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data {nama} berhasil dihapus.")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")
```
Fungsi ini digunakan untuk menghapus data mahasiswa berdasarkan nama. 
Jika nama tidak ditemukan, program akan memberi tahu pengguna.

### 5. Fungsi `ubah(nama, nilai_baru)`
```python
def ubah(nama, nilai_baru):
    if nama in data_mahasiswa:
        data_mahasiswa[nama] = nilai_baru
        print(f"Data {nama} berhasil diubah.")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")
```
Fungsi ini digunakan untuk mengubah nilai mahasiswa berdasarkan nama. 
Jika nama tidak ditemukan, program akan memberi tahu pengguna.

### 6. Menu Interaktif
```python
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
```
Bagian ini adalah loop utama program yang menyediakan menu interaktif untuk pengguna.
- **Pilihan Menu**:
  - `1`: Tambah data mahasiswa.
  - `2`: Tampilkan data mahasiswa.
  - `3`: Hapus data mahasiswa berdasarkan nama.
  - `4`: Ubah nilai mahasiswa berdasarkan nama.
  - `5`: Keluar dari program.


**Menambah Data:**
```
Menu: [1] Tambah  [2] Tampilkan  [3] Hapus  [4] Ubah  [5] Keluar
Pilih menu (1-5): 1
Masukkan nama mahasiswa: John
Masukkan nilai mahasiswa: 90
Data Dzaki berhasil ditambahkan.
```

**Menampilkan Data:**
```
Menu: [1] Tambah  [2] Tampilkan  [3] Hapus  [4] Ubah  [5] Keluar
Pilih menu (1-5): 2

Daftar Nilai Mahasiswa:
Nama                 Nilai     
------------------------------
Dzaki                90        
```

**Menghapus Data:**
```
Menu: [1] Tambah  [2] Tampilkan  [3] Hapus  [4] Ubah  [5] Keluar
Pilih menu (1-5): 3
Masukkan nama mahasiswa yang akan dihapus: John
Data Dzaki berhasil dihapus.
```

**Mengubah Data:**
```
Menu: [1] Tambah  [2] Tampilkan  [3] Hapus  [4] Ubah  [5] Keluar
Pilih menu (1-5): 4
Masukkan nama mahasiswa yang akan diubah: John
Masukkan nilai baru: 95
Data Dzaki berhasil diubah.
```


### Menu Utama
```
Menu: [1] Tambah  [2] Tampilkan  [3] Hapus  [4] Ubah  [5] Keluar
Pilih menu (1-5): 
```

### Contoh screenshout Output dari vsc

![Screenshot 2024-12-01 194410](https://github.com/user-attachments/assets/275e98f8-2ed0-4864-bbbf-bc13fc7ff517)

## berikut adalah screenshout flowchart nya


