def first_non_reapt(_str):
    _dict = dict()
    for i in _str:
        if i not in _dict:
            _dict[i] = 1
        else:
            _dict[i] +=1

    for k,v in _dict.items():
        if v == 1:
             return k
    return -1

print(first_non_reapt("aab"))


"""
def first_non_repeat(_str):
    _dict = {i: _str.count(i) for i in _str}
    return next((k for k, v in _dict.items() if v == 1), -1)
"""