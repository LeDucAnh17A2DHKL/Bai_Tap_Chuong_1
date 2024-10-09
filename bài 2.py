class ThiSinh:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

class QuanLyThiSinh:
    def __init__(self):
        self.danh_sach_thi_sinh = []

    def nhap_thong_tin(self):
        ho_ten = input("Nhập họ tên thí sinh: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hóa: "))
        thi_sinh = ThiSinh(ho_ten, diem_toan, diem_ly, diem_hoa)
        self.danh_sach_thi_sinh.append(thi_sinh)

    def in_danh_sach(self):
        for thi_sinh in self.danh_sach_thi_sinh:
            print(f"{thi_sinh.ho_ten}: Toán {thi_sinh.diem_toan}, Lý {thi_sinh.diem_ly}, Hóa {thi_sinh.diem_hoa}")

    def danh_sach_trung_tuyen(self, diem_chuan):
        danh_sach_trung_tuyen = sorted(
            [ts for ts in self.danh_sach_thi_sinh if ts.tinh_tong_diem() >= diem_chuan],
            key=lambda x: x.tinh_tong_diem(),
            reverse=True
        )
        print("Danh sách thí sinh trúng tuyển:")
        for thi_sinh in danh_sach_trung_tuyen:
            print(f"{thi_sinh.ho_ten}: Tổng điểm {thi_sinh.tinh_tong_diem()}")

# Sử dụng chương trình
quan_ly = QuanLyThiSinh()

# Nhập thông tin thí sinh
so_thi_sinh = int(input("Nhập số lượng thí sinh: "))
for _ in range(so_thi_sinh):
    quan_ly.nhap_thong_tin()

# In danh sách thí sinh
print("\nDanh sách thí sinh:")
quan_ly.in_danh_sach()

# In danh sách trúng tuyển
diem_chuan = 20
quan_ly.danh_sach_trung_tuyen(diem_chuan)