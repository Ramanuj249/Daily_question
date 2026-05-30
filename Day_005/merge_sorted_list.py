_list1 = [1,3,5]
_list2 = [2,4,6]
_list = []
for i in _list1:
    for j in _list2:
        if i<j:
            _list.append(i)

        else:
            _list.append(j)
print(_list)