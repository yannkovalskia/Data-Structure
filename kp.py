nilai = [
    [
        ["Vina", [80, 85, 90]],
        ["Rina", [70, 75, 80]],
        ["Rara", [88, 90, 92]]
    ],
    [
        ["Dian", [78, 80, 82]],
        ["Ali", [85, 87, 89]],
        ["Budi", [90, 92, 94]]
    ]
]

for k in range(len(nilai)):
    print(f"kelas {k + 1}:")
    for s in range(len(nilai[k])):
        nama = nilai[k][s][0]
        data_nilai = nilai[k][s][1]
        print(f"{nama} -> {data_nilai}")

print(nilai[0][1][0])
print(nilai[0][1][1][1])


nilai[0].append(["Lina", [95,90,93]])
del nilai[1][1]
dua_mahasiswa = nilai[1][:2]
print(dua_mahasiswa)