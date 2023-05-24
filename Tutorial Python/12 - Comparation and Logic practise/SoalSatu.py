# soal satu
# ----0++++5----8++++11----

#inputUser= float(input('masukan angka yang \nlebih besar dari 0 \ndan \nkurang dari 5 \n:'))

#print('\n', 10*'=', '\n')
#inputUser= float(input('masukan angka yang \nlebih besar dari 8 \ndan \nkurang dari 11 \n:'))
#lebih dari 8 (----8++++)

print('\n', 10*'=', '\n')
inputUser= float(input('masukan angka yang \nlebih besar dari 0 \ndan \nkurang dari 5 \natau \nlebih besar dari 8 \ndan \nkurang dari 11\n:'))
#lebih besar dari 0 (-----0++++++)
isBesarDari = inputUser > 0
print('lebih besar dari 0 =', isBesarDari)

#kurang dari 5 (++++5----)
isKurangDari = inputUser < 5
print('kurang dari 5 =', isKurangDari)

#----0++++5---- 
isCorrectA = isBesarDari and isKurangDari
print('angka yg anda masukan = ', isCorrectA)
isBesarDari = inputUser > 8
print('lebih besar dari 8 =', isBesarDari)

#kurang dari 11 (++++11----)
isKurangDari = inputUser < 11
print('kurang dari 11 =', isKurangDari)

#----8++++11---- 
isCorrectB = isBesarDari and isKurangDari
print('angka yg anda masukan = ', isCorrectB)

isCorrectTotal = isCorrectA or isCorrectB
print('angka yg anda masukan: ', isCorrectTotal)
#lebih dari 8 (----8++++)


print('\n==== Jawaban ====\n')
# ----0++++5----8++++11----
Angka=float(input('masukan angka 0<x<5 or 8<x<11 \n:'))
A= (Angka>0)
B= (Angka<5)
C= (Angka>8)
D= (Angka<11)
Hasil=(A and B) or (C and D)
print('angka yg dimasukan: ',Hasil)

print('\n ==== alternative ==== \n')
x = float(input('masukan angka 0<x<5 or 8<x<11 \n: '))
y = 0<x<5 or 8<x<11
z = (x>0 and x<5) or (x>8 and x<11)
print(y, '\n',z)