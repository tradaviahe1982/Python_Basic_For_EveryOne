text = input("Nhập chuỗi để giải mã hóa: ")
distance = int(input("Nhập khoảng cách giá trị: "))
code = ""
for ch in text:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
                      (distance - (ord('a') - ordValue - 1))
    code += chr(cipherValue)
print(code)