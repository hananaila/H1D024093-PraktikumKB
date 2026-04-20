import tkinter as tk
from tkinter import messagebox

# DATABASE PENYAKIT & GEJALA
database_penyakit = {
    "Tonsilitis":               ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris":     ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis":      ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Ethmoidalis":    ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis":    ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler":       ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis":               ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring":            ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum":           ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis":               ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala":    ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut":        ["G37", "G20", "G35", "G31"],
    "Contact Ulcers":           ["G5", "G2"],
    "Abses Parafaringeal":      ["G5", "G16"],
    "Barotitis Media":          ["G12", "G20"],
    "Kanker Nasofaring":        ["G17", "G8"],
    "Kanker Tonsil":            ["G6", "G29"],
    "Neuronitis Vestibularis":  ["G35", "G24"],
    "Meniere":                  ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik":  ["G29"],
    "Osteosklerosis":           ["G34", "G9"],
    "Vertigo Postular":         ["G24"],
}

# DAFTAR GEJALA
semua_gejala = [
    ("G1",  "Apakah Anda mengalami nafas yang abnormal?"),
    ("G2",  "Apakah suara Anda terdengar serak?"),
    ("G3",  "Apakah ada perubahan pada kulit Anda?"),
    ("G4",  "Apakah telinga Anda terasa penuh?"),
    ("G5",  "Apakah Anda nyeri saat bicara atau menelan?"),
    ("G6",  "Apakah Anda merasakan nyeri tenggorokan?"),
    ("G7",  "Apakah leher Anda terasa nyeri?"),
    ("G8",  "Apakah terjadi pendarahan pada hidung?"),
    ("G9",  "Apakah telinga Anda berdenging?"),
    ("G10", "Apakah air liur Anda sering menetes?"),
    ("G11", "Apakah ada perubahan pada suara Anda?"),
    ("G12", "Apakah Anda merasakan sakit kepala?"),
    ("G13", "Apakah ada nyeri di pinggir hidung?"),
    ("G14", "Apakah Anda mengalami serangan vertigo?"),
    ("G15", "Apakah kelenjar getah bening Anda terganggu?"),
    ("G16", "Apakah leher Anda terlihat bengkak?"),
    ("G17", "Apakah hidung Anda tersumbat?"),
    ("G18", "Apakah Anda mengalami infeksi sinus?"),
    ("G19", "Apakah berat badan Anda turun drastis?"),
    ("G20", "Apakah telinga Anda terasa nyeri?"),
    ("G21", "Apakah selaput lendir Anda berwarna merah?"),
    ("G22", "Apakah ada benjolan di leher Anda?"),
    ("G23", "Apakah tubuh Anda terasa tidak seimbang?"),
    ("G24", "Apakah bola mata Anda bergerak tidak terkontrol?"),
    ("G25", "Apakah wajah Anda terasa nyeri?"),
    ("G26", "Apakah dahi Anda terasa sakit?"),
    ("G27", "Apakah Anda mengalami batuk?"),
    ("G28", "Apakah ada sesuatu yang tumbuh di mulut Anda?"),
    ("G29", "Apakah ada benjolan di leher Anda?"),
    ("G30", "Apakah ada nyeri di antara kedua mata?"),
    ("G31", "Apakah gendang telinga Anda mengalami radang?"),
    ("G32", "Apakah tenggorokan Anda terasa gatal?"),
    ("G33", "Apakah hidung Anda meler?"),
    ("G34", "Apakah Anda mengalami ketulian?"),
    ("G35", "Apakah Anda merasa mual atau muntah?"),
    ("G36", "Apakah Anda merasa lemas dan lesu?"),
    ("G37", "Apakah Anda mengalami demam?"),
]

# APLIKASI 
class AplikasiPakarTHT:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#F5F5F5")

        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # Label kode gejala
        self.label_kode = tk.Label(
            root, text="", font=("Arial", 8),
            fg="#9E9E9E", bg="#F5F5F5"
        )
        self.label_kode.pack(pady=(20, 0))

        # Label pertanyaan utama
        self.label_tanya = tk.Label(
            root,
            text="Selamat Datang di Sistem Pakar\nDiagnosa Penyakit THT",
            font=("Arial", 12), wraplength=440,
            justify="center"
        )
        self.label_tanya.pack(pady=18)

        # Tombol Mulai
        self.btn_mulai = tk.Button(
            root, text="Mulai Diagnosa",
            bg="#2196F3", fg="white",
            activebackground="#1976D2", activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat", padx=16, pady=6,
            cursor="hand2",
            command=self.mulai_tanya
        )
        self.btn_mulai.pack(pady=6)

        # Frame tombol JAWABAN
        self.frame_jawaban = tk.Frame(root, bg="#F5F5F5")

        self.btn_ya = tk.Button(
            self.frame_jawaban, text="YA", width=10,
            bg="#4CAF50", fg="white",
            activebackground="#388E3C", activeforeground="white",
            font=("Arial", 9, "bold"),
            relief="flat", pady=5, cursor="hand2",
            command=lambda: self.jawab('y')
        )
        self.btn_tidak = tk.Button(
            self.frame_jawaban, text="TIDAK", width=10,
            bg="#F44336", fg="white",
            activebackground="#C62828", activeforeground="white",
            font=("Arial", 9, "bold"),
            relief="flat", pady=5, cursor="hand2",
            command=lambda: self.jawab('t')
        )
        self.btn_ya.pack(side=tk.LEFT, padx=12)
        self.btn_tidak.pack(side=tk.LEFT, padx=12)

        # Label progress di bawah
        self.label_progress = tk.Label(
            root, text="", font=("Arial", 8)
        )
        self.label_progress.pack(side=tk.BOTTOM, pady=8)

    # LOGIKA
    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=16)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_kode.config(text=f"[{kode}]")
            self.label_tanya.config(text=teks)
            self.label_progress.config(
                text=f"Pertanyaan {self.index_pertanyaan + 1} dari {len(semua_gejala)}"
            )
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)
        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        diagnosa = [
            p for p, syarat in database_penyakit.items()
            if all(s in self.gejala_terpilih for s in syarat)
        ]

        if diagnosa:
            hasil_teks = "Berdasarkan gejala yang Anda pilih,\nkemungkinan penyakit:\n\n"
            for p in diagnosa:
                hasil_teks += f"  •  {p}\n"
            hasil_teks += "\n⚠ Segera konsultasikan ke dokter THT."
        else:
            hasil_teks = "Tidak ada penyakit yang terdeteksi\nberdasarkan gejala yang dipilih."

        messagebox.showinfo("Hasil Diagnosa", hasil_teks)

        # Reset
        self.frame_jawaban.pack_forget()
        self.label_kode.config(text="")
        self.label_progress.config(text="")
        self.label_tanya.config(text="Diagnosa selesai.\nIngin melakukan pengecekan lagi?")
        self.btn_mulai.config(text="Diagnosa Ulang")
        self.btn_mulai.pack(pady=6)


# MAIN
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPakarTHT(root)
    root.mainloop()