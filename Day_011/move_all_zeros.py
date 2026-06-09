


def moves_zeros(lst):
    left = 0
    right = 0
    for i in range(len(lst)):
        if lst[right] ==0:
            right +=1
        else:
            lst[right], lst[left] = lst[left], lst[right]
            left +=1
            right +=1

    return lst

lst = [0,0,1,2,0,3]
print(moves_zeros(lst))