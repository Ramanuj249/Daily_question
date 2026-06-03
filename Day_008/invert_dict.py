def invert_dict(_dict)->dict:
    return {j:i for i, j in _dict.items()}

print(invert_dict({1:"a", 2:"b"}))