class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = []

    def push(self, item):
        if not self.isFull():
            self.stack.append(float(item))
        else:
            raise Exception("Stack overflow")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise Exception("Stack underflow")

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity

    def count(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

# Sử dụng lớp Stack đã cập nhật
if __name__ == "__main__":
    s = Stack(5)  # Tạo một Stack với dung lượng 5 phần tử

    # Thêm phần tử vào Stack và kiểm tra số lượng
    print("Thêm các phần tử vào Stack:")
    for i in range(3):
        s.push(i + 0.5)
        print(f"Đã thêm {i + 0.5}, Số phần tử hiện tại: {s.count()}, Stack: {s}")

    # Kiểm tra số lượng phần tử
    print(f"\nSố phần tử trong Stack: {s.count()}")

    # Lấy phần tử ra khỏi Stack và kiểm tra số lượng
    print("\nLấy các phần tử ra khỏi Stack:")
    while not s.isEmpty():
        print(f"Phần tử được lấy ra: {s.pop()}, Số phần tử còn lại: {s.count()}, Stack: {s}")

    # Kiểm tra Stack trống
    print(f"\nStack đã trống, số phần tử: {s.count()}")