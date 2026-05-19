# Klasifikasi Rock Paper Scissors dengan CNN

[![CNN](https://img.shields.io/badge/Model-CNN-4285F4?style=flat)](https://tensorflow.org)

> Implementasi Convolutional Neural Network (CNN) menggunakan TensorFlow/Keras untuk klasifikasi gambar tangan batu, kertas, gunting.

---

## Tentang Proyek

Proyek ini dibuat untuk memenuhi **Tugas Praktikum Kecerdasan Buatan (Pertemuan 8)** dengan topik **Convolutional Neural Network (CNN)**. Model yang dibangun mampu mengklasifikasikan gambar tangan menjadi 3 kategori:

| Kode | Nama Kelas |
|------|------------|
| 0 | Rock (Batu)  |
| 1 | Paper (Kertas)  |
| 2 | Scissors (Gunting)  |

---

## Arsitektur Model

```
┌─────────────────────────────────────────────────────────────┐
│              Input Layer (150x150x3 RGB)                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│         Conv2D(32, 3x3) + ReLU + MaxPooling2D(2,2)          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│         Conv2D(64, 3x3) + ReLU + MaxPooling2D(2,2)          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│        Conv2D(128, 3x3) + ReLU + MaxPooling2D(2,2)          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Flatten + Dense(512, ReLU)                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 Dense(3, Softmax) - Output                   │
└─────────────────────────────────────────────────────────────┘
```

**Total Parameter:** ±18,9 juta parameter yang dapat dilatih.

---

## Dataset

| Atribut | Keterangan |
|---------|------------|
| **Sumber** | [Kaggle - Rock Paper Scissors Dataset](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors?resource=download)|
| **Struktur Folder** | `rockpaperscissors/`, `rock.py`, `README.md` |
| **Ukuran Gambar** | Diresize menjadi 150x150 pixel |
| **Format Warna** | RGB (3 channel) |
| **Data Splitting** | 80% training, 20% validation |

### Struktur Folder:

```
TugasMinggu8/
│
├── rockpaperscissors/
│   ├── rock/
│   ├── paper/
│   └── scissors/
│
├── rock.py              # Source code utama
└── README.md            # Dokumentasi proyek
```

---

## Persyaratan

Pastikan environment Anda memiliki library berikut:

```txt
tensorflow>=2.0.0
numpy>=1.19.0
pandas>=1.0.0
Pillow>=8.0.0
```

### Instalasi Dependensi:
```bash
pip install tensorflow numpy pandas Pillow
```

---

## Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/hananaila/tugasminggu8.git
cd tugasminggu8
```

### 2. Download Dataset
Download dataset dari [Kaggle - Rock Paper Scissors](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors)

Ekstrak sehingga struktur foldernya menjadi:
```
./rockpaperscissors/
    ├── rock/
    ├── paper/
    └── scissors/
```

### 3. Jalankan Program
```bash
python rock.py
```

---

## Hasil yang Diharapkan

| Metrik | Target |
|--------|--------|
| Training Accuracy | > 85% |
| Validation Accuracy | > 80% |
| Validation Loss | < 0.5 |

---

## Parameter Training

| Parameter | Nilai |
|-----------|-------|
| **Epochs** | 10 |
| **Batch Size** | 32 |
| **Optimizer** | Adam |
| **Loss Function** | categorical_crossentropy |
| **Validation Split** | 20% |

---
