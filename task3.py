transactions = [
    {"fellow": "Ada", "quantity": 2},
    {"fellow": "John", "quantity": 4},
    {"fellow": "Ada", "quantity": 3},
    {"fellow": "Grace", "quantity": 1},
    {"fellow": "John", "quantity": 2}
]

def total_per_fellow(transactions):
    totals = {}
    for t in transactions:
        name = t["fellow"]
        if name in totals:
            totals[name] += t["quantity"]
        else:
            totals[name] = t["quantity"]
    return totals

print(total_per_fellow(transactions))