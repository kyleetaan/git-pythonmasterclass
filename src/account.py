import datetime
import pytz

class Account(object):
    """ Simple account class with balance """
    
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_list.append((Account._current_time(), amount))
            self.__show_balance()

    def witdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than zero and no more than your account balance.")
        self.__show_balance()
        self.transaction_list.append((Account._current_time(), -amount))
        
    def __show_balance(self):
        print("Balance is {}".format(self.balance))


    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == "__main__":
    macmac = Account("macmac", 100)
    macmac.deposit(500)
    macmac.witdraw(200)
    print(macmac.transaction_list)
    macmac.show_transactions()