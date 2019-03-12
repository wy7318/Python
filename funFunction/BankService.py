import datetime
import pytz

class Account:

    @staticmethod
    def _current_time():                        #name start with underscore is non-public
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self.name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_list.append((Account._current_time(), -amount))
            else:
                print("Your balance is {}, please choose other amount".format(self.balance))
            self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {}".format(amount, tran_type, date, date.astimezone()))

#Testing
if __name__ == '__main__':
    tim = Account("Time", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(1000)
    tim.show_transaction()

    Matt = Account("Matt", 800)
    Matt.deposit(100)
    Matt.withdraw(200)
    Matt.show_transaction()
