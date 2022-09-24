from isprime import isprime,sieve_of_eratosthenes


def main():
    value = int(input("Enter Number: "))
    method = input("enter your method either normal or SOE: ")
    if method == "normal":
            sum = 0
            for i in range(2,value+1):
                sum += isprime(i)
            print(sum)
    elif method ==  "soe":
            sieve_of_eratosthenes(value)
    else:
            print("invalid argument")
    
if __name__ == "__main__":
    main()