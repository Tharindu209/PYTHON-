from math import pi,exp,sqrt,ceil

def factorial(num):
    tau = 2*pi
    output = ( sqrt(tau*num) * ((num / exp(1))**num))
    return output

n = int(input("enter your number: "))
output = ceil(factorial(n))
if output % pow(10,len(str(output))-1) != 0:
    print (output + 10*len(str(output))-1)