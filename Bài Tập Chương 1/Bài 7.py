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

    def next(self):
        day = self.day + 1
        month = self.month
        year = self.year

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self._is_leap_year():
            days_in_month[1] = 29

        if day > days_in_month[month - 1]:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1

        return Date(day, month, year)

# Sử dụng lớp Date
if __name__ == "__main__":
    # Tạo một đối tượng Date với giá trị mặc định
    date1 = Date()
    print("Ngày mặc định:", date1.display())

    # Tạo một đối tượng Date với giá trị cụ thể
    date2 = Date(31, 12, 2023)
    print("Ngày cụ thể:", date2.display())

    # Sử dụng phương thức next để tính ngày tiếp theo
    next_date = date2.next()
    print("Ngày tiếp theo:", next_date.display())

    # Kiểm tra năm nhuận
    leap_year_date = Date(29, 2, 2024)
    print("Ngày trong năm nhuận:", leap_year_date.display())
    print("Ngày tiếp theo sau năm nhuận:", leap_year_date.next().display())

    # Kiểm tra xử lý lỗi
    try:
        invalid_date = Date(31, 4, 2024)
    except ValueError as e:
        print("Lỗi:", e)