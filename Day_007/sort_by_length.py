def sort_by_length(_list)->list:
    return sorted(_list, key=lambda x: len(x))

print(sort_by_length(["cat", "elephant", "dog", "butterfly"]))