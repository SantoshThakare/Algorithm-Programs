


def _anagram():
    if sorted(_str1) == sorted(_str2):
        return "string are Anagram"

    else:
        return "string are not Anagram"

if __name__ == '__main__':

    _str1 = input("Enter the First String : ")
    _str2 = input("Enter the Second String: ")
    result = _anagram()
    print(result)