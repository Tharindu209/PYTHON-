# x = [0]*501
# x[1] = 1
# for i in range(2,len(x)):
    # x[i] = x[i-1]+x[i-2]

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
 
# for i in range(len(x)):
# ``  print(f"{i} ",x[i])
    
print(fib(5))