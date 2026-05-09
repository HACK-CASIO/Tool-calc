# Tinh the tich hinh hoc - lop 9

import math

menu = ["1: hinh tru", "2: hinh non", "3: hinh cau"]

def the_tich_tru(r, h):
    V = math.pi * r**2 * h
    print(f"Ket qua: {V:.2f} cm³.")

def the_tich_non(r, h):
    V = (1/3) * math.pi * r**2 * h
    print(f"Ket qua: {V:.2f} cm³.")

def the_tich_cau(r):
    V = (4/3) * math.pi * r**3
    print(f"Ket qua: {V:.2f} cm³.")

while True:
    print("\nChon tinh toan voi hinh hoc")

    for i in menu:
        print(i)

    chon = int(input("Chon: "))

    if chon == 1:
        print("hinh tru")
        r = int(input("r (cm): "))
        h = int(input("h (cm): "))
        the_tich_tru(r, h)

    elif chon == 2:
        print("hinh non")
        r = int(input("r (cm): "))
        h = int(input("h (cm): "))
        the_tich_non(r, h)

    elif chon == 3:
        print("hinh cau")
        r = int(input("r (cm): "))
        the_tich_cau(r)

    else:
        print("Thu lai")
