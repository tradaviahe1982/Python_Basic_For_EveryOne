decimal = int(input("Nhập số thập phân: "))
if (decimal == 0):
    print(decimal)
else:
    print("Thương_Số Phần_Còn_Lại Số_Nhị_Phân")
    bitString = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bitString = str(remainder) + bitString
        print("%5d%8d%12s" % (decimal, remainder, bitString))
print("Chuỗi nhị phân là: ", bitString)