# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\n Program Konversi Temperatur\n")

celcius = float(input('Masukan suhu dalam celcius: '))
print( 'suhu adalah: ', celcius, " Celcius" )
kelvin = float(input('Masukan suhu dalam kelvin: '))
print( 'suhu adalah: ', kelvin, " kelvin" )
fahrenheit = float(input('Masukan suhu dalam fahrenheit: '))
print( 'suhu adalah: ', fahrenheit, " fahrenheit" )

# reamur

reamur = (4/5) * celcius
print( 'suhu dlm reamur adalah: ', reamur, " Reamur" )

# fahrenheit
#fahrenheit = ((9/5) * celcius) + 32
#print( 'suhu dlm fahrenheit adalah: ', fahrenheit, " Fahrenheit" )

# kelvin
#kelvin = celcius + 273.25
#print( 'suhu dlm kelvin adalah: ', kelvin, " Kelvin" )

# fahrenheit ke kelvin
#kelvin = (5/9  *(fahrenheit - 32)) + 273.15
#print( 'suhu dari Fahrenheit ke kelvin adalah: ', kelvin, " kelvin" )

# kelvin ke fahrenheit
fahrenheit = (9/5 *(kelvin-273.15)) + 32
print( 'suhu kelvin ke fahrenheit adalah: ', fahrenheit, " Fahrenheit" )

12
