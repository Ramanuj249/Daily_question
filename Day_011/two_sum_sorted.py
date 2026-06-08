

def two_sum_sorted(lst, target):
    left = 0
    right = len(lst)-1
    while left < right:
        sum=lst[left] + lst[right]
        if sum == target:
            return [left, right]
        elif sum > target:
            right-=1
        elif sum<target:
            left +=1

lst = [1,2,3,4,5,6,7,8,9]
target = 7
print(two_sum_sorted(lst, target))