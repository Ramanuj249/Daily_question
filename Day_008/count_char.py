def count_char(_str)-> dict:
    return {x: _str.count(x) for x in set(_str)}

print(count_char("hello"))