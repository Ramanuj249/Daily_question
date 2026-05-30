
def group_by_len(_list)->dict:
    count = dict()
    for i in _list:
        if len(i) not in count:
            count[len(i)] = [i]
        else:
            count[len(i)].append(i)
    return count

_list = ["hi", "hello", "hey", "world", "ok"]
print(group_by_len(_list))

"""
def group_by_length(words):
    count = {}
    for word in words:
        count.setdefault(len(word), []).append(word)
    return count
"""