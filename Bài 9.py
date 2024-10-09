import math

class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh
    
    def tinh_chu_vi(self):
        pass
    
    def tinh_dien_tich(self):
        pass

class HinhBinhHanh(DaGiac):
    def __init__(self, canh_day, canh_ben, chieu_cao):
        super().__init__(4)
        self.canh_day = canh_day
        self.canh_ben = canh_ben
        self.chieu_cao = chieu_cao
    
    def tinh_chu_vi(self):
        return 2 * (self.canh_day + self.canh_ben)
    
    def tinh_dien_tich(self):
        return self.canh_day * self.chieu_cao

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong, chieu_rong)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh
    
    def tinh_chu_vi(self):
        return 4 * self.canh
    
    def tinh_dien_tich(self):
        return self.canh ** 2

# Hàm nhập dữ liệu và tính toán
def main():
    print("Chọn hình muốn tính:")
    print("1. Hình bình hành")
    print("2. Hình chữ nhật")
    print("3. Hình vuông")
    
    lua_chon = int(input("Nhập lựa chọn của bạn (1-3): "))
    
    if lua_chon == 1:
        canh_day = float(input("Nhập cạnh đáy: "))
        canh_ben = float(input("Nhập cạnh bên: "))
        chieu_cao = float(input("Nhập chiều cao: "))
        hinh = HinhBinhHanh(canh_day, canh_ben, chieu_cao)
    elif lua_chon == 2:
        chieu_dai = float(input("Nhập chiều dài: "))
        chieu_rong = float(input("Nhập chiều rộng: "))
        hinh = HinhChuNhat(chieu_dai, chieu_rong)
    elif lua_chon == 3:
        canh = float(input("Nhập độ dài cạnh: "))
        hinh = HinhVuong(canh)
    else:
        print("Lựa chọn không hợp lệ")
        return
    
    print(f"Chu vi: {hinh.tinh_chu_vi()}")
    print(f"Diện tích: {hinh.tinh_dien_tich()}")

if __name__ == "__main__":
    main()