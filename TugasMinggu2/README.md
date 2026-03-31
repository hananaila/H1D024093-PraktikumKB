# Sistem Kontrol Kecepatan Kipas Berbasis Logika Fuzzy

Proyek ini adalah implementasi sistem kontrol logika fuzzy (Fuzzy Logic Control System) menggunakan bahasa pemrograman Python dan pustaka `scikit-fuzzy`. Program ini bertujuan untuk menentukan **kecepatan kipas angin** secara otomatis berdasarkan dua input lingkungan: **Suhu** dan **Kelembapan**.

## Fitur Utama
* **Definisi Himpunan Fuzzy:** Membagi variabel input dan output ke dalam himpunan fuzzy (membership function) dengan bentuk segitiga (`trimf`).
* **Sistem Inferensi:** Menggunakan aturan fuzzy (fuzzy rules) untuk menentukan logika operasional kipas.
* **Defuzzifikasi:** Menghitung nilai *crisp* (angka pasti) untuk kecepatan kipas berdasarkan input kondisi yang diberikan.
* **Visualisasi Grafik:** Menampilkan grafik fungsi keanggotaan (membership function) untuk suhu, kelembapan, dan kecepatan kipas menggunakan `matplotlib`.

## Variabel dan Himpunan Fuzzy

Sistem ini menggunakan parameter berikut:

**1. Input: Suhu (°C)**
* Rentang: 0 - 40 °C
* Himpunan: `dingin`, `normal`, `panas`

**2. Input: Kelembapan (%)**
* Rentang: 0 - 100 %
* Himpunan: `kering`, `ideal`, `basah`

**3. Output: Kecepatan Kipas**
* Rentang: 0 - 100 (Skala kecepatan)
* Himpunan: `lambat`, `sedang`, `cepat`

## Aturan Fuzzy (Fuzzy Rules)
Sistem ini beroperasi berdasarkan 3 aturan dasar:
1. **JIKA** Suhu `dingin` **DAN** Kelembapan `basah`, **MAKA** Kipas `lambat`.
2. **JIKA** Suhu `normal` **DAN** Kelembapan `ideal`, **MAKA** Kipas `sedang`.
3. **JIKA** Suhu `panas` **ATAU** Kelembapan `kering`, **MAKA** Kipas `cepat`.

## Persyaratan Sistem (Prerequisites)

Pastikan Anda telah menginstal Python. Program ini membutuhkan beberapa pustaka eksternal. Anda dapat menginstalnya menggunakan `pip`:

```bash
pip install numpy scikit-fuzzy matplotlib