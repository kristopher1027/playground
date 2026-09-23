def summarise_amounts(raw_values):
    total = 0
    rejected = 0
    
    for raw in raw_values:
        try:
            value = int(raw)
            if value >= 0:
                total += value
            else:
                rejected += 1  
        except ValueError:
            rejected += 1      
            
    return {"total": total, "rejected": rejected}