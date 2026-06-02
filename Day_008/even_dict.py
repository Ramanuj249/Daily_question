def even_dict(_lst)->dict:
    return {x:x*x*x for x in _lst if x%2==0}

print(even_dict([1,2,3,4,5,6,7,8,9,10]))
