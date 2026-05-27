def largest_number(a):
    right_num = a[0]
    for i in range(1, len(a)):
        if a[i] > right_num:
            right_num = a[i]
    return right_num

a = [1,2,3,4,5,6,7,8,9]
print(largest_number(a))