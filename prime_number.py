def CheckPrime():
    '''
    :return:  prime number from 1 to 1000 range
    '''
    list_ = []
    for number in range(1, 1000):
        if number > 1:
            for iterate in range(2, int(number / 2) + 1):
                if (number % iterate) == 0:
                    break
            else:
                list_.append(number)

    return list_


if __name__ == '__main__':
    m1 = CheckPrime()
    print(m1)

