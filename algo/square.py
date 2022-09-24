def trang(number):
    if number == 1:
        return 1
    elif number < 1:
        return 0
    return trang(number-1) + number

def square(n):
    return trang(n) + trang(n-1)

if __name__ == "__main__":
    number = int(input("Enter Number: "))
    print("square root is: ",square(number))