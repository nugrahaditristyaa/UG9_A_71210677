#Membuat catatan pemesanan dan penghitung pengeluaran pelanggan.

i = 25000
e = 6000
r = 8000

print("=====MASUKAN JUMLAH MAKANAN YANG DIPESAN=====")
i1 = int(input("IKAN BAKAR       Rp 25.000,00   : "))
e2 = int(input("ES DOGER         Rp 6.000,00    : "))
r3 = int(input("RUJAK            Rp 8.000,00    : "))

print("=====TOTAL=====")
print("TOTAL IKAN BAKAR    : Rp ", (i*i1))
print("TOTAL ES DOGER      : Rp ", (e*e2))
print("TOTAL RUJAK CINGUR  : Rp ", (r*r3))

print("Jumlah total biaya yang harus dibayar adalah Rp ", ((i*i1)+(e*e2)+(r*r3)))



