def finding_missing_number(n):
    _max = len(n) +1
    _missing = (_max*(_max+1)//2) - sum(n)
    return _missing

print(finding_missing_number([1,3,4,5]))