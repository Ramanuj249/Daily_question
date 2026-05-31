def reverse_string(_str)-> str:
    if len(_str)<=1:
        return _str
    else:
        return _str[-1] + reverse_string(_str[:-1])

print(reverse_string("hello"))