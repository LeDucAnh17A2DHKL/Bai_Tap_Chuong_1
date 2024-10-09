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

    def __str__(self):
        return str(self.stack)

# Sử dụng lớp Stack
if __name__ == "__main__":
    s = Stack(5)  # Tạo một Stack với dung lượng 5 phần tử

    # Thêm phần tử vào Stack
    print("Thêm các phần tử vào Stack:")
    for i in range(5):
        s.push(i + 0.5)
        print(f"Đã thêm {i + 0.5}, Stack hiện tại: {s}")

    # Kiểm tra Stack đã đầy chưa
    print(f"\nStack đã đầy chưa? {s.isFull()}")

    # Lấy phần tử ra khỏi Stack
    print("\nLấy các phần tử ra khỏi Stack:")
    while not s.isEmpty():
        print(f"Phần tử được lấy ra: {s.pop()}, Stack còn lại: {s}")

    # Kiểm tra Stack đã trống chưa
    print(f"\nStack đã trống chưa? {s.isEmpty()}")

    # Thử lấy phần tử từ Stack rỗng
    try:
        s.pop()
    except Exception as e:
        print(f"\nLỗi: {e}")

    # Thử thêm phần tử vào Stack đầy
    s = Stack(1)
    s.push(1.0)
    try:
        s.push(2.0)
    except Exception as e:
        print(f"\nLỗi: {e}")