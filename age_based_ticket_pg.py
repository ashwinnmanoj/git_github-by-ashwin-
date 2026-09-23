#concepts:if,else,elif,compassion operation
age = int(input("enter your age"))
if age <5:
    price = 0
elif age < 18:
    price = 200
else:
    price = 300
    print("Ticket price",price)
    