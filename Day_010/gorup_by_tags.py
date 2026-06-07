data = [
    {"id": 1, "tags": ["JS", "Python"]},
    {"id": 2, "tags": ["Python", "Java"]},
    {"id": 3, "tags": ["Java", "JS"]}
]

def group_by_tags(data)->dict:
    new_dict = dict()
    for i in data:
        item_id = i["id"]
        for j in i["tags"]:
            if j in new_dict:
                new_dict[j].append(item_id)
            elif j not in new_dict:
                new_dict[j] = [item_id]

    return new_dict

print(group_by_tags(data))



"""
def group_by_tags(data):
    result = {}
    for item in data:
        for tag in item["tags"]:
            result.setdefault(tag, []).append(item["id"])
    return result
"""
