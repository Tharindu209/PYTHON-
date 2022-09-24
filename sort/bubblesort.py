number = [23,21,33,53,67,2,36,8,22,97,200]

def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def main():
    return bubble(number)

print(main())
