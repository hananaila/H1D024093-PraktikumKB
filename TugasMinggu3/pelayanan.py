import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Mendefinisikan Variabel Input dan Output
informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'informasi')
persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'persyaratan')
petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'petugas')
sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'sarpras')

kepuasan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan')

# 2. Mendefinisikan Himpunan Fuzzy
for var in [informasi, persyaratan, petugas, sarpras]:
    var['tidak_memuaskan'] = fuzz.trapmf(var.universe, [0, 0, 60, 75])
    var['cukup_memuaskan'] = fuzz.trimf(var.universe, [60, 75, 90])
    var['memuaskan'] = fuzz.trapmf(var.universe, [75, 90, 100, 100])

kepuasan['tidak_memuaskan'] = fuzz.trapmf(kepuasan.universe, [0, 0, 50, 100])
kepuasan['kurang_memuaskan'] = fuzz.trimf(kepuasan.universe, [50, 100, 150])
kepuasan['cukup_memuaskan'] = fuzz.trapmf(kepuasan.universe, [150, 175, 250, 275])
kepuasan['memuaskan'] = fuzz.trapmf(kepuasan.universe, [250, 275, 325, 350])
kepuasan['sangat_memuaskan'] = fuzz.trapmf(kepuasan.universe, [325, 350, 400, 400])

# --- Informasi Tidak Memuaskan ---
rule1 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
rule2 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['tidak_memuaskan'])
rule3 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['tidak_memuaskan'])
rule4 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
rule5 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['tidak_memuaskan'])
rule6 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['kurang_memuaskan'])
rule7 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
rule8 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['kurang_memuaskan'])
rule9 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule10 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
rule11 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['tidak_memuaskan'])
rule12 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['kurang_memuaskan'])
rule13 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
rule14 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['kurang_memuaskan'])
rule15 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule16 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['kurang_memuaskan'])
rule17 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule18 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule19 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
rule20 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['kurang_memuaskan'])
rule21 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule22 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['kurang_memuaskan'])
rule23 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule24 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule25 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan'])
rule26 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule27 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])

# --- Informasi Cukup Memuaskan ---
rule28 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
rule29 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['tidak_memuaskan'])
rule30 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['kurang_memuaskan'])
rule31 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
rule32 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['kurang_memuaskan'])
rule33 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule34 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['kurang_memuaskan'])
rule35 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule36 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule37 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
rule38 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['kurang_memuaskan'])
rule39 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule40 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['kurang_memuaskan'])
rule41 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule42 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule43 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan'])
rule44 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule45 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule46 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['kurang_memuaskan'])
rule47 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule48 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule49 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan'])
rule50 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule51 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule52 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan'])
rule53 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan'])
rule54 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan'])

# --- Informasi Memuaskan ---
rule55 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
rule56 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['kurang_memuaskan'])
rule57 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule58 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['kurang_memuaskan'])
rule59 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule60 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule61 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan'])
rule62 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule63 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule64 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['kurang_memuaskan'])
rule65 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule66 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
rule67 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan'])
rule68 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule69 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule70 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan'])
rule71 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan'])
rule72 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan'])
rule73 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan'])
rule74 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
rule75 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule76 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan'])
rule77 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan'])
rule78 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan'])
rule79 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['memuaskan'])
rule80 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['sangat_memuaskan'])
rule81 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan'])

# 4. Membuat Control System dari 81 Aturan
kepuasan_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
    rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
    rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
    rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
    rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
    rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60,
    rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70,
    rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80,
    rule81
])
simulasi_kepuasan = ctrl.ControlSystemSimulation(kepuasan_ctrl)

# 5. Memasukkan Input dari Studi Kasus
simulasi_kepuasan.input['informasi'] = 80
simulasi_kepuasan.input['persyaratan'] = 60
simulasi_kepuasan.input['petugas'] = 50
simulasi_kepuasan.input['sarpras'] = 90

# 6. Menjalankan Perhitungan
simulasi_kepuasan.compute()

# 7. Menampilkan Hasil dan Grafik
print("--- Hasil Studi Kasus 2: Pelayanan Masyarakat ---")
print("Input Kejelasan Informasi   : 80")
print("Input Kejelasan Persyaratan : 60")
print("Input Kemampuan Petugas     : 50")
print("Input Ketersediaan Sarpras  : 90")
print(f"Output Tingkat Kepuasan Pelayanan : {simulasi_kepuasan.output['kepuasan']:.2f}")

kepuasan.view(sim=simulasi_kepuasan)
plt.title("Grafik Output: Kepuasan Pelayanan")
plt.show()