def remove_duplicate(a):
    _list = []
    for i in a:
        if i not in _list:
            _list.append(i)
        else:
            continue
    return _list

print(remove_duplicate(["a", "b", "b", "a", "c"]))