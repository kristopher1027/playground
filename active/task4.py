def ticket_total(price, quantity):
    total = int(price) * quantity
    print(total)
amount = ticket_total("7", 3)
print(amount)

# You need to pass the price as a number (an integer or a float) instead of a string (text wrapped in quotes).
# In Python, passing a string "7" and multiplying it by an integer 3 results in string repetition. The program simply repeats the character "7" three times
