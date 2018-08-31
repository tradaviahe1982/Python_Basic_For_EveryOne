import math
area = float(input("Nhập diện tích: "))
if area > 0:
    radius = area / math.pi
    print("Bán kính là: ", radius)
else:
    print("Lỗi, diện tích phải là số")