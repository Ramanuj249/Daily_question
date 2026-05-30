def common_in_list(_list1, _list2)-> list:
    result = list()
    _set2 = set(_list2)
    for i in _list1:
        if i in _set2:
            result.append(i)
    return result

print(common_in_list([1,2,3,4], [4,5]))