
def armstrong_range(a,b)-> list:
    _list = list()
    for i in range(a,b+1):
        if i >100:
            _str = str(i)
            power = len(_str)
            count = 0
            for j in _str:
                sum = int(j)**power
                count +=sum
            if count == i:
                _list.append(i)
    return _list

print(armstrong_range(1,10000))