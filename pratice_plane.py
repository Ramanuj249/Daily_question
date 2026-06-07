_list = [1,2,3,4,5,6,8,7]
largest=_list[0]
smallest=0
for i in _list:
    if i>largest:
        smallest = largest
        largest = i
    elif i<largest and i>smallest:
        smallest = i

print(smallest)