import sys

def isprime(number):  
    count,i = 0,2  
    while i <= number//2:
        if number%i== 0:
            count+=1 
            break
        i+=1
    if count == 0 and number !=1:
        return number
    else:
        return 0
    

def sieve_of_eratosthenes(number):
    l = []
    for i in range(number+1):
        l.append(i)
    p = 2
    l[1] = 0
    while p*p <= number:
        i = p*p
        while i <= number:
            l[i] = 0
            i+=p
        p+=1
    print(sum(l))
    
    
    
