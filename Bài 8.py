class Date:
    def __init__(self, day=1, month=1, year=2024):
        self.day = day
        self.month = month
        self.year = year
        self._validate()

    def _validate(self):
        # Kiểm tra tính hợp lệ của ngày, tháng, năm
        if not (1 <= self.month <= 12):
            raise ValueError("Tháng không hợp lệ")
        
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self._is_leap_year():
            days_in_month[1] = 29
        
        if not (1 <= self.day <= days_in_month[self.month - 1]):
            raise ValueError("Ngày không hợp lệ")

    def _is_leap_year(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    def display(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

class Employee:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao_cong_ty):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cong_ty = ngay_vao_cong_ty

    def display(self):
        return f"Họ tên: {self.ho_ten}\nNgày sinh: {self.ngay_sinh.display()}\nNgày vào công ty: {self.ngay_vao_cong_ty.display()}"

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def them_nhan_vien(self, nhan_vien):
        self.employees.append(nhan_vien)
        print(f"Đã thêm nhân viên: {nhan_vien.ho_ten}")

    def hien_thi_danh_sach(self):
        if not self.employees:
            print("Danh sách nhân viên trống.")
        else:
            print("Danh sách nhân viên:")
            for i, emp in enumerate(self.employees, 1):
                print(f"\nNhân viên {i}:")
                print(emp.display())

    def tim_kiem_nhan_vien(self, ten):
        ket_qua = [emp for emp in self.employees if ten.lower() in emp.ho_ten.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} nhân viên:")
            for emp in ket_qua:
                print(emp.display())
                print()
        else:
            print("Không tìm thấy nhân viên.")

# Chương trình chính
if __name__ == "__main__":
    quan_ly = EmployeeManagement()

    while True:
        print("\n--- QUẢN LÝ NHÂN VIÊN ---")
        print("1. Thêm nhân viên")
        print("2. Hiển thị danh sách nhân viên")
        print("3. Tìm kiếm nhân viên")
        print("4. Thoát")

        lua_chon = input("Chọn chức năng (1-4): ")

        if lua_chon == '1':
            ho_ten = input("Nhập họ tên nhân viên: ")
            ns_day, ns_month, ns_year = map(int, input("Nhập ngày sinh (dd mm yyyy): ").split())
            vc_day, vc_month, vc_year = map(int, input("Nhập ngày vào công ty (dd mm yyyy): ").split())
            
            try:
                ngay_sinh = Date(ns_day, ns_month, ns_year)
                ngay_vao_cong_ty = Date(vc_day, vc_month, vc_year)
                nhan_vien = Employee(ho_ten, ngay_sinh, ngay_vao_cong_ty)
                quan_ly.them_nhan_vien(nhan_vien)
            except ValueError as e:
                print(f"Lỗi: {e}")

        elif lua_chon == '2':
            quan_ly.hien_thi_danh_sach()

        elif lua_chon == '3':
            ten = input("Nhập tên nhân viên cần tìm: ")
            quan_ly.tim_kiem_nhan_vien(ten)

        elif lua_chon == '4':
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")