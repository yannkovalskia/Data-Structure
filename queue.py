class QueueKlinik:
    def __init__(self):
        self.queue = []
        self.max_size = 5
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return len(self.queue) == 0
    def is_full(self):
        return len(self.queue) >= self.max_size
    def enqueue(self, data):
        if self.is_full():
            print("Antrian penuh, tidak dapat menambah data.")
        else:
            if self.is_empty():
                self.front = 0
            self.queue.append(data)
            self.rear += 1
            print(f"'{data}' berhasil ditambahkan ke antrian.")
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada data untuk dihapus.")
        else:
            hapus_data = self.queue.pop(0)
            self.rear -= 1
            if self.is_empty():
                self.front = -1
                self.rear = -1
            print(f"'{hapus_data}' berhasil dihapus dari antrian.")
    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
        else:
            print("Isi antrian saat ini: ", self.queue)
            print(f"Front = {self.queue[self.front]}, Rear = {self.queue[self.rear]}")
Klinik = QueueKlinik()
Klinik.enqueue("Pasien 1")
Klinik.enqueue("Pasien 2")
Klinik.enqueue("Pasien 3")
Klinik.display()
Klinik.dequeue()
Klinik.display()