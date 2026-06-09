lst = [1,2,3,2,1]

def is_palidrome(lst):
    left = 0
    right = len(lst)-1
    while left<=right:
        if lst[left]!=lst[right]:
            return False
        else:
            left +=1
            right -=1
    return True
print(is_palidrome(lst))