# create bankaccount class
class bank:
    
    # initial state(constructor)
    def __init__(self,balance):
        self.__balance = balance
        self.amount = 0
        
    # function of get the value of deposite or withdrawal
    def value(self,amount):
        self.amount = amount
    
    # calculate balance
    def calculate(self,state):
        if  state == 'd':
            self.__balance += self.amount
        else:
            self.__balance -= self.amount
    
    # mutators for the class's data attributes
    def set_value(self,balance):
        self.balance = balance
    
    # accessors for the class's data attributes
    def get_balance(self):
        return self.__balance
    
    # deconstructor
    def __str__(self):
        return f'your balance is: {self.__balance}'
    
