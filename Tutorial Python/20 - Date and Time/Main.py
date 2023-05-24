# Date and time (Latihan)

import datetime as dt

# hari_ini = dt.date.today()

# print(hari_ini)

# print(f"Hari ini adalah hari = {hari_ini:%A}")
# tanggal = dt.date(2005,10,10)
# print(tanggal)
# print(f"Hari ini adalah hari = {tanggal:%A}")

print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah: {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari= hari_ini - tanggal_lahir
umur_tahun = umur_hari.days//365
umur_bulan_sisa = (umur_hari.days % 30)

print(f"Harinya adalah: {tanggal_lahir:%A}")
print(f"umur anda adalah: {umur_tahun}tahun, {umur_bulan_sisa}bulan")