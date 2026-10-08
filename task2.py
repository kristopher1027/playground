def borrow(resource, quantity):
    if not isinstance(quantity, int) or quantity <= 0:
        return False, "Quantity must be a positive whole number."
    if quantity > resource["available"]:
        return False, "Not enough stock."
    resource["available"] -= quantity
    return True, "Success"
borrow()