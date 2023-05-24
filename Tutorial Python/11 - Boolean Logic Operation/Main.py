# operasi logika atau boolean

#not, or , and, xor

print('====NOT====')
a = True
c = not a

print('data a =', a)
print('---- NOT')
print('data c =', c)

print('====OR====') #() jika salah satu true, maka hasilnya adl true)
a = True
b = False
c = a or b
print( a, 'OR', b, '=', c)
a = False
b = False
c = a or b
print( a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print( a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print( a, 'OR', b, '=', c)

print('====AND====') #() jika dua buah nilai true, maka hasilnya adl true)
a = True
b = False
c = a and b
print( a, 'and', b, '=', c)
a = False
b = False
c = a and b
print( a, 'and', b, '=', c)
a = False
b = True
c = a and b
print( a, 'and', b, '=', c)
a = True
b = True
c = a and b
print( a, 'and', b, '=', c)


print('====XOR====') #() akan true, jika salah satu true, sisanya akan false)
a = True
b = False
c = a ^ b
print( a, '^', b, '=', c)
a = False
b = False
c = a ^ b
print( a, '^', b, '=', c)
a = False
b = True
c = a ^ b
print( a, '^', b, '=', c)
a = True
b = True
c = a ^ b
print( a, '^', b, '=', c)