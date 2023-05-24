# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka3


# ++++++3--------10++++++

inputUser = float(input("masukan angka yg bernilai\nkurang dr 3 \natau \nlebih dari 10 \n:"))

# +++++3---------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# ---------10++++
# Memeriksa angka lebih dari 10
isLebihDari = ( inputUser > 10)
print("Lebih dari 10 = ",isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukan: ', isCorrect)

print('\n', 10*'=' ,'\n')

inputUser = float(input("masukan angka yg bernilai\nlebih dr 3 \ndan \nkurang dari 10 \n:"))

# -----3++++++++++
# memeriksa angka lebih dari 3

isLebihDari = (inputUser > 3)
print("lebih dari 3 =", isLebihDari)

# +++++++++10-----
# Memeriksa angka kurang dari 10
isKurangDari = ( inputUser < 10)
print("kurang dari 10 = ",isKurangDari)

isCorrect = isLebihDari and isKurangDari
print('angka yang anda masukan: ', isCorrect)

