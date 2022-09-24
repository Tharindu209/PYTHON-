def find_sqrt():
    n = int(input("Enter the number for find the square root: "))
    x = 1
    output = 0
    for _ in range(10):
        x = (x +(n/x))/2
        
    print("your output is: ",x)

find_sqrt()