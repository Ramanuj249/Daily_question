
# def reverse_dict(_dict)->dict:
#     new_dict = dict()
#     for key, value in _dict.items():
#         new_dict[value] = key
#     return new_dict



# thik about duplicates values.

def reverse_dict(_dict)-> dict:
    new_dict = dict()
    for key, value in _dict.items():
        if value not in new_dict.keys():
            new_dict[value] = []
        new_dict[value].append(key)  # adding each value in the new_dict if is change by above line or not.
    return new_dict

print(reverse_dict({1:'a', 2:'b', 3:'c', 4:'a'}))

