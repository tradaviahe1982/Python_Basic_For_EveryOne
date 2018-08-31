f = open("songuyen.txt", "r")
theSum = 0
for line in f:
    line = line.strip()
    number = int(line)
    theSum += number
print("Tổng 500 số ngẫu nhiên trong khoảng [1, 100] đọc từ file là: ", theSum)
