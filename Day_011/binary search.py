

def binary_search(lst, target):
    left = 0
    right = len(lst)-1
    while left<=right:
        mid = (left+right)//2
        if lst[mid] == target:
            return mid
        elif lst[mid]<target:
            left = mid +1
        elif lst[mid]>target:
            right = mid -1

    return -1

lst = [1,2,3,4,5,6,7,8,9]
target = 9

print(binary_search(lst,target))