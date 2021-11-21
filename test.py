from descr_commision import Value

class Account():
    amount = Value()

    def __init__(self, comission):
        self.comission = comission

if __name__=='__main__':
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)