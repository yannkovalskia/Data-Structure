class Stack_Lifo:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def push(self, item):
        self.items.append(item)
    def search(self, stack, nomor):
        for item in stack.items:
          if item[0] == nomor:
            return item
        return None
    def tampilkan_info(self):
        print("Isi Stack:", self.items)
jadwal_kereta = [
    ["73", "Gumarang", "Pasar Turi", "14:30", "Pasar Senen"],
    ["74", "Gumarang", "Pasar Senen", "14:45", "Pasar Turi"],
    ["75", "Lodaya", "Solo Balapan", "08:30", "Bandung"],
    ["76", "Lodaya", "Bandung", "08:00", "Solo Balapan"],
    ["77", "Lodaya", "Solo Balapan", "20:30", "Bandung"],
    ["78", "Lodaya", "Bandung", "20:00", "Solo Balapan"],
    ["79", "Mutiara Timur", "Gubeng", "09:15", "Banyuwangi"],
    ["80", "Mutiara Timur", "Banyuwangi", "09:00", "Gubeng"],
    ["81", "Mutiara Timur", "Gubeng", "22:35", "Banyuwangi"]
]
from datetime import datetime
def jam_to_dt(jadwal):
    return datetime.strptime(jadwal[3], "%H:%M")
jadwal_kereta_sorted = sorted(jadwal_kereta, key=jam_to_dt, reverse=True)
kereta_stack = Stack_Lifo()
for jadwal in jadwal_kereta_sorted:
    kereta_stack.push(jadwal)

kereta_stack.tampilkan_info()

def cari_kereta_berdasarkan_nomor(stack, nomor):
    for item in stack.items:
        if item[0] == nomor:
            return item
    return None
cari_nomor = "80"
kereta_dicari = kereta_stack.search(kereta_stack, cari_nomor)
if kereta_dicari:
    print(f"Kereta nomor {kereta_dicari[0]} Ditemukan dengan data: Nomor kereta: {kereta_dicari[0]}, Nama: {kereta_dicari[1]}, Asal Stasiun: {kereta_dicari[2]}, Jam Keberangkatan: {kereta_dicari[3]}, Tujuan Akhir: {kereta_dicari[4]}")
else:
    print(f"Kereta nomor {cari_nomor} tidak ada dalam data jadwal.")