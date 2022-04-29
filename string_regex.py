import re

def str_regex(username):
    patterns = 'santosh'
    if re.search(patterns,username):
        return 'found a match!'
    else:
        return ('Not matched !')

if __name__ == '__main__':

    print(str_regex("santosh"))
    print(str_regex(("sachin")))
