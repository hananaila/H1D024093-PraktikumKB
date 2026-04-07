# Praktikum Kecerdasan Buatan - Pertemuan 3
**Topik:** Logika Fuzzy 2 (Metode Mamdani)

Repository ini berisi source code penyelesaian Studi Kasus Praktikum Kecerdasan Buatan Pertemuan 3 menggunakan library `scikit-fuzzy` pada bahasa pemrograman Python.

## Struktur Folder

```text
TugasMinggu3/
├── README.md
├── hewan.py       # Source code Studi Kasus 1 (Toko Hewan)
└── pelayanan.py   # Source code Studi Kasus 2 (Pelayanan Masyarakat)

## Penjelasan File

### 1. `hewan.py` (Studi Kasus 1: Toko Hewan)
Program ini menentukan jumlah persediaan stok makanan hewan yang optimal di "Udin Pet Shop" agar dapat memenuhi permintaan tanpa mengalami overstock atau kekurangan persediaan.
- **Variabel & Himpunan Fuzzy:** Barang Terjual (80), Permintaan (255), Harga per Item (25.000), dan Profit (3.500.000).
- **Aturan (Rule Base):** Terdapat 6 aturan sesuai dengan dokumen modul praktikum.
- **Output:** Menghasilkan nilai *crisp* untuk persediaan Stok Makanan yang optimal beserta grafik area fuzzifikasinya.

### 2. `pelayanan.py` (Studi Kasus 2: Pelayanan Masyarakat)
Script ini menyelesaikan studi kasus penentuan tingkat kepuasan di Kantor Pelayanan Masyarakat Kota Sejahtera menggunakan metode Fuzzy Mamdani.
- **Variabel Input:** Kejelasan Informasi (80)Kejelasan Persyaratan (60), Kemampuan Petugas (50), dan Ketersediaan Sarpras (90).
- **Aturan (Rule Base):** Mengimplementasikan ke-81 kemungkinan kombinasi aturan ($3^4 = 81$ *rules*) secara komprehensif sesuai instruksi tambahan dari Mas Aska melalui Discord.
- **Output:** Menghasilkan nilai *crisp* untuk persentase Kepuasan Pelayanan yang objektif beserta grafik area fuzzifikasinya.

## Cara Menjalankan Program

**1. Persiapan Lingkungan (Install Dependencies)** Pastikan Python sudah terinstal di sistem Anda. Buka terminal atau *command prompt*, lalu instal pustaka pendukung berikut:
```bash
pip install numpy scikit-fuzzy matplotlib

**2. Eksekusi Program**
Arahkan direktori terminal ke dalam folder TugasMinggu3, kemudian jalankan salah satu perintah berikut untuk mengeksekusi file:
```bash
python hewan.py
atau 
```bash
python pelayanan.py

**3. Melihat Hasil**
Program akan langsung melakukan kalkulasi dan mencetak hasil output di terminal. Bersamaan dengan itu, jendela figure dari matplotlib akan otomatis terbuka untuk menampilkan visualisasi grafik himpunan dan area hasil.
