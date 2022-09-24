number = [23,21,33,53,67,2,36,8,22,97,200]

def heap(number):
    # create max heap
    n = len(number)
    for i in range(n//2,-1,-1):
        heapify(number,n,i)
    # sort
    for i in range(n-1,0,-1):
        # swap
        number[0],number[i] = number[i],number[0]
        heapify(number,i,0)
        
    
def heapify(arr,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[largest] < arr[left]:
        largest = left
    
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        # swap
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,n,largest)
    
def main():
    heap(number)
    return number

print(main())