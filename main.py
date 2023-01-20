from Account import Account
from BankAccount import BankAccount

def chooseAcc():
    global accounts
    choose = 0
    while choose != -1:
        print('\n0. Exit')
        for i in range(len(accounts)):
            print(f'{i+1}: {accounts[i]}')
        choose = int(input('\nYour choise: ')) - 1
        print(choose)
        if choose >= len(accounts) | choose < -1:
            print('Please write an appropriate number!!!\n')
        elif choose != -1:
            choose2 = -1
            while choose2 != 0:
                print('\n0. Exit')
                print('1. Add to BankAccout')
                print('2. Get money from bank account')
                print('3. Convert the money')
                choose2 = int(input('\nYour choise: '))
                if choose2 == 1:
                    accounts[choose].addToBankAccount()
                elif choose2 == 2:
                    accounts[choose].subtractFromBankAccount()
                elif choose2 == 3:
                    accounts[choose].moneyConversion()
                elif choose2 != 0:
                    print('Please write an appropriate number!!!\n')







choose  = -1
accounts = []
while choose != 0:
    print('\nYour actions:')
    print('0. Exit')
    print('1. Create account')
    print('2. Choose an Account')
    choose = int(input('\n\nYour choise: '))
    if choose == 1:
        accounts.append(BankAccount())
    elif choose == 2:
        chooseAcc()





