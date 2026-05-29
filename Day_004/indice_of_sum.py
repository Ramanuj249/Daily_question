
# understand this its important question

def indice_of_sum(_list,num)->list:
    for i in range(len(_list)):
        for j in range(i, len(_list)):
            if _list[i] + _list[j]==num:
                return [i,j]
    return []

a = [2, 7, 11, 15]
b = 17

print(indice_of_sum(a,b))