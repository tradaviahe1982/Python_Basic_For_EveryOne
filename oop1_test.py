from oop1 import BankAccount
def main():
    start_bal = float(input("Nhập tài khoản bắt đầu của bạn: "))
    #tạo đối tượng bank account
    savings = BankAccount(start_bal)
    #rút tiền
    pay = float(input("Bạn thực hiện gửi vào tài khoản số tiền: "))
    savings.deposit(pay)
    ###
    cash = float(input("Bạn thực hiện rút tiền trong tài khoản với số tiền: "))
    savings.withdraw(cash)
    ###
    print("Số tiền còn lại trong tài khoản bạn là: ", savings.get_balance())

main()

