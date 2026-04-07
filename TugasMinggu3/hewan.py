import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Mendefinisikan Variabel Input dan Output
terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'terjual')
permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')
harga = ctrl.Antecedent(np.arange(0, 100001, 1000), 'harga')
profit = ctrl.Antecedent(np.arange(0, 4000001, 10000), 'profit')

stok = ctrl.Consequent(np.arange(0, 1001, 1), 'stok')

# 2. Mendefinisikan Himpunan Fuzzy berdasarkan grafik
terjual['rendah'] = fuzz.trapmf(terjual.universe, [0, 0, 20, 40])
terjual['sedang'] = fuzz.trimf(terjual.universe, [20, 50, 70])
terjual['tinggi'] = fuzz.trapmf(terjual.universe, [50, 90, 100, 100])

permintaan['rendah'] = fuzz.trapmf(permintaan.universe, [0, 0, 100, 150])
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [100, 150, 200])
permintaan['tinggi'] = fuzz.trapmf(permintaan.universe, [150, 200, 300, 300])

harga['murah'] = fuzz.trapmf(harga.universe, [0, 0, 30000, 50000])
harga['sedang'] = fuzz.trimf(harga.universe, [20000, 50000, 80000])
harga['mahal'] = fuzz.trapmf(harga.universe, [50000, 80000, 100000, 100000])

profit['rendah'] = fuzz.trapmf(profit.universe, [0, 0, 1500000, 2500000])
profit['sedang'] = fuzz.trimf(profit.universe, [1500000, 2500000, 3500000])
profit['tinggi'] = fuzz.trapmf(profit.universe, [2500000, 3500000, 4000000, 4000000])

stok['sedang'] = fuzz.trapmf(stok.universe, [0, 0, 600, 900])
stok['banyak'] = fuzz.trapmf(stok.universe, [600, 900, 1000, 1000])

# 3. Mendefinisikan Rules
rule1 = ctrl.Rule(terjual['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok['banyak'])
rule2 = ctrl.Rule(terjual['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule3 = ctrl.Rule(terjual['tinggi'] & permintaan['sedang'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule4 = ctrl.Rule(terjual['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule5 = ctrl.Rule(terjual['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok['banyak'])
rule6 = ctrl.Rule(terjual['rendah'] & permintaan['rendah'] & harga['sedang'] & profit['sedang'], stok['sedang'])

# 4. Membuat Control System dan Simulasi
stok_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
simulasi_stok = ctrl.ControlSystemSimulation(stok_ctrl)

# 5. Memasukkan Input dari Studi Kasus
simulasi_stok.input['terjual'] = 80
simulasi_stok.input['permintaan'] = 255
simulasi_stok.input['harga'] = 25000
simulasi_stok.input['profit'] = 3500000

# 6. Melakukan Perhitungan dan Menampilkan Hasil
simulasi_stok.compute()
print("--- Hasil Studi Kasus 1: Udin Pet Shop ---")
print(f"Output Stok Makanan yang optimal : {simulasi_stok.output['stok']:.2f} unit")

# 7. Menampilkan Grafik
stok.view(sim=simulasi_stok)
plt.title("Grafik Output: Stok Makanan")
plt.show()