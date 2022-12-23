#my original solution
def shortcut(s):
    s = s.replace('a','')
    s = s.replace('e','')
    s = s.replace('i','')
    s = s.replace('o', '')
    s = s.replace('u', '')
    return s


if __name__ == '__main__':
    print(shortcut('hello'))
    print(shortCut('welcome to new york'))