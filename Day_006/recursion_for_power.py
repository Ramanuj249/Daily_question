def power(num_1, num_2):
    if num_2 <= 0:
        return 1
    else:
        return num_1 * power(num_1, num_2-1)

print(power(2,3))