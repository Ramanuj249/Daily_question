employees = [
    {"name": "Shivam", "hours": 45},
    {"name": "John", "hours": 38},
    {"name": "Sara", "hours": 50},
    {"name": "Mike", "hours": 40},
    {"name": "Alice", "hours": 35}
]
def calculate_salary(list1):
    _list = list()
    for i in list1:
        _dict = dict()
        if i["hours"]>40:
            normal = 40*100
            extra = (i["hours"]-40)*150
            total = normal + extra
            _dict["name"] = i["name"]
            _dict["regular"] = normal
            _dict["overtime"] = extra
            _dict["total"] = total
            _list.append(_dict)
        else:
            normal = i["hours"]*100
            total = normal
            _dict["name"] = i["name"]
            _dict["regular"] = normal
            _dict["overtime"] = 0
            _dict["total"] = total
            _list.append(_dict)

    return _list

print(calculate_salary(employees))