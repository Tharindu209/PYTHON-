number = [23,21,33,53,67,2,36,8,200]

def shell(arr):
    gap = len(arr)//2
    while gap > 0:
        before = gap
        after = 0
        while before < len(arr):
            if arr[before] < arr[after]:
                arr[after],arr[before] = arr[before],arr[after]
            before +=1
            after +=1
            
            tmp = after
            while tmp - gap > -1:
                if arr[tmp] < arr[tmp-gap]:
                    arr[tmp],arr[tmp-gap] = arr[tmp-gap],arr[tmp]
                tmp -=1
                       
        gap //= 2
    return arr

if __name__ == '__main__':
    print(shell(number))