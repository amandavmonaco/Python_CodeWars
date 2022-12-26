def filter_list(l):
    newList = [];
    for i in l:
        if type(i) == int:
            newList.append(i)
    return newList

if __name__ == '__main__':
    print(filter_list([1,2,'a','b']))