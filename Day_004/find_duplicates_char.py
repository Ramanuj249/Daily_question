def find_duplicate_char(_str) -> list:
    count = dict()
    for i in _str:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    _list = list()
    for i in count:
        if count[i]>1:
            _list.append(i)
    return _list

a = "programming"
print(find_duplicate_char(a))


"""
# your way ✅
if i in count:
    count[i] += 1
else:
    count[i] = 1

# shorter way ✅
count[i] = count.get(i, 0) + 1
"""