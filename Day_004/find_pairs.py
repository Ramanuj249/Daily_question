
def find_pair(_list, num) -> list:
    _pairs = list()
    for i in range(len(_list)):
        for j in range(i+1, len(_list)):
            if _list[i] + _list[j] == num:
                _pairs.append((_list[i], _list[j]))
    return _pairs

_list = [1,2,3,4,5]
num = 6

print(find_pair(_list, num))