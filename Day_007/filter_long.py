def filter_long_words(_list, n):
    return list(filter(lambda x: len(x)>n, _list))

print(filter_long_words(["cat", "elephant", "dog", "butterfly"], 4))