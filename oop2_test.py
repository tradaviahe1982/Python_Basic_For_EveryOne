from oop2 import CellPhone
def main():
    man = input("Nhập hãng sản xuất: ")
    mod = input("Nhập mã sản phẩm: ")
    retail = float(input("Nhập giá sản phẩm: "))
    #
    phone = CellPhone(man, mod, retail)
    #
    print("Hãng sản xuất là: ", phone.get_manufact())
    print("Mã sản phẩm là: ", phone.get_model())
    print("Giá sản phẩm là: ", phone.get_retail_price())

main()