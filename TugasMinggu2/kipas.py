import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Definisi Variabel (Antecedent & Consequent)
suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan')
kipas = ctrl.Consequent(np.arange(0, 101, 1), 'kecepatan_kipas')

# 2. Himpunan Fuzzy (Segitiga / trimf)
# Himpunan untuk Suhu
suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 18])
suhu['normal'] = fuzz.trimf(suhu.universe, [12, 22, 32])
suhu['panas'] = fuzz.trimf(suhu.universe, [28, 40, 40])

# Himpunan untuk Kelembapan
kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 45])
kelembapan['ideal'] = fuzz.trimf(kelembapan.universe, [35, 55, 75])
kelembapan['basah'] = fuzz.trimf(kelembapan.universe, [65, 100, 100])

# Himpunan untuk Kecepatan Kipas
kipas['lambat'] = fuzz.trimf(kipas.universe, [0, 20, 40])
kipas['sedang'] = fuzz.trimf(kipas.universe, [35, 55, 75])
kipas['cepat'] = fuzz.trimf(kipas.universe, [65, 85, 100])

# 3. Aturan Fuzzy (Fuzzy Rules)
rule1 = ctrl.Rule(suhu['dingin'] & kelembapan['basah'], kipas['lambat'])
rule2 = ctrl.Rule(suhu['normal'] & kelembapan['ideal'], kipas['sedang'])
rule3 = ctrl.Rule(suhu['panas'] | kelembapan['kering'], kipas['cepat'])

mesin_kipas = ctrl.ControlSystem([rule1, rule2, rule3])
simulasi = ctrl.ControlSystemSimulation(mesin_kipas)

# 5. INPUTAN (Skenario Unik)
simulasi.input['suhu'] = 28
simulasi.input['kelembapan'] = 45

# 6. Proses Perhitungan (Defuzzifikasi)
simulasi.compute()

# 7. Output Hasil Kecepatan Kipas
print("==========================================")
print(f"Input Suhu       : 28 °C")
print(f"Input Kelembapan : 45 %")
print(f"Hasil Kecepatan Kipas: {simulasi.output['kecepatan_kipas']:.2f}")
print("==========================================")

# 8. Visualisasi Grafik
suhu.view(sim=simulasi)
kelembapan.view(sim=simulasi)
kipas.view(sim=simulasi)

# Tampilkan semua jendela grafik
plt.show()