from Day_002.check_prime import check_prime

def primes_in_range(a, b):
    result = []
    for i in range(a,b+1):
        if check_prime(i):
            result.append(i)
    return result

print(primes_in_range(10,20))