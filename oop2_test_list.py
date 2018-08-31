from oop2 import CellPhone
def main():
    phones = make_list()
    display_list(phones)
#
def make_list():
    phone_list = []
    print ("Nhập dữ liệu cho 5 CellPhone!")
    for count in range(1, 6):
        man = input("Nhập hãng sản xuất: ")
        mod = input("Nhập mã sản phẩm: ")
        retail = float(input("Nhập giá sản phẩm: "))
        print()
        phone = CellPhone(man, mod, retail)
        #
        phone_list.append(phone)
        #
    return phone_list
#
def display_list(list_phone):
    for item in list_phone:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()
#
main()
