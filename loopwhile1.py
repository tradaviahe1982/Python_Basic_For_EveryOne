theSum = 0.0
data = input("Nhập số hoặc nhập Enter để thoát")
while data != "":
    number = float(data)
    theSum += number
    data = input("Nhập số hoặc nhập Enter để thoát")
print("Tổng là: ", theSum)