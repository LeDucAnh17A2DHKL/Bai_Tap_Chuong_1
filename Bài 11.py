import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def tinh_chu_vi(self):
        return self.a + self.b + self.c
    
    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        c = math.sqrt(a**2 + b**2)
        super().__init__(a, b, c)

class TamGiacCan(TamGiac):
    def __init__(self, day, canh_ben):
        super().__init__(day, canh_ben, canh_ben)

class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)

def main():
    print("Chọn loại tam giác:")
    print("1. Tam giác thường")
    print("2. Tam giác vuông")
    print("3. Tam giác cân")
    print("4. Tam giác đều")
    
    lua_chon = int(input("Nhập lựa chọn của bạn (1-4): "))
    
    if lua_chon == 1:
        a = float(input("Nhập cạnh a: "))
        b = float(input("Nhập cạnh b: "))
        c = float(input("Nhập cạnh c: "))
        tam_giac = TamGiac(a, b, c)
    elif lua_chon == 2:
        a = float(input("Nhập cạnh góc vuông a: "))
        b = float(input("Nhập cạnh góc vuông b: "))
        tam_giac = TamGiacVuong(a, b)
    elif lua_chon == 3:
        day = float(input("Nhập độ dài đáy: "))
        canh_ben = float(input("Nhập độ dài cạnh bên: "))
        tam_giac = TamGiacCan(day, canh_ben)
    elif lua_chon == 4:
        canh = float(input("Nhập độ dài cạnh: "))
        tam_giac = TamGiacDeu(canh)
    else:
        print("Lựa chọn không hợp lệ")
        return
    
    print(f"Chu vi: {tam_giac.tinh_chu_vi():.2f}")
    print(f"Diện tích: {tam_giac.tinh_dien_tich():.2f}")

if __name__ == "__main__":
    main()