# Praktikum Kecerdasan Buatan — Pertemuan 4

**Topik:** Sistem Pakar 

Repository ini berisi source code penyelesaian Studi Kasus Praktikum Kecerdasan Buatan Pertemuan 4 menggunakan library `tkinter` pada bahasa pemrograman Python.

---

## Struktur Folder
```text
TugasMinggu4/
├── coba1.py
├── coba2.py
├── coba3.py
├── coba4.py
├── README.md
└── komputer.py    # Source code Tugas Pertemuan 4
```

---

## Penjelasan File

### `komputer.py` — Sistem Pakar Diagnosa Kerusakan Komputer

Program ini mendiagnosa kerusakan perangkat keras (hardware) komputer atau laptop berdasarkan gejala-gejala yang dialami pengguna menggunakan pendekatan **Forward Chaining**.

| Komponen | Detail |
|---|---|
| Jumlah Kerusakan | 6 jenis kerusakan hardware |
| Jumlah Gejala | 18 pertanyaan gejala |
| Metode Inferensi | Forward Chaining (`all()`) |
| Antarmuka | GUI berbasis `tkinter` |

- **Knowledge Base:** Terdapat 6 aturan kerusakan — RAM Rusak, PSU Lemah, Overheat, VGA Bermasalah, Hardisk Corrupt, dan Baterai CMOS Habis.
- **Output:** Nama kerusakan yang terdeteksi beserta solusi perbaikan yang muncul dalam dialog pop-up.

---

## Daftar Kerusakan yang Dapat Dideteksi

| No | Kerusakan | Gejala | Solusi Singkat |
|---|---|---|---|
| 1 | **RAM Rusak** | Bunyi beep, layar blank, BSOD | Bersihkan pin kuningan RAM dengan penghapus |
| 2 | **Power Supply (PSU) Lemah** | Mati mendadak, kipas sebentar, bau hangus | Periksa kabel power atau ganti PSU |
| 3 | **Overheat (Prosesor)** | Kipas bising, mati saat panas, kinerja lambat | Bersihkan debu & ganti thermal paste |
| 4 | **VGA Bermasalah** | Garis aneh di layar, warna pudar, freeze | Update driver atau bersihkan konektor VGA |
| 5 | **Hardisk/SSD Corrupt** | Booting lama, bunyi klik, gagal baca file | Backup data & scan bad sector |
| 6 | **Baterai CMOS Habis** | Jam reset, pesan CMOS Error, BIOS default | Ganti baterai CR2032 di motherboard |

---

## Cara Menjalankan Program

### 1. Persiapan Lingkungan

Pastikan Python sudah terinstal di sistem Anda. Library `tkinter` sudah tersedia secara bawaan, sehingga **tidak perlu instalasi tambahan**.

### 2. Eksekusi Program

Arahkan terminal ke dalam folder `TugasMinggu4`, kemudian jalankan perintah berikut:
```bash
python komputer.py
```

### 3. Melihat Hasil

Program akan membuka jendela aplikasi GUI. Klik tombol **"Mulai Diagnosa"**, lalu jawab setiap pertanyaan gejala dengan menekan tombol **YA** atau **TIDAK**. Setelah semua pertanyaan selesai dijawab, hasil diagnosa beserta solusi perbaikan akan otomatis muncul dalam jendela pop-up.