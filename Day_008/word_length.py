def word_length(_lst)->dict:
    return {x: len(x) for x in _lst}

print(word_length(["apple", "banana", "watermelon", "cherry"]))

