def find_inv_sqrt():
    n = float(input("Enter the number for find the inverse of square root: "))
    x = 1
    output = 0
    for _ in range(20):
        x = ((3 - (n*(x**2)))*x)/2
        
    print("your output is: ",x)

find_inv_sqrt()