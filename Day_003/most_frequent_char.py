
def most_freq_char(a):
    count = {}
    for i in a:
        if i not in count:
            count[i] = 1
        else:
            count[i] +=1
    return (max(count, key=count.get))

print(most_freq_char("madagasker"))

# Homework perform this without using the max keyword.

