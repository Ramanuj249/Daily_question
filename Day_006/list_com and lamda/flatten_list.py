def flatten_list(_list)->list:
    return [item for sublist in _list for item in sublist]

print(flatten_list([[1,2], [3,4], [5,6]]))