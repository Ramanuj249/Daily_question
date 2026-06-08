products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 80000},
    {"id": 2, "name": "Phone", "category": "Electronics", "price": 40000},
    {"id": 3, "name": "Shirt", "category": "Clothing", "price": 1500},
    {"id": 4, "name": "Pants", "category": "Clothing", "price": 2000},
    {"id": 5, "name": "Headphones", "category": "Electronics", "price": 5000},
    {"id": 6, "name": "Shoes", "category": "Clothing", "price": 3000}
]

result =\
{
    "Electronics": {"count": 3, "total": 125000, "most_expensive": "Laptop"},
    "Clothing":    {"count": 3, "total": 6500,   "most_expensive": "Shoes"}
}

def category_summary(_dict)->dict:
    new_dict = dict()
    for i in products:
        new_category = i["category"]
        if new_category not in new_dict:
            new_dict[new_category] = {"count": 1, "total": i["price"], "most_expensive": i["name"], "max_price": i["price"]}
        else:
            new_dict[new_category]["count"] +=1
            new_dict[new_category]["total"] += i["price"]
            if i["price"] > new_dict[new_category]["max_price"]:
                new_dict[new_category]["most_expensive"] = i["name"]

    for category in new_dict:
        del new_dict[category]["max_price"]

    return (new_dict)

print(category_summary(products))