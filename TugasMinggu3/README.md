# Praktikum Kecerdasan Buatan - Pertemuan 3
**Topik:** Logika Fuzzy 2 (Metode Mamdani)

Repository ini berisi source code penyelesaian Studi Kasus Praktikum Kecerdasan Buatan Pertemuan 3 menggunakan library `scikit-fuzzy` pada bahasa pemrograman Python.

## Penjelasan File

### 1. `hewan.py` (Studi Kasus 1: Toko Hewan)
Script ini menyelesaikan studi kasus penentuan stok makanan di "Udin Pet Shop" menggunakan metode Fuzzy Mamdani.
- **Variabel Input:** Barang Terjual (80), Permintaan (255), Harga per Item (25.000), Profit (3.500.000).
- **Aturan (Rule Base):** Terdapat 6 aturan sesuai dengan dokumen modul praktikum.
- **Output:** Menghasilkan nilai crisp untuk persediaan Stok Makanan yang optimal beserta grafik area fuzzifikasinya.

### 2. `pelayanan.py` (Studi Kasus 2: Pelayanan Masyarakat)
Script ini menyelesaikan studi kasus penentuan tingkat kepuasan di Kantor Pelayanan Masyarakat Kota Sejahtera menggunakan metode Fuzzy Mamdani.
- **Variabel Input:** Kejelasan Informasi (80), Kejelasan Persyaratan (60), Kemampuan Petugas (50), Ketersediaan Sarpras (90).
- **Catatan Fiksasi Logika (PENTING):** Pada dokumen modul praktikum, hanya terdapat 13 aturan (Rule Base). Namun, kombinasi input pada studi kasus ini (terutama Kemampuan Petugas = 50 yang bernilai 'Tidak Memuaskan' dan Informasi = 80 yang bernilai 'Cukup/Memuaskan') **tidak tercakup** dalam 13 aturan tersebut, sehingga sistem tidak dapat menghasilkan output (menghasilkan *blank spot*).
- **Solusi:** Pada script `pelayanan.py` ini, telah dilakukan fiksasi dengan menjabarkan ke-81 kemungkinan kombinasi aturan ($3^4 = 81$ *Rules*) secara manual dan komprehensif. Hal ini memastikan sistem Fuzzy dapat melakukan defuzzifikasi dengan sempurna pada nilai input berapapun tanpa terjadi *error*.

## Requirements & Instalasi

Pastikan Anda sudah menginstal library Python berikut sebelum menjalankan program. Buka terminal dan jalankan perintah:

```bash
pip install numpy
pip install scikit-fuzzy
pip install matplotlib