class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.__balance = 0
        self.__account_name = ""
        self.account_name = account_name

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        new_name = new_name.strip()

        if new_name == "":
            print("Tên tài khoản không được để trống")
        else:
            self.__account_name = new_name.upper()

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
        else:
            self.__balance += amount
            print(f"Nạp tiền thành công: +{amount:,} VND")
            print(f"Số dư mới: {self.balance:,} VND")

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return

        total = amount + BankAccount.transaction_fee

        if self.__balance < total:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            print(f"Số dư mới: {self.balance:,} VND")
        else:
            self.__balance -= total
            print(f"Rút tiền thành công: -{amount:,} VND")
            print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
            print(f"Số dư mới: {self.balance:,} VND")

    def display_info(self):
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print("Ngân hàng:", BankAccount.bank_name)
        print("Số tài khoản:", self.account_number)
        print("Tên chủ tài khoản:", self.account_name)
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
        

def open_account():
    print("\n--- MỞ TÀI KHOẢN MỚI ---")

    while True:
        account_number = input("Nhập số tài khoản 10 chữ số: ")

        if BankAccount.validate_account_number(account_number):
            break

        print("Số tài khoản không hợp lệ!")
        print("Số tài khoản phải gồm đúng 10 chữ số.")

    account_name = input("Nhập tên chủ tài khoản: ")

    account = BankAccount(account_number, account_name)

    print("Mở tài khoản thành công!")
    print("Số tài khoản:", account.account_number)
    print("Tên chủ tài khoản:", account.account_name)

    return account


def view_account(current_account):
    if current_account is None:
        print("Hệ thống chưa có thông tin tài khoản")
        print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
    else:
        current_account.display_info()


def transaction(current_account):
    if current_account is None:
        print("Hệ thống chưa có thông tin tài khoản")
        print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        return

    print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
    print("1. Nạp tiền")
    print("2. Rút tiền")

    choice = input("Chọn loại giao dịch (1-2): ")

    amount = input("Nhập số tiền giao dịch: ")

    if not amount.isdigit():
        print("Số tiền không hợp lệ")
        return

    amount = int(amount)

    if choice == "1":
        current_account.deposit(amount)

    elif choice == "2":
        current_account.withdraw(amount)

    else:
        print("Lựa chọn không hợp lệ")
        
def update_name(current_account):
    if current_account is None:
        print("Hệ thống chưa có thông tin tài khoản")
        print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        return

    print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")

    old_name = current_account.account_name

    new_name = input("Nhập tên mới: ")
    current_account.account_name = new_name

    if current_account.account_name != old_name:
        print("Cập nhật thành công. Tên mới:", current_account.account_name)


def update_fee():
    print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
    print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")

    new_fee = input("Nhập phí giao dịch mới: ")

    if not new_fee.isdigit():
        print("Phí giao dịch không hợp lệ")
        return

    new_fee = int(new_fee)

    if new_fee < 0:
        print("Phí giao dịch không được âm")
        print(f"Phí giao dịch hiện tại vẫn là {BankAccount.transaction_fee:,} VND")
    else:
        BankAccount.update_transaction_fee(new_fee)
        print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {BankAccount.transaction_fee:,} VND")

def main():
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Giao dịch Nạp / Rút tiền")
        print("4. Cập nhật Tên chủ tài khoản")
        print("5. Đổi phí giao dịch hệ thống")
        print("6. Thoát chương trình")
        print("==========================================")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            current_account = open_account()

        elif choice == "2":
            view_account(current_account)

        elif choice == "3":
            transaction(current_account)

        elif choice == "4":
            update_name(current_account)

        elif choice == "5":
            update_fee()

        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
            break

        else:
            print("Lựa chọn không hợp lệ")

main()