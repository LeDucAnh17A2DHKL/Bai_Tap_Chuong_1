class hinh_chu_nhat:
    def __init__(self,dài, rộng):
        self.dài= dài
        self.rộng= rộng

     #tính chu vi
    def chuvi(self):
        return 2*(self.dài + self.rộng)

     #tính diện tích
    def dientich(self):
        return (self.dài * self.rộng)

    def hien_thi(self):
        print(f"Chiều dài: {self.dài}")
        print(f"Chiều rộng: {self.rộng}")
        print(f"Chu vi: {self.chuvi()}")
        print(f"Diện tích: {self.dientich()}")

if __name__ == "__main__":
    # Nhập chiều rộng và chiều dài của hình chữ nhật
    rộng = float(input("Nhập chiều rộng của hình chữ nhật: "))
    dài = float(input("Nhập chiều dài của hình chữ nhật: "))

    Chu_nhat = hinh_chu_nhat(rộng, dài)

    Chu_nhat.hien_thi()