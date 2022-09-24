import toss_class as a

if __name__ == '__main__':
    for i in range(10):
        mycoin = a.coin()
        mycoin.toss()
        print(f'your result is: {mycoin.get_result()}')
    