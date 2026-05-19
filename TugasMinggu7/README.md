# Klasifikasi Bunga Iris dengan Neural Network

[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat&logo=tensorflow)](https://tensorflow.org)

> Implementasi Neural Network menggunakan TensorFlow/Keras untuk klasifikasi 3 spesies bunga Iris berdasarkan dataset dari UCI Machine Learning Repository.

---

## Tentang Proyek

Proyek ini dibuat untuk memenuhi **Tugas Praktikum Kecerdasan Buatan (Pertemuan 7)** dengan topik **Jaringan Syaraf Tiruan**. Model yang dibangun adalah **Feedforward Neural Network** dengan 4 hidden layer untuk memprediksi kelas bunga Iris berdasarkan ukuran kelopak (sepal) dan mahkota (petal).

### Spesies yang Dikenali:
| Kode | Nama Spesies |
|------|---------------|
| 0 | Iris-setosa |
| 1 | Iris-versicolor |
| 2 | Iris-virginica |

---

## Arsitektur Model

```
┌─────────────────────────────────────────────────────────┐
│                    Input Layer (4 fitur)                 │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│           Dense Layer 1: 1000 neuron (ReLU)              │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│            Dense Layer 2: 500 neuron (ReLU)              │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│            Dense Layer 3: 300 neuron (ReLU)              │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│          Output Layer: 3 neuron (Softmax)                │
└─────────────────────────────────────────────────────────┘
```

**Total Parameter:** ±1.2 juta parameter yang dapat dilatih.

---

## Dataset

| Atribut | Keterangan |
|---------|------------|
| **Sumber** | [UCI Machine Learning Repository - Iris Dataset](https://archive.ics.uci.edu/dataset/53/iris) |
| **Jumlah Sampel** | 150 sampel |
| **Jumlah Fitur** | 4 fitur numerik |
| **Jumlah Kelas** | 3 kelas |
| **Data Splitting** | 80% training, 20% testing |

### Detail Fitur:
- `sepal length` (cm)
- `sepal width` (cm)
- `petal length` (cm)
- `petal width` (cm)

---

## Persyaratan

Pastikan environment Anda memiliki library berikut:

```txt
tensorflow>=2.0.0
pandas>=1.0.0
numpy>=1.19.0
scikit-learn>=0.24.0
matplotlib>=3.3.0
seaborn>=0.11.0
```

### Instalasi Dependensi:
```bash
pip install tensorflow pandas numpy scikit-learn matplotlib seaborn
```

---

## Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/hananaila/tugasminggu7.git
cd tugasminggu7
```

### 2. Download Dataset
Download file `iris.data` dari [link ini](https://archive.ics.uci.edu/static/public/53/iris.zip)  
Ekstrak dan letakkan file `iris.data` di folder yang sama dengan `iris.py`

### 3. Jalankan Program
```bash
python iris.py
```

---

## Hasil yang Diharapkan

| Metrik | Target |
|--------|--------|
| Training Accuracy | > 98% |
| Validation Accuracy | > 95% |
| Testing Accuracy | > 95% |
| Training Loss | < 0.1 |

## Contoh Output

### Prediksi Manual:
```
--- Coba Prediksi Bunga Iris ---
Masukkan sepal length: 5.1
Masukkan sepal width: 3.5
Masukkan petal length: 1.4
Masukkan petal width: 0.2
Prediksi kelas: Iris-setosa
```