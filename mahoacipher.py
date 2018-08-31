text = input("Nhập chuỗi để mã hóa: ")
distance = int(input("Nhập khoảng cách giá trị: "))
code = ""
for ch in text:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                      (ord('z') - ordValue + 1)
    code += chr(cipherValue)
print(code)

