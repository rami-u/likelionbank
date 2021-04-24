from Account import Account
from Actions.Actions import create_account

account_list = []  


def show_menu():
    print("===== Bank Menu =====")
    print("1. 계좌 개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체 조회")
    print("5. 계좌 번호 변경")
    print("6. 종료하기")
    print("======================")



while 1:
    show_menu()
    menu = int(input())
    if menu == 1:
        account_number, name, deposit = create_account()
        account = Account(account_number, name, deposit)
        account_list.append(account)
        print("##계좌개설을 완료하였습니다##")
        continue
    elif menu == 2:
        account_number = int(input("입금하실 계좌번호를 입력해주세요: "))
        for account in account_list:
            if account.account_number == account_number:
                print("계좌번호: ", account.account_number, end="")
                print(" / 이름 : ", account.name, end="")
                print(" / 잔액 : ", account.balance)
                
                balance = int(input("입금하실 금액을 입력해주세요: "))
                if balance>0:
                    account.balance += balance
                    print("계좌번호: ", account.account_number, end="")
                    print(" / 이름 : ", account.name, end="")
                    print(" / 잔액 : ", account.balance)
                else:
                    print("다시 입력하세요")
            else:
                print("계좌를 잘못 입력하셨습니다.")
        continue
    elif menu == 3:
        account_number = int(input("출금하실 계좌번호를 입력해주세요: "))
        for account in account_list:
            if account.account_number == account_number:
                print("계좌번호: ", account.account_number, end="")
                print(" / 이름 : ", account.name, end="")
                print(" / 잔액 : ", account.balance)
                
                balance = int(input("출금하실 금액을 입력해주세요: "))
                if balance > account.balance:
                    print("잔액이 부족합니다.")
                    print("계좌번호: ", account.account_number, end="")
                    print(" / 이름 : ", account.name, end="")
                    print(" / 잔액 : ", account.balance)
                elif balance<0:
                    print("다시 입력하세요")
                else:
                    account.balance -= balance
                    print("계좌번호: ", account.account_number, end="")
                    print(" / 이름 : ", account.name, end="")
                    print(" / 잔액 : ", account.balance)
            else:
                print("잘못 입력하셨습니다.")
        continue
    elif menu == 4:
        for account in account_list:
            print("계좌번호: ", account.account_number, end="")
            print(" / 이름 : ", account.name, end="")
            print(" / 잔액 : ", account.balance)
        continue
    elif menu == 5:
        account_number = int(input("변경할 계좌번호를 입력해주세요: "))
        for account in account_list:
            if account.account_number == account_number:
               a =int(input("변경하고 싶은 계좌번호를 입력해주세요:"))
               account.account_number = a
            else:
                print("계좌번호가 없습니다.")
        continue
    elif menu == 6:
        exit()
