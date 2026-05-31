def even_square(num)->list:
    return [i*i for i in range(1, num+1) if i%2 ==0]
print(even_square(10))