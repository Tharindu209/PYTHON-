def find_duplicate(x):
    tortoise = x[0]
    hare = x[0]
    while True:
        tortoise = x[tortoise]
        print(tortoise,end = "\t")
        hare = x[x[hare]]
        print(hare)
        if tortoise == hare:
            break
        
    ptr1 = x[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = x[ptr1]
        ptr2 = x[ptr2]
    
    return ptr2

print(find_duplicate([3,4,2,1,4,6,7]))