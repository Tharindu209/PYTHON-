from linked_list import *

if __name__ == '__main__':
    n = Linkedlist()
    while True:
        value = input("enter your value: ")
        if value.isnumeric() == True:
            n.add(value)
            print(n)
        elif value == 'q':
            break
        else:
            continue
    n.insert(10,1)
    n.insert(30,2)
    n.remove(2)
    print(n)