import tkinter as tk
from tkinter import messagebox

database_kerusakan = {
    "RAM Rusak": {
        "gejala": ["beep", "blank", "bsod"],
        "solusi": "Coba cabut RAM, bersihkan pin kuningan dengan penghapus bersih, lalu pasang kembali."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["mati_mendadak", "kipas_sebentar", "bau_hangus"],
        "solusi": "Periksa kabel power. Jika tercium bau hangus, segera ganti PSU dengan daya memadai."
    },
    "Overheat (Prosesor)": {
        "gejala": ["kipas_bising", "mati_lama", "kinerja_lambat"],
        "solusi": "Bersihkan tumpukan debu pada heatsink/kipas prosesor dan segera ganti thermal paste."
    },
    "VGA Bermasalah": {
        "gejala": ["garis_aneh", "warna_pudar", "freeze"],
        "solusi": "Periksa kabel monitor, update driver grafis, dan bersihkan pin konektor VGA."
    },
    "Hardisk Corrupt / Bad Sector": {
        "gejala": ["booting_lama", "bunyi_klik", "gagal_baca"],
        "solusi": "Segera backup data penting Anda, lakukan scan bad sector, dan pertimbangkan ganti ke SSD."
    },
    "Baterai CMOS Habis / Rusak": {
        "gejala": ["waktu_reset", "pesan_cmos_error", "bios_default"],
        "solusi": "Ganti baterai CMOS (tipe bulat pipih CR2032) di motherboard, lalu atur ulang jam dan tanggal di BIOS."
    }
}

# DAFRAT PERTANYAAN GEJALA
semua_gejala = [
    ("beep", "Apakah terdengar bunyi beep berulang kali saat komputer dinyalakan?"),
    ("blank", "Apakah layar blank hitam (no display) padahal mesin menyala?"),
    ("bsod", "Apakah sering terjadi Blue Screen (BSOD)?"),
    ("mati_mendadak", "Apakah komputer mati tiba-tiba saat menjalankan aplikasi berat?"),
    ("kipas_sebentar", "Apakah kipas menyala sebentar lalu mati lagi saat tombol power ditekan?"),
    ("bau_hangus", "Apakah ada bau hangus dari dalam casing?"),
    ("kipas_bising", "Apakah kipas prosesor berputar sangat kencang dan bising?"),
    ("mati_lama", "Apakah komputer sering mati mendadak setelah menyala beberapa saat?"),
    ("kinerja_lambat", "Apakah kinerja komputer melambat drastis saat dipakai lama?"),
    ("garis_aneh", "Apakah muncul garis-garis aneh pada monitor?"),
    ("warna_pudar", "Apakah warna pada layar terlihat memudar atau resolusi terkunci?"),
    ("freeze", "Apakah tampilan layar sering patah-patah atau freeze?"),
    ("booting_lama", "Apakah proses booting Windows memakan waktu sangat lama?"),
    ("bunyi_klik", "Apakah terdengar bunyi 'klik-klik' mekanik dari dalam casing?"),
    ("gagal_baca", "Apakah sering gagal saat membaca, menyalin, atau menyimpan file?"),
    ("waktu_reset", "Apakah jam dan tanggal di Windows sering ngaco saat komputer dinyalakan?"),
    ("pesan_cmos_error", "Apakah muncul pesan 'CMOS Checksum Error' atau minta tekan F1 saat pertama kali nyala?"),
    ("bios_default", "Apakah pengaturan BIOS selalu kembali ke setelan awal setiap kali komputer dimatikan?")
]

class AplikasiPakarKomputer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Komputer")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # Label Judul/Pertanyaan 
        self.label_tanya = tk.Label(root, text="Selamat Datang di Sistem Pakar\nDiagnosa Kerusakan Komputer", 
                                    font=("Arial", 12), wraplength=450, justify="center")
        self.label_tanya.pack(pady=30)

        # Tombol Mulai
        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", bg="blue", fg="white", 
                                   font=("Arial", 10, "bold"), command=self.mulai_tanya)
        self.btn_mulai.pack(pady=10)

        # Frame Tombol Jawaban
        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=10, bg="green", fg="white", 
                                font=("Arial", 9, "bold"), command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=10, bg="red", fg="white", 
                                   font=("Arial", 9, "bold"), command=lambda: self.jawab('t'))
        self.btn_ya.pack(side=tk.LEFT, padx=15)
        self.btn_tidak.pack(side=tk.LEFT, padx=15)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            # Jika user jawab YA, simpan kode gejalanya
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)
            
        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        kerusakan_ditemukan = []
        
        for penyakit, data in database_kerusakan.items():
            syarat_gejala = data["gejala"]
            # Cek apakah semua gejala untuk kerusakan ini ada di gejala_terpilih user
            if all(s in self.gejala_terpilih for s in syarat_gejala):
                kerusakan_ditemukan.append((penyakit, data["solusi"]))
                
        # Menyiapkan Teks Output
        if kerusakan_ditemukan:
            pesan_hasil = "Berdasarkan gejala Anda, komputer mengalami:\n"
            for nama, solusi in kerusakan_ditemukan:
                pesan_hasil += f"\n>> {nama.upper()}\nSolusi: {solusi}\n"
        else:
            pesan_hasil = "Selamat! Komputer Anda sepertinya dalam kondisi sehat karena tidak ada gejala kerusakan yang terdeteksi."
            
        # Tampilkan Pop-up Hasil
        messagebox.showinfo("Hasil Diagnosa", pesan_hasil)

        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.btn_mulai.config(text="Diagnosa Ulang")
        self.label_tanya.config(text="Diagnosa Selesai.\nApakah Anda ingin mengulang?")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x250") 
    app = AplikasiPakarKomputer(root)
    root.mainloop()