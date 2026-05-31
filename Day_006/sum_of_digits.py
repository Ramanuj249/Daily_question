def sum_of_digits(num) -> int:
    if num <=9:
        return num
    last_digit = num % 10
    answer = num // 10
    return last_digit + sum_of_digits(answer)

print(sum_of_digits(99999))

# print(999 % 10)
# print(999//10)