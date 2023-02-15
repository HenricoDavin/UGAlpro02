#input
detik1 = int(input('Masukkan detik: '))

#proses
konMenit = 60
konJam = konMenit*60
konHari = konJam*24

hari = detik1 // konHari
sisa_detik_hari = detik1 % konHari

jam = sisa_detik_hari // konJam
sisa_detik_jam = detik1 % konJam

menit = sisa_detik_jam // konMenit
sisa_detik_menit = detik1 % konMenit

detik2 = sisa_detik_menit

#output
print (f'{hari} hari, {jam} jam, {menit} menit, {detik2} detik')