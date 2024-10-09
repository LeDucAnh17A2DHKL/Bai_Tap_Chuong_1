import math

class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Elip:
    def __init__(self, tam, ban_truc_lon, ban_truc_nho):
        self.tam = tam
        self.ban_truc_lon = ban_truc_lon
        self.ban_truc_nho = ban_truc_nho
    
    def tinh_dien_tich(self):
        return math.pi * self.ban_truc_lon * self.ban_truc_nho

class DuongTron(Elip):
    def __init__(self, tam, ban_kinh):
        super().__init__(tam, ban_kinh, ban_kinh)
        self.ban_kinh = ban_kinh
    
    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2

def main():
    print("Nhập tọa độ tâm:")
    x = float(input("x = "))
    y = float(input("y = "))
    tam = Diem(x, y)

    print("\nChọn hình muốn tính:")
    print("1. Elip")
    print("2. Đường tròn")
    
    lua_chon = int(input("Nhập lựa chọn của bạn (1-2): "))
    
    if lua_chon == 1:
        ban_truc_lon = float(input("Nhập độ dài bán trục lớn: "))
        ban_truc_nho = float(input("Nhập độ dài bán trục nhỏ: "))
        hinh = Elip(tam, ban_truc_lon, ban_truc_nho)
    elif lua_chon == 2:
        ban_kinh = float(input("Nhập bán kính: "))
        hinh = DuongTron(tam, ban_kinh)
    else:
        print("Lựa chọn không hợp lệ")
        return
    
    print(f"Diện tích: {hinh.tinh_dien_tich():.2f}")

if __name__ == "__main__":
    main()