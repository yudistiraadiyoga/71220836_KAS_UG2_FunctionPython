def volume_tabung(d,t):
    r = d/2
    v = 3.14*(r**2)*t
    return v

def volume_kubus(s):
    v = s**3
    return v

def volume_balok(p,l,t):
    v = p*l*t
    return v

print('='*20,' KALKULATOR CERDAS ','='*20)
print('Pilihlah bangun yang ingin anda hitung(inputan angka saja) :')
print('1. Tabung')
print('2. Kubus')
print('3. Balok')
pilih = int(input('>> '))
if pilih == 1:
    d = int(input('Masukkan diameter(cm)\t: '))
    t = int(input('Masukkan tinggi(cm)\t: '))
    print(f'Hasil\t\t\t: {volume_tabung(d,t)} cm')
elif pilih == 2:
    s = int(input('Masukkan sisi(cm)\t: '))
    print(f'Hasil\t\t\t: {volume_kubus(s)} cm')
elif pilih == 3:
    p = int(input('Masukkan panjang(cm)\t: '))
    l = int(input('Masukkan lebar(cm)\t: '))
    t = int(input('Masukkan tinggi(cm)\t: '))
    print(f'Hasil\t\t\t: {volume_balok(p,l,t)} cm')
else:
    print('Pilihan tidak tersedia !!')