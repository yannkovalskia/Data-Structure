class CircullarQueue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size
        self.front = -1
        self.rear = -1
    def isempty(self):
        return self.front == -1
    def isfull(self):
        return (self.rear + 1) % self.max_size == self.front
    def enqueue(self, data):
        if self.isfull():
            print("Antrian penuh!")
        else:
            if self.isempty():
                self.front = 0
                self.rear = 0
                self.queue = [data]
            else:
                self.rear = (self.rear + 1) % self.max_size
                if len(self.queue) < self.max_size:
                    self.queue.append(data)
                else:
                    self.queue[self.rear] = data
            print(f"Data pasien dengan nama: {data['nama']}, berhasil ditambahkan ke antrian.")
            print(f"Front: {self.front}, Rear: {self.rear}")
    def dequeue(self):
        if self.isempty():
            print("Antrian kosong!")
        else:
            data = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.max_size
            print(f"Data pasien {data['nama']} berhasil dihapus dari antrian.")
            print(f"Front: {self.front}, Rear: {self.rear}")
    def display(self):
        if self.isempty():
            print("Antrian kosong!")
        else:
            print("\nAntrian pasien rumah sakit")
            i = self.front
            while True:
                data = self.queue[i]
                print(f"Nama Pasien: {data['nama']}", f"Umur: {data['umur']}", f"Keluhan: {data['penyakit']}")
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size
            print(f"Front: {self.front}, Rear: {self.rear}")
    def cari(self, nama):
        if self.isempty():
            print("Antrian kosong!")
        else:
            i = self.front
            found = False
            while True:
                data = self.queue[i]
                if data["nama"] == nama:
                    print(f"Data pasien ditemukan: Nama Pasien: {data['nama']}, Umur: {data['umur']}, Keluhan: {data['penyakit']}")
                    found = True
                    break
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size
            if not found:
                print(f"Data pasien dengan nama {nama} tidak ditemukan dalam antrian.")

rs = CircullarQueue(4)
while True:
    print("\n=== Pendaftaran Pasien Rumah Sakit ===")
    nama = input("Masukkan nama pasien: ")
    if nama == "":
        break
    umur = input("Masukkan umur pasien: ")
    keluhan = input("Masukkan keluhan pasien: ")
    pasien = {"nama": nama, "umur": umur, "penyakit": keluhan}
    rs.enqueue(pasien)

rs.display()
cari_nama = input("\nCari pasien berdasarkan nama: ")
rs.cari(cari_nama)
rs.dequeue()
rs.display()
