def exp():
    x = int(input("Enter your number:  "))
    output = 0
    n = 1
    for i in range(0,1000):
        if i != 0:
            n *= i
        output += ((x**i)/n)
        
    return (output)

print(exp())