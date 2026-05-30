

def rotate_list(_list, num)-> list:
    for i in range(num):
        a = _list.pop()
        _list.insert(0,a)
    return(_list)

_list = [1,2,3,4,5]
num=2

print(rotate_list(_list, num))

# Slicing method

"""
def rotate_list(lst, k):
    k = k % len(lst)        # handles k larger than list length
    return lst[-k:] + lst[:-k]
"""