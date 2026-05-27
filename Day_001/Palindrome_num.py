def palindrome_num(n):
    n = str(n)
    return n==n[::-1]

print(palindrome_num(121))
print(palindrome_num(122))