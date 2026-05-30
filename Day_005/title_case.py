
def title_case(_str)-> str:
    _str = _str.split()
    new_list = list()
    for i in _str:
        if 97 <= ord(i[0]) <= 122:
            num = ord(i[0]) - 32
            new_str = chr(num)+i[1:]
            new_list.append(new_str)
    return " ".join(new_list)
_str = "hello world"
print(title_case(_str))


# clean version
"""
def title_case(s):
    words = s.lower().split()    # lowercase everything first
    new_list = []
    for word in words:
        if 97 <= ord(word[0]) <= 122:    # now always lowercase
            new_str = chr(ord(word[0]) - 32) + word[1:]
            new_list.append(new_str)
    return " ".join(new_list)

print(title_case("the QUICK brown FOX")) 
"""
