
def word_freq(_str)->dict:
    _str = _str.split(" ")
    count = dict()
    for i in _str:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count

print(word_freq("hi my name is john and my name is john"))


"""
def word_frequency(sentence):
    count = {}
    for word in sentence.split():
        count[word] = count.get(word, 0) + 1
    return count
"""