lst = [1,8,6,2,5,4,8,3,7]
left = 0
right = len(lst)-1
print(right)
max = lst[left]*lst[right]
all_container = []
while left<right:
    if lst[left]*lst[right]>max:
        new_num = max
        left +=1
        right +=1
    else:
        left+=1
        right -=1
print(new_num)