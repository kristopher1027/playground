Easy  |  6 minutes  |  10 marks
A ticket should cost 7 units. The developer expects three tickets to produce the integer 21.
def ticket_total(price, quantity):
    total = price * quantity
    print(total)
amount = ticket_total("7", 3)
print(amount)
Q1 Part C
Rewrite the function and its call so the function returns an integer total and does not print internally. Print the returned result once outside the function. You may assume numeric integer inputs in the corrected version. [3 marks]
def ticket_total(price, quantity):
    total = int(price) * quantity
    return total
amount = ticket_total("7", 3)
print(amount)
Q1 Part A
Before running the code, write the exact two output lines and state the value and type of amount. [4 marks]
Q1 Part B
Explain why multiplication behaves this way and why amount does not contain the printed result. [3 marks]
* it because when you multiply a string by an integer it brings it out as the number of number multiplying it 
* amount return no printed result but return None because they was no return value
