number = [23,21,33,53,67,2,36,8,22,97,200]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pilot = arr[0]
    left = []
    right = []
    for i in range(1,len(arr)):
        if arr[i] < pilot:
            left.append(arr[i])
        else:
            right.append(arr[i])
            
    return quicksort(left)+[pilot]+quicksort(right)

if __name__ == '__main__':
    print(quicksort(number))