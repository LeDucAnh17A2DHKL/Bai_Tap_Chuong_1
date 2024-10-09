import math

class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        if mau_so == 0:
            raise ValueError("Mẫu số không thể bằng 0")
        self.mau_so = mau_so
        self.rut_gon()

    def rut_gon(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
        if self.mau_so < 0:
            self.tu_so = -self.tu_so
            self.mau_so = -self.mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        while True:
            try:
                self.tu_so = int(input("Nhập tử số: "))
                self.mau_so = int(input("Nhập mẫu số: "))
                if self.kiem_tra_hop_le():
                    self.rut_gon()
                    break
                else:
                    print("Phân số không hợp lệ. Mẫu số không thể bằng 0.")
            except ValueError:
                print("Vui lòng nhập số nguyên.")

    def in_phan_so(self):
        if self.mau_so == 1:
            return str(self.tu_so)
        elif self.tu_so == 0:
            return "0"
        else:
            return f"{self.tu_so}/{self.mau_so}"

    def __str__(self): #in đối tượng phân số
        return self.in_phan_so()

# Sử dụng lớp PhanSo
if __name__ == "__main__":
    ps = PhanSo()
    print("Nhập phân số:")
    ps.nhap_phan_so()
    print(f"Phân số sau khi rút gọn: {ps}")

    # Kiểm tra tính hợp lệ
    if ps.kiem_tra_hop_le():
        print("Phân số hợp lệ.")
    else:
        print("Phân số không hợp lệ.")