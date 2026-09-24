Challenging  |  13 minutes  |  25 marks
You receive a list of strings representing whole-unit amounts. Return a dictionary with total and rejected. Use Python int(raw) conversion: surrounding whitespace is accepted. A converted amount of zero or more is valid. Negative amounts and strings that cannot be converted must each increase rejected by one. An empty list returns both values as zero. Do not change the input.
```py
def summarise_amounts(raw_values):
    total = 0
    for raw in raw_values:
        try:
            total += int(raw)
        except:
            pass
    return {"total": total, "rejected": 0}

Required example: ["10", " 5 ", "bad", "-3", "0", ""] must return {"total": 15, "rejected": 3}. Inputs are always strings; no other type validation is required.
```
## Q4 Part A
Identify three defects or risks in the supplied function. Explain why a bare except can hide an unrelated failure. [6 marks]

* 1. it does not check for the rejected 
* 2. it process negative number incorrect instead of rejecting it 
* 3. it uses except without specifying the error name
Why a bare except hides failures: is because if there is an bug it will it can ignore it and pass instead of showing the error message

## ## Q4 Part C
Write four executable assertions covering the required mixed example, empty input, all rejected input, and a valid zero. State why checking only total could miss a bug. [8 marks]
```py
# 1. Empty input
assert summarise_amounts([]) == {"total": 0, "rejected": 0}

# 2. All rejected input
assert summarise_amounts(["bad", "-5", "abc"]) == {"total": 0, "rejected": 3}

# 3. Valid zero
assert summarise_amounts(["0", "  0  "]) == {"total": 0, "rejected": 0}

```

If you only check the "total", your test will pass even if the "rejected" 
## Q4 Part B
Rewrite the function to meet every rule. Catch only the expected conversion exception. [11 marks]
```py
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
```
