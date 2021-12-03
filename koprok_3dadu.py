import random


def gambardadu(dadu): 
	'''tampilkan gambar dadu'''
	return [ gambar[int(dadu[i])-1] for i in range(3) ]

def input_number(prompt, kind='int', min=None, max=None):
	inp = 0
	while True:
		try:
			inp = input(prompt)
			if kind=='float':
				inp = float(inp)
			else:
				inp = int(inp)
			if min: assert inp >= min
			if max: assert inp <= max
			break
		except:
			print('--Error: Input tidak valid')
	return inp
		

gambar = [ _ for _ in 'kendi ayam kepiting roda lobster ikan'.split() ]

#jenis game koprok
games = {
'1': ['Match 1 Gambar', 1],
'2': ['Match 2 Gambar', 2],
'3': ['Match Gambar Kembar 2', 5],
'4': ['Match Gambar kembar 3', 50],
}

PILIHAN1234x = ['1','2','3','4','x','r']
PILIHAN123456 = ['1','2','3','4','5','6']
dadu = ['1','1','1']

#Menu
import os
os.system('clear')
print('SIMULASI JUDI KOPROK 3 DADU')
print('---------------------------\n')

print('JENIS PERMAINAN')
while True:
	for k, v in games.items():
		print(f'{k})', v[0],f'--Win{v[1]}x')
	#print('r)', 'Random')
	print('x)', 'eXit')

	pilihgame = input('Pilih Nomor: ').lower()
	if pilihgame in PILIHAN1234x:
		if pilihgame != 'x':
			break
		else:
			quit()
	print('Pilihan tidak valid')

print('\nGAMBAR TARUHAN')
for i,g in enumerate(gambar):
	print(f'{i+1})', g.capitalize())
#print('r)', 'Random')

while True:
	if pilihgame in ['1','3','4']:
		print('Pilih 1 gambar pada Nomor: ', end='')
		pasang = input().lower()
		if pasang in PILIHAN123456:
			break
	else:
		print('Pilih 2 gambar Nomor berapa saja (pisahkan dg spasi): ', end='')
		pasang = input().lower().split()
		if len(pasang) == 2:
			valid = True
			for p in pasang:
				if p not in PILIHAN123456:
					valid = False
			if pasang[0] == pasang[1]:
				valid = False
			if valid:
				break	

	print('Pilihan tidak valid')


#input trial dan taruhan
print()
trial = input_number('Banyaknya x main (min. 1): ', min=1)
taruh = input_number('Nilai sekali taruhan: (min. 1000): ', min=1000)

input('\nEnter untuk mulai..')

data = []

winsx  = 0
hasilx = 0
accutaruh = 0
accuhasil = 0

print('\nKOCOKAN')
for i in range(trial):
	dadu[0] = random.sample(PILIHAN123456, 1)[0]
	dadu[1] = random.sample(PILIHAN123456, 1)[0]
	dadu[2] = random.sample(PILIHAN123456, 1)[0]

	print(f'{i+1}.', ','.join(gambardadu(dadu)), end=' ')

	win = False
	if pilihgame == '1':
		if pasang in dadu:
			win = True

	elif pilihgame == '2':
		if pasang[0] in dadu and pasang[1] in dadu:
			win = True

	elif pilihgame == '3':
		if dadu.count(pasang) >= 2:
			win = True

	else:
		# pilihgame == 4
		if dadu.count(pasang) == 3:
			win = True

	accutaruh += taruh
	if win:
		winsx  += 1
		hasilx += (1 + games[pilihgame][1])
		accuhasil += (1 + games[pilihgame][1]) * taruh
		print(f'\t--Win{games[pilihgame][1]}x--')
	else:
		print()

	data.append(accuhasil-accutaruh)

maxhasil = max(data)
idxhasil = data.index(maxhasil)
menang   = accuhasil-accutaruh

print('\n--Hasil Taruhan--')
print(games[pilihgame][0],f'--Win{games[pilihgame][1]}x\n')

print('Dari', trial, 'kali main, menang', winsx, 'kali')
print('Akumulasi taruhan=', format(accutaruh,'_d'))
print('Akumulasi hasil  =', format(accuhasil,'_d'))
print('Menang           =', format(menang, '_d'))
if maxhasil > 0:
	print('Kemenangan tertinggi =', end=' ')
	print(format(maxhasil,'_d'), 'pada kocokan ke', idxhasil+1)

if trial >= 30:
	expwin = winsx/trial
	exphasil = hasilx/trial

	print('\n--Statistik--')
	print('Ekspektasi wins  =', format(expwin,'.4f'),'kali')
	print('Ekspektasi hasil =', format(exphasil,'.4f'),'nilai taruhan')
	if exphasil > 0:
		print('Jadi...')
		print('Untuk menang 1 juta rupiah,')
		print('anda harus pasang rata2 total', end=' ')
		print(format(int(1e6//exphasil), '_d'), 'rupiah')
