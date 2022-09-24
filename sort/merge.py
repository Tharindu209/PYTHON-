number = [23,21,33,53,67,2,36,8,22,97,200]

def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge(arr[:mid])
    right = merge(arr[mid:])
    
    sorted = []
    left_index = 0
    rigth_index = 0
    
    while len(right) > rigth_index and len(left) > left_index:
        if left[left_index] < right[rigth_index]:
            sorted.append(left[left_index])
            left_index += 1
        else:
            sorted.append(right[rigth_index])
            rigth_index += 1
    
    sorted += left[left_index:]
    sorted += right[rigth_index:]
    
    return sorted

if __name__ == '__main__':
    print(merge(number))