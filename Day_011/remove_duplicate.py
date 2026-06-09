def remove_duplicate(lst):
    left = 0
    right = 1
    for i in range(len(lst)-1):
        if lst[left] != lst[right]:
            left +=1
            right +=1
        else:
            del lst[right]

    return lst

lst = [1,1,1,1,1]
print(remove_duplicate(lst))


"""
def remove_duplicates(lst):
    left = 0
    for right in range(1, len(lst)):
        if lst[right] != lst[left]:
            left += 1
            lst[left] = lst[right]
    return left + 1   # length of unique elements

"""