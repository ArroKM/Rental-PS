# Coded by AseCx
# App Pemesanan Rental PS 24 jam
import os, re
from time import sleep

class Sewa:
	def __init__(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		satu = [["No"],["Nama"],["Durasi"],["Harga"],["Waktu mulai"],["Waktu selesai"]]
		self.menu = "\n\t{** Rental PS 24 Jam **}\n\n[*] Harga Rental PS : 4000/jam\n"
		self.data(satu, 0)

	def data(self, satu, noom):
		nom = 0
		os.system('cls' if os.name == 'nt' else 'clear')
		print("="*50+self.menu+"="*50)
		while True:
			nom += 1
			nam = nom+noom
			print("\n[*] Pesan Sekarang")
			satu[1].append(input("[?] Nama      : "))
			jum = int(input("[?] Durasi/Jam      : "))
			tgl = input("[?] Main Tanggal Berapa : ")
			jam = input("[?] Main Jam berapa     : ")
			if int(jam) >= 24:
				print("[!] Masukan dengan format 24 jam")
				sleep(5)
				self.data(satu, noom)
			print("="*50)
			try:
				noo = 0
				for i in range(len(satu[0])-1):
					noo += 1
					ju = re.findall('\\d+', str(satu[4][noo]))
					if str(tgl)+str(jam)+"00" == str(ju[0]+ju[1]+ju[2]):
						print(f"Pesanan di Tanggal {tgl}, jam {jam}:00 Sudah ada")
						sleep(3)
						bak = input("\nPesan lagi (Y/T) : ")
						if bak == "T" or bak == "t":
							self.tampil(satu, noom)
						else:
							self.data(satu, noom)
			except IndexError: pass
			except TypeError: pass
			no = 0
			for i in range(jum):
				no += 1
				if no >= jum:
					satu[2].append(f"{str(jum)} Jam")
					satu[3].append(jum*4000)
					satu[4].append(f"Tgl {str(tgl)}, {str(jam)}:00")
					satu[5].append(f"Tgl {str(tgl)}, {str(int(jam)+jum)}:00")
					satu[0].append(str(nam))

			print("[*] Pesanan Berhasil")
			print("="*50)
			pol = input("(?) Pesan Lagi (Y/T) : ")
			if pol == "T" or pol == "t":
				self.tampil(satu, nam)

	def pesanan(self, satu):
		if len(satu[0]) == 1:
			print("\n[*] Semua Pesanan Anda")
			print("[!] Pesanan kosong")
			sleep(5)
		else:
			nol = 0
			print("\n[*] Semua Pesanan Anda\n")
			for i in range(len(satu[0])-1):
				nol += 1
				print(f"\n{str(satu[0][0])} : {str(satu[0][nol])}")
				print(f"{str(satu[1][0])} : {str(satu[1][nol])}")
				print(f"{str(satu[2][0])} : {str(satu[2][nol])}")
				print(f"{str(satu[3][0])} : {str(satu[3][nol])}")
				print(f"{str(satu[4][0])} : {str(satu[4][nol])}")
				print(f"{str(satu[5][0])} : {str(satu[5][nol])}")

	def tampil(self, satu, nam):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("="*50+self.menu+"="*50)
		print("(A) Lihat Pesanan\n(B) Batalkan Pesanan\n(C) Pesan Lagi")
		print("="*50)
		pul = input("(<<( pilih )>>) : ")
		print("="*50)
		if pul == "A" or pul == "a":
			self.pesanan(satu)
			sleep(7)
			self.tampil(satu, nam)

		elif pul == "B" or pul == "b":
			de = int(input("Masukan No pesanan : "))
			za = 0
			for z in range(len(satu[0])-1):
				za += 1
				if str(de) == str(satu[0][za]):
					for i in satu:
						del i[za]
						print(f"Pesanan No {de} di batalkan")
						sleep(5)
						self.pesanan(satu)
						sleep(5)
						self.tampil(satu, nam)
					break

			print(f"Pesanan No {de} Tidak ada")
			sleep(5)
			self.tampil(satu, nam)
		elif pul == "C" or pul == "c":
			self.data(satu, nam)
		else:
			exit("Pilihan tidak ada..")


if __name__ == '__main__':
	try:
		Sewa()
	except KeyboardInterrupt:
		exit("[*] Oke Terima Kasih")
