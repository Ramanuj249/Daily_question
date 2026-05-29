def flatten_list(_list) -> list:
    _new = list()
    for i in _list:
        if isinstance(i, list):
            for j in i:
                _new.append(j)
        else:
            _new.append(i)
    return _new

_list = [1,2,3, [4, 5], [6, 7, 8]]
print(flatten_list(_list))


"""
For deep nesting you need recursion — we'll cover that later when we get to recursion topics. 
For now your solution is perfect for single level nesting!
"""