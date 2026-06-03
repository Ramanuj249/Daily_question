def merge_dict(_dict1, _dict2):
    return {k:v for d in [_dict1, _dict2] for k,v in d.items()}

print(merge_dict({1:"a", 2: "b", 3: "c"}, {4: "d", 5:"e"}))