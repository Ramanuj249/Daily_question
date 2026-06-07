students = [
    {"id": 1, "name": "Shivam", "marks": [85, 90, 78]},
    {"id": 2, "name": "John", "marks": [60, 55, 70]},
    {"id": 3, "name": "Sara", "marks": [95, 88, 92]},
    {"id": 4, "name": "Mike", "marks": [40, 45, 50]}
]



def check_passfail(_dict)->list:
    result = list()
    for i in _dict:
        temp={}
        temp["id"]=i["id"]
        temp["name"]=i["name"]
        temp["avg"]=round(sum(i["marks"])/len(i["marks"]),2)
        temp["status"]= "pass" if temp["avg"]>=50 else "fail"
        result.append(temp)
    return result

print(check_passfail(students))