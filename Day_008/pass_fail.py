def pass_fail(_dict)->dict:
    return {i: "pass" if j>50 else "fail" for i, j in _dict.items()}

students = {
    "Aman": 85,
    "Riya": 45,
    "Rahul": 72,
    "Priya": 38
}
print(pass_fail(students))