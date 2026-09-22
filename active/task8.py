def reserve_stock(stock, order):
    remaining = stock.copy()
    for item, quantity in order:
        if quantity > stock[item]:
            raise ValueError("Insufficient stock")
        remaining[item] = stock[item] - quantity
    return remaining


    # To fix this, you should perform all checks and deductions directly on your remaining copy, and use .get() to handle missing items safely.
    def reserve_stock(stock, order):
    remaining = stock.copy()
    
    for item, quantity in order:
        # 1. Use .get() to handle items not present in stock (defaults to 0)
        current_stock = remaining.get(item, 0)
        
        # 2. Check against the UPDATED tracking inventory, not the original
        if quantity > current_stock:
            raise ValueError(f"Insufficient stock for {item}")
        
        # 3. Deduct from the updating pool
        remaining[item] = current_stock - quantity
        
    return remaining
