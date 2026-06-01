def sum_of_even_square(_lst):
    return sum(list(map(lambda x: x*x, filter(lambda x:x%2==0, _lst))))
print(sum_of_even_square([1,2,3,4]))