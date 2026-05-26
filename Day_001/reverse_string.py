def reverse_string(str):
    _list = list(str)
    new_str = []
    while _list:
        new_str.append(_list.pop())
    return "".join(new_str)

print(reverse_string("ramanuj"))