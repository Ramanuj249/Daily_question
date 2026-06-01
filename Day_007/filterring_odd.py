def filter_odd(_list):
    return list(filter(lambda x: x%2==0, _list))

print(filter_odd([1,2,3,4,5,6,7]))