import random
import matplotlib.pyplot as plt
import numpy as np

# Mengimpor fungsi-fungsi dari file lain
from inisiasipopulasi import inisialisasi_populasi
from evaluasifitness import hitung_fitness
from selection import tournament_selection       # Sesuai digit 9
from crossover import one_point_crossover        # Sesuai digit 3
from mutation import uniform_mutation            # Sesuai hasil 9+3=12 (digit 2)

# Data barang: (nama, keuntungan, ukuran)
barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7)
]

def run_ga(jumlah_generasi, jumlah_populasi, prob_crossover, prob_mutasi, kapasitas_tas):
    # Menentukan jumlah gen berdasarkan jumlah barang
    jumlah_gen = len(barang)
    
    # Inisialisasi populasi awal
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)
    
    # Menghitung fitness untuk setiap individu dalam populasi
    fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi]
    
    # List untuk menyimpan nilai fitness terbaik, terburuk, dan rata-rata setiap generasi
    best_fitness_list = []
    worst_fitness_list = []
    avg_fitness_list = []
    all_fitness = []
    
    # Variabel untuk menyimpan individu terbaik secara keseluruhan
    best_individu = None
    best_fitness_overall = 0
    
    # Proses evolusi selama jumlah generasi yang ditentukan
    for generasi in range(jumlah_generasi):
        # Evaluasi fitness populasi saat ini
        fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi]
        
        # Menyimpan nilai fitness untuk plotting
        best_fitness = max(fitness_populasi)
        worst_fitness = min(fitness_populasi)
        avg_fitness = sum(fitness_populasi) / len(fitness_populasi)
        
        best_fitness_list.append(best_fitness)
        worst_fitness_list.append(worst_fitness)
        avg_fitness_list.append(avg_fitness)
        all_fitness.append(fitness_populasi.copy())
        
        # Menyimpan individu terbaik secara keseluruhan
        if best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            index_best = fitness_populasi.index(best_fitness)
            best_individu = populasi[index_best]
            
        new_populasi = []
        used_indices = []
        
        # Membentuk populasi baru
        while len(new_populasi) < jumlah_populasi:
            # 1. SELEKSI: Menggunakan Tournament Selection (Digit 9)
            parent1, idx1 = tournament_selection(populasi, fitness_populasi)
            used_indices.append(idx1)
            
            # Memastikan orang tua kedua berbeda
            available_indices = [i for i in range(len(populasi)) if i not in used_indices]
            
            if not available_indices:
                used_indices = [idx1]
                available_indices = [i for i in range(len(populasi)) if i != idx1]
                
            parent2, _ = tournament_selection(
                [populasi[i] for i in available_indices], 
                [fitness_populasi[i] for i in available_indices]
            )
            used_indices.append(available_indices[_] if _ < len(available_indices) else available_indices[0])
            
            # 2. CROSSOVER: Menggunakan One Point Crossover (Digit 3)
            if random.random() < prob_crossover:
                anak1, anak2 = one_point_crossover(parent1, parent2)
            else:
                anak1, anak2 = parent1[:], parent2[:]
                
            # 3. MUTASI: Menggunakan Uniform Mutation (Digit 2 dari 12)
            if random.random() < prob_mutasi:
                anak1 = uniform_mutation(anak1)
            if random.random() < prob_mutasi:
                anak2 = uniform_mutation(anak2)
                
            # Menambahkan anak ke populasi baru
            new_populasi.extend([anak1, anak2])
            
        # Memastikan populasi baru sesuai dengan jumlah populasi
        populasi = new_populasi[:jumlah_populasi]
        
    # Menampilkan grafik fitness
    plt.figure(figsize=(12, 7))
    
    # Plot semua nilai fitness dengan transparansi rendah
    for i in range(jumlah_generasi):
        x = [i+1]*len(all_fitness[i])
        y = all_fitness[i]
        plt.scatter(x, y, color='gray', alpha=0.1)
        
    # Plot nilai fitness terbaik, terburuk, dan rata-rata
    plt.plot(range(1, jumlah_generasi+1), best_fitness_list, color='blue', label='Fitness Tertinggi')
    plt.plot(range(1, jumlah_generasi+1), worst_fitness_list, color='yellow', label='Fitness Terendah')
    plt.plot(range(1, jumlah_generasi+1), avg_fitness_list, color='red', label='Fitness Rata-rata')
    
    plt.title('Perkembangan Nilai Fitness - NIM H1D024093')
    plt.xlabel('Generasi')
    plt.ylabel('Nilai Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Menampilkan barang yang terpilih dalam knapsack terbaik
    selected_items = [barang[i][0] for i in range(len(best_individu)) if best_individu[i] == 1]
    selected_value = hitung_fitness(best_individu, barang, kapasitas_tas)
    selected_weight = sum([barang[i][2] for i in range(len(best_individu)) if best_individu[i] == 1])
    
    print("=== HASIL OPTIMASI GUDANG ===")
    print(f"Nilai Keuntungan Terbaik : {selected_value}")
    print(f"Total Ukuran Dipakai     : {selected_weight} / {kapasitas_tas}")
    print("Barang Terpilih:")
    for item in selected_items:
        print(f"- {item}")

# Menjalankan GA dengan parameter berikut
run_ga(
    jumlah_generasi=50,
    jumlah_populasi=20,
    prob_crossover=0.5,
    prob_mutasi=0.1,
    kapasitas_tas=15  # Ukuran Maksimal Gudang
)