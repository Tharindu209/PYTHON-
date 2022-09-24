import acc_class as c

if __name__ == '__main__':
    value = int(input("enter your recent balance: "))
    obj = c.bank(value)
    while True:
        state = input("if deposite enter d ,else enter w as withdrawal: ")
        amount = int(input("enter your value: "))
        if amount <= 0:
            break 
        obj.value(amount)
        obj.calculate(state)
        print(obj.get_balance())
    print(obj)
    
