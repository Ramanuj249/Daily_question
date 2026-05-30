def longest_word(_str)->str:
    max_len = 0
    word = ""
    for i in _str.split():
        if len(i)>max_len:
            max_len = len(i)
            word = i
    return word

print(longest_word("Hi my name is John"))