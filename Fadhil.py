# Praktek Ke-3
# Membuat sebuah sistem restoran sederhana menggunakan OOP
# Interaksi antar objek
class MenuItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    
    def __str__(self):
        return f"{self.nama} - ${self.harga:.2f}"
    
class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.pesanan = []
        
    def pesan(self, menu_item):
        self.pesanan.append(menu_item)
        print(f"{self.nama} memesan {menu_item}")
    
    def bayar(self):
        total = sum(item.harga for item in self.pesanan)
        return total
    
class Pelayan:
    def __init__(self, nama):
        self.nama = nama
        
    def ambil_pesanan(self, pelanggan):
        print(f"{self.nama} mengantarkan pesanan dari {pelanggan.nama}")
        
    def antar_pesanan(self, pelanggan):
        total = pelanggan.bayar()
        print(f"{self.nama} mengantarkan pesanan kepada {pelanggan.nama}")
        print(f"Total Tagihan: ${total:.2f}")
        
class Dapur:
    def __init__(self):
        self.menu = {
            "AyamGeprek": MenuItem("AyamGeprek", 15.000),
            "MieAyam": MenuItem("MieAyam", 15.000),
            "NasiGoreng": MenuItem("NasiGoreng", 15.000),
        }
        
    def siapkan_pesanan(self, pesanan):
        for item in pesanan:
            if item.nama in self.menu:
                print(f"Menyediakan {item} dengan harga ${item.harga:.2f}")
            else: 
                print(f"{item.nama} Tidak ada dalam menu")
                
Pelanggan = Pelanggan("RisqiJawa")
Pelayan = Pelayan("NandaCina")
Dapur = Dapur()

AyamGeprek = MenuItem("AyamGeprek", 15.000)
MieAyam = MenuItem("MieAyam", 15.000)
NasiGoreng = MenuItem("NasiGoreng", 15.000)

Pelanggan.pesan(NasiGoreng)
Pelanggan.pesan(AyamGeprek)

Pelayan.ambil_pesanan(Pelanggan)
Dapur.siapkan_pesanan(Pelanggan.pesanan)

Pelayan.antar_pesanan(Pelanggan)