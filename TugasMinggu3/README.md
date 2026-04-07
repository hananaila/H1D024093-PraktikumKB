# Praktikum Kecerdasan Buatan — Pertemuan 3

**Topik:** Logika Fuzzy 2 (Metode Mamdani)

Repository ini berisi source code penyelesaian Studi Kasus Praktikum Kecerdasan Buatan Pertemuan 3 menggunakan library `scikit-fuzzy` pada bahasa pemrograman Python.

---

## Struktur Folder
```text
TugasMinggu3/
├── README.md
├── hewan.py       # Source code Studi Kasus 1 (Toko Hewan)
└── pelayanan.py   # Source code Studi Kasus 2 (Pelayanan Masyarakat)
```

---

## Penjelasan File

### 1. `hewan.py` — Studi Kasus 1: Toko Hewan

Program ini menentukan jumlah persediaan stok makanan hewan yang optimal di **Udin Pet Shop** agar dapat memenuhi permintaan tanpa mengalami *overstock* atau kekurangan persediaan.

| Variabel | Nilai |
|---|---|
| Barang Terjual | 80 |
| Permintaan | 255 |
| Harga per Item | Rp 25.000 |
| Profit | Rp 3.500.000 |

- **Rule Base:** Terdapat 6 aturan sesuai dokumen modul praktikum.
- **Output:** Nilai *crisp* untuk persediaan stok makanan optimal beserta grafik area fuzzifikasi.

---

### 2. `pelayanan.py` — Studi Kasus 2: Pelayanan Masyarakat

Script ini menyelesaikan studi kasus penentuan tingkat kepuasan di **Kantor Pelayanan Masyarakat Kota Sejahtera** menggunakan metode Fuzzy Mamdani.

| Variabel Input | Nilai |
|---|---|
| Kejelasan Informasi | 80 |
| Kejelasan Persyaratan | 60 |
| Kemampuan Petugas | 50 |
| Ketersediaan Sarpras | 90 |

- **Rule Base:** Mengimplementasikan 81 kemungkinan kombinasi aturan secara komprehensif sesuai instruksi tambahan dari Mas Azka melalui Discord.
- **Output:** Nilai *crisp* untuk persentase kepuasan pelayanan beserta grafik area fuzzifikasi.

---

## Cara Menjalankan Program

### 1. Persiapan Lingkungan

Pastikan Python sudah terinstal di sistem Anda, lalu install seluruh dependensi yang dibutuhkan:
```bash
pip install numpy scikit-fuzzy matplotlib
```

### 2. Eksekusi Program

Arahkan terminal ke dalam folder `TugasMinggu3`, kemudian jalankan salah satu perintah berikut:
```bash
# Studi Kasus 1 - Toko Hewan
python hewan.py
```
```bash
# Studi Kasus 2 - Pelayanan Masyarakat
python pelayanan.py
```

### 3. Melihat Hasil

Program akan melakukan kalkulasi dan mencetak hasil output di terminal. Bersamaan dengan itu, jendela figure dari `matplotlib` akan otomatis terbuka untuk menampilkan visualisasi grafik himpunan dan area hasil defuzzifikasi.