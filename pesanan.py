class Order:
    def __init__(self, nama, menu):
        self.nama = nama
        self.menu = menu
class OrderQueue:
    def __init__(self):
        self.order = []
        self.front = -1
        self.rear = -1
    def is_empty(self):
        return len(self.order) == 0
    def tambah_order(self, nama_pelanggan, menu):
        self.order.append(Order(nama_pelanggan, menu))
        if self.front == -1:
            self.front = 0
        self.rear += 1
        print(f"Order dari {nama_pelanggan} untuk menu '{menu}' telah ditambahkan.")
    def layani_order(self):
        if self.is_empty():
            print("Tidak ada order untuk dilayani.")
        else:
            order_dilayani = self.order.pop(0)
            print(f"Order dari {order_dilayani.nama} untuk menu '{order_dilayani.menu}' telah dilayani.")
            self.rear -= 1
            if self.is_empty():
                self.front = -1
                self.rear = -1
    def lihat_antrian(self):
        if self.is_empty():
            print("Tidak ada order dalam antrian.")
        else:
            print("Daftar order dalam antrian:")
            for i, order in enumerate(self.order):
                print(f"{i + 1}. {order.nama} - {order.menu}")
    def cari_order(self, nama_pelanggan):
        for order in self.order:
            if order.nama == nama_pelanggan:
                print(f"Order ditemukan: {order.nama} - {order.menu}")
                return
        print(f"Tidak ada order dari {nama_pelanggan} dalam antrian.")

order = OrderQueue()
order.tambah_order("Rayyan", "Nasi Goreng")
order.tambah_order("Alya", "Mie Ayam")
order.tambah_order("Elysia", "Sate Ayam")
order.tambah_order("Agy", "Bakso")
order.tambah_order("Cast", "Soto Ayam")
order.lihat_antrian()
order.layani_order()
order.cari_order("Alya")