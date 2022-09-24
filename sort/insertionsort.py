number = [23,21,33,53,67,2,36,8,22,97,200]


def insert(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr

def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            
    return arr

if __name__ == '__main__':
    print(insert(number))
    print(insertion(number))