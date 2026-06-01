def capitalize_words(_lst):
    return list(map(lambda x: x[0].upper() + x[1:], _lst))

print(capitalize_words(["hello", "world", "python"]))