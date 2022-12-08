import a as f1

print('coba import')
print('calculator operasi 2 bilangan')
bil1 = int(input('masukkan bilangan 1 :'))
bil2 = int(input('masukkan bilangan 2 :'))

print ('pilih jenis operasi : ')
print('1. penjumlahan')
print('2. pengurangan')
print('3. perkalian')
print('4. pembagian')

pilihan = int(input('jenis operasi yang dipakai:'))
if pilihan == 1:
    print('jadi hasilnya',bil1,'+',bil2,'=', f1.tambah(bil1,bil2))
elif pilihan == 2:
    print('jadi hasilnya',bil1,'-',bil2,'=', f1.kurang(bil1,bil2))
elif pilihan == 3:
    print('jadi hasilnya',bil1,'*',bil2,'=', f1.kali(bil1,bil2))
elif pilihan == 4:
    print('jadi hasilnya',bil1,'/',bil2,'=', f1.bagi(bil1,bil2))
else:
    print('inputan salah')