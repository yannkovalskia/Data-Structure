class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    def clear(self):
        self.items.clear()
    def __str__(self):
        return str(self.items)

buku = Stack()
daftar_buku = [
    "Pemrograman Berorientasi Objek",
    "Pemrograman Visual",
    "Multimedia",
    "Sistem Basis Data",
    "Struktur Data",
    "Jaringan Komputer"
]

for b in daftar_buku:
    buku.push(b)
buku_dipinjam = ["Multimedia", "Struktur Data"]
temp = Stack()
pinjam = Stack()
while not buku.isEmpty():
    top = buku.pop()
    if top in buku_dipinjam:
        pinjam.push(top)
    else:
        temp.push(top)
while not temp.isEmpty():
    buku.push(temp.pop())
print("Buku tersisa di perpustakaan:", buku)
print("Buku yang dipinjam:", pinjam)
