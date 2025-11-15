class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None
def balik_kalimat(kalimat):
    s = Stack()
    for huruf in kalimat:
        s.push(huruf)
    hasil = ""
    while len(s.items) > 0:
        hasil += s.pop()
    return hasil
kalimat = "Saya beli mobil"
print("Kalimat asli :", kalimat)
print("Kalimat terbalik :", balik_kalimat(kalimat))
