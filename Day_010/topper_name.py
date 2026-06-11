students = [
    {"name": "Shivam", "grades": {"math": 85, "science": 90, "english": 78}},
    {"name": "John",   "grades": {"math": 60, "science": 55, "english": 70}},
    {"name": "Sara",   "grades": {"math": 95, "science": 88, "english": 92}},
    {"name": "Mike",   "grades": {"math": 40, "science": 45, "english": 50}}
]

result = {
    "math":    "Sara",   # highest in math
    "science": "Sara",   # highest in science
    "english": "Sara"    # highest in english
}
_dict = dict()

for i in students:
    name=i["name"]
    math = i["grades"]["math"]
    science = i["grades"]["science"]
    english = i["grades"]["english"]
    if _dict["math_marks"]>math:
        _dict["math"] = name
    else:
        _dict["math_marks"] =
    elif _dict["science_marks"]>science:
        _dict["math"] = name
    elif _dict["english_marks"]>english:
        _dict["math"] = name