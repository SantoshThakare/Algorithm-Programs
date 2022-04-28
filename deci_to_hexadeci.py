conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}



def decimal_to_hexadecimal(decimal):
    hexadecimal = ''
    while (decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        print(remainder)
        print(hexadecimal)
        decimal = decimal // 16
        print(decimal)

    return hexadecimal

if __name__ == '__main__':

    decimal_number = 12
    print("The hexadecimal form of", decimal_number,
      "is", decimal_to_hexadecimal(decimal_number))