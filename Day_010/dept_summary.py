employees = [
    {"id": 1, "name": "Shivam", "dept": "Engineering", "salary": 70000},
    {"id": 2, "name": "John", "dept": "Marketing", "salary": 50000},
    {"id": 3, "name": "Sara", "dept": "Engineering", "salary": 90000},
    {"id": 4, "name": "Mike", "dept": "Marketing", "salary": 60000},
    {"id": 5, "name": "Alice", "dept": "Engineering", "salary": 80000}
]

"""
{
    "Engineering": {"total": 240000, "count": 3, "avg": 80000},
    "Marketing":   {"total": 110000, "count": 2, "avg": 55000}
}
"""

new_dict = dict()
for i in employees:
    key = i["dept"]
    if key not in new_dict:
        new_dict[key] = {"total": i["salary"], "count":1, "avg":0}
    else:
        new_dict[key]["total"] +=i["salary"]
        new_dict[key]["count"] +=1
        new_dict[key]["avg"] = new_dict[key]["total"] // new_dict[key]["count"]

print(new_dict)