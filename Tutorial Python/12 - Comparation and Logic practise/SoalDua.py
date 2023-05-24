# soal dua
# ++++0----5++++8----11++++

#inputUser= float(input('masukan angka yang \nkurang dari 0 \natau \nlebih dari 5 \n:'))

#print('\n', 10*'=', '\n')
#inputUser= float(input('masukan angka yang \nlebih besar dari 8 \ndan \nkurang dari 11 \n:'))
#lebih dari 8 (----8++++)

print('\n', 10*'=', '\n')
inputUser= float(input('masukan angka yang \nkurang dari 0 \natau \nlebih dari 5 \ndan \nkurang dari 8 \natau \nlebih dari 11\n:'))
#kurang dari 0 (++++0----)
isKurangDari = inputUser < 0
print('kurang dari 0 =', isKurangDari)

#lebih dari 5 (----5++++)
isLebihDari = inputUser > 5
print('lebih dari 5 =', isLebihDari)

#----0++++5---- 
isCorrectA = isKurangDari or isLebihDari
print('angka yg anda masukan = ', isCorrectA)
isKurangDari = inputUser < 8
print('Kurang dari 8 =', isKurangDari)

#kurang dari 11 (++++11----)
isLebihDari = inputUser > 11
print('lebih dari 11 =', isLebihDari)

#----8++++11---- 
isCorrectB = isKurangDari or isLebihDari
print('angka yg anda masukan = ', isCorrectB)

isCorrectTotal = isCorrectA and isCorrectB
print('angka yg anda masukan: ', isCorrectTotal)
#lebih dari 8 (----8++++)

print('\n ====== Jawaban ===== \n')
# ++++0----5++++8----11++++
X= float(input('Masukan angka 0>x atau 5<x<8 atau 11<x \n:'))
A = (X<0)
B = (X>5)
C = (X<8)
D = (X>11)
Hasil = (A or B) and (C or D)
print('ANgka yg anda masukan: ', Hasil)

print('\n ==== alternative ==== \n')
x = float(input('masukan angka 0>x atau 5<x<8 atau 11<x \n:'))
y = 0<x or 5<x<8 or 11<x
z = x>0 or x>5 and x>8 or x>11
print(y,'\n',z)
