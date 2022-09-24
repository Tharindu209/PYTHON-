number = [23,21,33,53,67,2,36,8,22,97,200]

def selection(arr):
    n = len(arr) 
    for i in range(n):
        point = i
        for j in range(i+1,n):
            if arr[point] > arr[j]:
                point = j
        arr[i],arr[point] = arr[point],arr[i]        
    return arr

def main():
    return selection(number)

main()