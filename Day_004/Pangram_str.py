

def pangram_str(_str):
    _dict = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
        'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
        'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
        'y': 0, 'z': 0
    }
    _str = _str.lower()
    _str = _str.replace(" ", "")
    for i in _str:
        _dict[i] += 1
    return False if 0 in _dict.values() else True

a = "the quick brown fox jumps over the lazy dog"
print(pangram_str(a))


# Suggeestion: _dict = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}


# def is_pangram(s):
#     s = s.lower()
#     alphabet = set('abcdefghijklmnopqrstuvwxyz')
#     return alphabet.issubset(set(s))   # all 26 letters present in s?
#
# a = "the quick brown fox jumps over the lazy dog"
# print(is_pangram(a))   # True
# print(is_pangram("hello world"))   # False