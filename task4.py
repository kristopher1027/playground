resources = [
    {"name": "Laptop", "available": 0},
    {"name": "Mouse", "available": 0},
    {"name": "Keyboard", "available": 3}
]
#
resources = [r for r in resources if r["available"] != 0]
print(resources)