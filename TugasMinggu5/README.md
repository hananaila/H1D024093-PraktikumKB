# Praktikum Kecerdasan Buatan — Pertemuan 5

**Topik:** Sistem Pakar 2

Repository ini berisi source code penyelesaian Studi Kasus Praktikum Kecerdasan Buatan Pertemuan 5 menggunakan library `tkinter` pada bahasa pemrograman Python.

---

## Struktur Folder

```text
TugasMinggu5/
├── PakarTHT.py
└── README.md
```

---

## Penjelasan File

### `PakarTHT.py` — Sistem Pakar Diagnosa Penyakit THT

Program ini mendiagnosa penyakit **Telinga, Hidung, dan Tenggorokan (THT)** berdasarkan gejala-gejala yang dialami pengguna menggunakan pendekatan **Forward Chaining**.

| Komponen | Detail |
|---|---|
| Jumlah Penyakit | 23 jenis penyakit THT |
| Jumlah Gejala | 37 pertanyaan gejala (G1–G37) |
| Metode Inferensi | Forward Chaining (`all()`) |
| Antarmuka | GUI berbasis `tkinter` |

- **Knowledge Base:** Terdapat 23 aturan penyakit THT — Tonsilitis, Sinusitis (4 jenis), Faringitis, Laringitis, Kanker Laring, Otitis Media Akut, Meniere, Vertigo, dan lainnya.
- **Output:** Nama penyakit yang terdeteksi muncul dalam dialog pop-up beserta peringatan untuk segera berkonsultasi ke dokter THT.

---

## Daftar Gejala

| Kode | Gejala | Kode | Gejala |
|------|--------|------|--------|
| G1 | Nafas abnormal | G20 | Nyeri telinga |
| G2 | Suara serak | G21 | Selaput lendir merah |
| G3 | Perubahan kulit | G22 | Benjolan leher |
| G4 | Telinga penuh | G23 | Tubuh tak seimbang |
| G5 | Nyeri bicara/menelan | G24 | Bola mata bergerak |
| G6 | Nyeri tenggorokan | G25 | Nyeri wajah |
| G7 | Nyeri leher | G26 | Dahi sakit |
| G8 | Pendarahan hidung | G27 | Batuk |
| G9 | Telinga berdenging | G28 | Tumbuh di mulut |
| G10 | Air liur menetes | G29 | Benjolan di leher |
| G11 | Perubahan suara | G30 | Nyeri antara mata |
| G12 | Sakit kepala | G31 | Radang gendang telinga |
| G13 | Nyeri pinggir hidung | G32 | Tenggorokan gatal |
| G14 | Serangan vertigo | G33 | Hidung meler |
| G15 | Getah bening | G34 | Tuli |
| G16 | Leher bengkak | G35 | Mual muntah |
| G17 | Hidung tersumbat | G36 | Lesu/lemas |
| G18 | Infeksi sinus | G37 | Demam |
| G19 | Berat badan turun | | |

---

## Daftar Penyakit yang Dapat Dideteksi

| No | Penyakit | Gejala yang Digunakan |
|---|---|---|
| 1 | **Tonsilitis** | G37, G12, G5, G27, G6, G21 |
| 2 | **Sinusitis Maksilaris** | G37, G12, G27, G17, G33, G36, G29 |
| 3 | **Sinusitis Frontalis** | G37, G12, G27, G17, G33, G36, G21, G26 |
| 4 | **Sinusitis Ethmoidalis** | G37, G12, G27, G17, G33, G36, G21, G30, G13, G26 |
| 5 | **Sinusitis Sfenoidalis** | G37, G12, G27, G17, G33, G36, G29, G7 |
| 6 | **Abses Peritonsiler** | G37, G12, G6, G15, G2, G29, G10 |
| 7 | **Faringitis** | G37, G5, G6, G7, G15 |
| 8 | **Kanker Laring** | G5, G27, G6, G15, G2, G19, G1 |
| 9 | **Deviasi Septum** | G37, G17, G20, G8, G18, G25 |
| 10 | **Laringitis** | G37, G5, G15, G16, G32 |
| 11 | **Kanker Leher & Kepala** | G5, G22, G8, G28, G3, G11 |
| 12 | **Otitis Media Akut** | G37, G20, G35, G31 |
| 13 | **Contact Ulcers** | G5, G2 |
| 14 | **Abses Parafaringeal** | G5, G16 |
| 15 | **Barotitis Media** | G12, G20 |
| 16 | **Kanker Nasofaring** | G17, G8 |
| 17 | **Kanker Tonsil** | G6, G29 |
| 18 | **Neuronitis Vestibularis** | G35, G24 |
| 19 | **Meniere** | G20, G35, G14, G4 |
| 20 | **Tumor Syaraf Pendengaran** | G12, G34, G23 |
| 21 | **Kanker Leher Metastatik** | G29 |
| 22 | **Osteosklerosis** | G34, G9 |
| 23 | **Vertigo Postular** | G24 |

---

## Cara Menjalankan Program

### 1. Persiapan Lingkungan

Pastikan Python sudah terinstal di sistem Anda. Library `tkinter` sudah tersedia secara bawaan, sehingga **tidak perlu instalasi tambahan**.

### 2. Eksekusi Program

Arahkan terminal ke dalam folder repository, kemudian jalankan perintah berikut:

```bash
python PakarTHT.py
```

### 3. Melihat Hasil

Program akan membuka jendela aplikasi GUI. Klik tombol **"Mulai Diagnosa"**, lalu jawab setiap pertanyaan gejala dengan menekan tombol **YA** atau **TIDAK**. Setelah semua 37 pertanyaan selesai dijawab, hasil diagnosa akan otomatis muncul dalam jendela pop-up.