def fiter_negative_and_square(_list):
    return list(map(lambda x: x*x, filter(lambda x: x<0, _list)))

print(fiter_negative_and_square([1,-2,3,-4,5,-6]))