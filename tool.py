# Tinh dien tich hinh chu nhat

menu = ["1: chu_vi", "2: dien_tich"]

def chu_vi(a, b):
    tinh_toan = 2 * (a + b)
    print(f"Ket qua: {tinh_toan} cm.")

def dien_tich(a, b):
    tinh_toan = a * b
    print(f"Ket qua: {tinh_toan} cm².")

while True:
    print("Chon tinh toan voi hinh chu nhat")    
    for i in menu:
        print(i)

    chon = int(input("Chon: "))

    if chon == 1:
        print("Chu vi")
        a = int(input("Chieu dai (cm): "))
        b = int(input("Chieu rong (cm): "))
        chu_vi(a, b)

    elif chon == 2:
        print("Dien tich")
        a = int(input("Chieu dai (cm): "))
        b = int(input("Chieu rong (cm): "))
        dien_tich(a, b)

    else:
        print("Thu lai")
