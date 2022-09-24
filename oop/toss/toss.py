import toss_class as a

if __name__ == '__main__':
    mycoin = a.coin()
    mycoin.toss()
    print(mycoin.get_result())
    mycoin.set_result('foo bar baz')
    print(mycoin.get_result())
    