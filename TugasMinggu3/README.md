# Praktikum Kecerdasan Buatan - Pertemuan 3
**Topik:** Logika Fuzzy 2 (Metode Mamdani)

Repository ini berisi source code penyelesaian Studi Kasus Praktikum Kecerdasan Buatan Pertemuan 3 menggunakan library `scikit-fuzzy` pada bahasa pemrograman Python.

## Penjelasan File

### 1. `hewan.py` (Studi Kasus 1: Toko Hewan)
Script ini menyelesaikan studi kasus penentuan stok makanan di "Udin Pet Shop" menggunakan metode Fuzzy Mamdani.
- **Variabel Input:** Barang Terjual (80), Permintaan (255), Harga per Item (25.000), dan Profit (3.500.000).
- **Aturan (Rule Base):** Terdapat 6 aturan sesuai dengan dokumen modul praktikum.
- **Output:** Menghasilkan nilai *crisp* untuk persediaan Stok Makanan yang optimal beserta grafik area fuzzifikasinya.

### 2. `pelayanan.py` (Studi Kasus 2: Pelayanan Masyarakat)
Script ini menyelesaikan studi kasus penentuan tingkat kepuasan di Kantor Pelayanan Masyarakat Kota Sejahtera menggunakan metode Fuzzy Mamdani.
- **Variabel Input:** Kejelasan Informasi (80)Kejelasan Persyaratan (60), Kemampuan Petugas (50), dan Ketersediaan Sarpras (90).
- **Aturan (Rule Base):** Mengimplementasikan ke-81 kemungkinan kombinasi aturan ($3^4 = 81$ *rules*) secara komprehensif sesuai instruksi tambahan dari Mas Aska melalui Discord.
- **Output:** Menghasilkan nilai *crisp* untuk persentase Kepuasan Pelayanan yang objektif beserta grafik area fuzzifikasinya.