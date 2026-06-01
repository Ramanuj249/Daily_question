def sorted_by_2nd(_list)->list:
    return sorted(_list, key = lambda x: x[1])

print(sorted_by_2nd([(1,3), (2,1), (3,2)]))