

def anagram_string(a,b):
    count = {}
    for i in a:
        count[i]=count.get(i,0)+1
    for i in b:
        count[i]=count.get(i,0)-1
    for val in count.values():
        if val !=0:
            return False
    return True

a = "abc"
b = "acb"
print(anagram_string(a,b))