def count_vowel(a):
    count = 0
    for i in a:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            count +=1
    return count

print(count_vowel("AEIOUaeiou"))