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

    def print(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack contents (bottom to top):")
            for item in self.stack:
                print(f"  {item}")

    def __str__(self):
        return str(self.stack)

# Sử dụng lớp Stack đã cập nhật
if __name__ == "__main__":
    s = Stack(5)  # Tạo một Stack với dung lượng 5 phần tử

    # Thêm phần tử vào Stack và in nội dung
    print("Thêm các phần tử vào Stack:")
    for i in range(3):
        s.push(i + 0.5)
        print(f"Đã thêm {i + 0.5}")
        s.print()
        print()  # Thêm dòng trống để dễ đọc

    # Lấy phần tử ra khỏi Stack và in nội dung
    print("Lấy các phần tử ra khỏi Stack:")
    while not s.isEmpty():
        popped = s.pop()
        print(f"Đã lấy ra: {popped}")
        s.print()
        print()  # Thêm dòng trống để dễ đọc

    # Kiểm tra Stack trống
    print("Kiểm tra Stack trống:")
    s.print()