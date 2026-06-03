def filter_dict(_dict,num)-> dict:
    return {k:v for k, v in _dict.items() if v>num}

print(filter_dict({"a":1, "b":3, "c":4, "d":5}, 3))