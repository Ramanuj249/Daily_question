
def merge_sorted_list(_list1, _list2)-> list:
    result = []
    i =0
    j =0
    while i < len(_list1) and j<len(_list2):
        if _list1[i] < _list2[j]:
            result.append(_list1[i])
            i += 1
        else:
            result.append(_list2[j])
            j += 1
    result = result + _list1[i:]
    result = result + _list2[j:]
    return result

_list1 = [1,3,5,7,8,9] # len = 3
_list2 = [2,4,6] # len =3
print(merge_sorted_list(_list1, _list2))