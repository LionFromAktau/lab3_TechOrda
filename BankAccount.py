from Account import Account
class BankAccount:
    _name: str
    _surname: str
    _account = Account
    _curs = 0
    _pocket = 0
    _curses = ['USD', 'RUB', 'KZT', 'EUR']
    # def __int__(self, name: str, surname: str):
    #     self._name = name
    #     self._surname = surname
    #     print('\nWellcome to our bank')
    #     print(self)
    def __init__(self):
        self._name = input('Please write your name: ')
        self._surname = input('Please write your surname: ')
        print('\nWellcome to our bank\n')
        print(self)
    def getPocket(self) -> int:
        return "{:.2f}".format(self._pocket) + " in " + self._curses[self._curs]
    def addToBankAccount(self):
        money = int(input('Please write an amount: '))
        self._pocket += money
        print('Successfull Added')
    def __repr__(self):
        return f'Owner: {self._name} {self._surname}.\nMoney in pocket: {self.getPocket()}.'
    def subtractFromBankAccount(self):
        print(f'Currently you have {self.getPocket()}')
        money = int(input('Please write an amount: '))
        if money > self._pocket:
            print('Your money in pocket is not enough')
        else:
            self._pocket -= money
            print('Successfully subtracted')
    def __convert(self, newCurs: int):
        money = Account.USD.value
        for j in Account:
            if self._curses[self._curs] == j.name:
                money = j.value
                break
        print(f'\nFrom {self._curses[self._curs]} to {self._curses[newCurs]}')
        self._curs = newCurs
        print(f'\nnew curs money {money[newCurs]}')
        self._pocket = money[newCurs] * self._pocket

    # def getCurs(self) -> str:
    #     return f'Currently the curs in the Bank is {self._curses[self._curs]}'




    def moneyConversion(self):
        choose = -1
        while(choose != 0):
            print('0. Exit')
            print('1. To USD')
            print('2. To RUB')
            print('3. To KZT')
            print('4. To EUR')
            choose = int(input('Your choise: '))
            if choose > 4:
                print('Plese write an appropriate number!!!')
            else:
                self.__convert(choose - 1)
                print('Successfully Converted')
                print(self.getPocket())
                break

