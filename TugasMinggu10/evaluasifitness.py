# Data barang (nama, keuntungan, bobot/ukuran)
barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7)
]
kapasitas_tas = 15 # Kapasitas maksimum gudang (sesuai modul 10)

# Fungsi untuk menghitung nilai fitness
def hitung_fitness(kromosom, barang, kapasitas_tas):
    total_harga = 0
    total_bobot = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_harga += barang[i][1]
            total_bobot += barang[i][2]
            
    if total_bobot > kapasitas_tas:
        return 0 # Penalti jika melebihi kapasitas
    else:
        return total_harga

# Definisi contoh populasi awal
populasi_awal = [
    [1, 0, 1, 0, 1], # Contoh kromosom individu
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1],
    # Tambahkan lebih banyak individu sesuai kebutuhan
]

# Contoh penggunaan
if __name__ == "__main__":
    fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi_awal]

    # Menampilkan nilai fitness
    print("\nNilai Fitness:")
    for idx, fitness in enumerate(fitness_populasi):
        print(f"Individu {idx+1}: Fitness = {fitness}")