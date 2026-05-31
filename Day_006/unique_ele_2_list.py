def unique_elements(_list1, _list2)-> list:
    new_list = list()
    for i in _list1:
        if i not in _list2:
            new_list.append(i)
    for j in _list2:
        if j not in _list1:
            new_list.append(j)
    return new_list

print(unique_elements([1,2,3], [4,5,6]))

# use set insted of list and then also use one line for the for loops. Homework.
