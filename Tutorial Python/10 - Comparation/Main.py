# operasi komparasi

# setiap hasil dari operasi komparasi adl boolean

# >, <, >= , <=, ==, !=, is, is not

a = 4
b = 2
print('========= > ==========')
# lebih besar dari >
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

print('========= < ==========')
# lebih kecil dari <
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

print('========= >= ==========')
# lebih dari sama dengan >=
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

print('========= <= ==========')
# lebih kecil dari sama dengan <=
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

print('========= == ==========')
# sama dengan ==
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 3
print(b, '==', 3, '=', hasil)
hasil = b == 2
print(b, '==', 2, '=', hasil)

print('========= != ==========')
# sama dengan !=
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 3
print(b, '!=', 3, '=', hasil)
hasil = b != 2
print(b, '!=', 2, '=', hasil)

print('========= object identity (is) ==========')
# 'is' sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y =', y , ', id', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y =', y , ', id', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

print('========= object identity (is not) ==========')
# 'is' sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y =', y , ', id', hex(id(y)))
hasil = x is not y
print('x is y = ', hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x = ', x, ', id = ', hex(id(x)))
print('nilai y =', y , ', id', hex(id(y)))
hasil = x is not y
print('x is y = ', hasil)