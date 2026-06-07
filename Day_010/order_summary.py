# def order_summary(_dict)->dict:
#     new_dict = dict()
#     for i in _dict:
#         new_cat = i["status"]
#         if new_cat not in new_dict:
#             new_dict[new_cat] = [i["customer"]]
#         else:
#             new_dict[new_cat].append(i["customer"])
#     return new_dict


def order_summary(_dict):
    result = dict()
    for i in _dict:
        result.setdefault(i["status"], []).append(i["customer"])
    return result

orders = [
    {"id": 1, "customer": "Shivam", "items": ["laptop", "mouse", "keyboard"], "status": "delivered"},
    {"id": 2, "customer": "John", "items": ["phone", "charger"], "status": "pending"},
    {"id": 3, "customer": "Sara", "items": ["tablet"], "status": "delivered"},
    {"id": 4, "customer": "Mike", "items": ["laptop", "headphones"], "status": "cancelled"},
    {"id": 5, "customer": "Alice", "items": ["phone", "case", "charger"], "status": "pending"}
]

print(order_summary(orders))



