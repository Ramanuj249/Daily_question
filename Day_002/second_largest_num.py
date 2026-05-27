

def second_largest(_list):
    small = 0
    large = 0
    for i in range(len(_list)):
        if _list[i]>large:
            small = large
            large = _list[i]
        elif _list[i]>small:
            small = _list[i]
    return small
_list = [1,2,3,9,8,7,6,5,4]
print(second_largest(_list))