transactions = [
    {"id": 1, "user": "Shivam", "type": "credit", "amount": 5000},
    {"id": 2, "user": "John", "type": "debit", "amount": 2000},
    {"id": 3, "user": "Shivam", "type": "debit", "amount": 1000},
    {"id": 4, "user": "John", "type": "credit", "amount": 3000},
    {"id": 5, "user": "Shivam", "type": "credit", "amount": 2000},
    {"id": 6, "user": "Sara", "type": "debit", "amount": 500}
]

# def user_balance(trans):
#     _dict = dict()
#     for i in trans:
#         name = i["user"]
#         trans_type = i["type"]
#         if name in _dict:
#             if trans_type=="debit":
#                 _dict[name] -= i["amount"]
#             else:
#                 _dict[name] +=i["amount"]
#         else:
#             if trans_type=="debit":
#                 _dict[name] = -i["amount"]
#             else:
#                 _dict[name] = +i["amount"]
#     return _dict


def user_balance(trnas):
    _dict = {}
    for i in trnas:
        name = i["user"]
        _dict.setdefault(name, 0)
        if i["type"] == "debit":
            _dict[name] -= i["amount"]
        else:
            _dict[name] += i["amount"]
    return _dict

print(user_balance(transactions))