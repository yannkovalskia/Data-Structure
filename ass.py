class CircullarQueueBank:
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
            print("Antrian penuh")
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
            print(f"Data nasabah dengan nama: {data['nama']}, berhasil ditambahkan ke antrian")
    def dequeue(self):
        if self.isempty():
            print("Antrian kosong")
        else:
            data = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.max_size
            print(f"Data nasabah dengan nama: {data['nama']}, telah dilayani dan dihapus dari antrian")
            return data
    def display(self):
        if self.isempty():
            print("Antrian kosong")
        else:
            print("Daftar Antrian Nasabah:")
            i = self.front
            while True:
                nasabah = self.queue[i]
                print(f"Nama: {nasabah['nama']}, Nomor Rekening: {nasabah['nomor_rekening']}")
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size

nasabah_queue = CircullarQueueBank(2)
while True:
    print(f"\nMenu Layanan Bank:")
    print("1. Tambah Antrian")
    print("2. Layani Antrian")
    print("3. Tampilkan Antrian")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")
    if pilihan == '1':
        nama = input("Masukkan nama nasabah: ")
        nomor_rekening = input("Masukkan nomor rekening: ")
        nasabah = {'nama': nama, 'nomor_rekening': nomor_rekening}
        nasabah_queue.enqueue(nasabah)
    elif pilihan == '2':
        nasabah_queue.dequeue()
        print("Nasabah telah dilayani")
    elif pilihan == '3':
        nasabah_queue.display()
    elif pilihan == '4':
        print("Terima kasih")
        break
    else:
        print("Pilihan tidak valdi")