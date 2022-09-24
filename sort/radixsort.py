number = [23,21,33,53,67,2,36,8,22,97,200]

def group(arr,exp):
    n = len(arr)
    output = [0]*(n)
    count = [0]*(10)
    
    for i in range(n):
        index = int(arr[i]/exp)
        count[index%10] +=1
        
    for i in range(1,10):
        count[i] += count[i-1]
    
    for i in range(n-1,-1,-1):
        index = int(arr[i]/exp)
        output[count[index%10]-1] = arr[i]
        count[index%10] -= 1
    for i in range(n):
        arr[i] = output[i]
        

def radix(arr):
    large = max(arr)
    exp = 1
    while large/exp > 0:
        group(arr,exp)
        exp *= 10 
    return arr

if __name__ == '__main__':       
    print(radix(number))