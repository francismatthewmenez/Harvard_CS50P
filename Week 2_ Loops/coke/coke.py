amount = 50
while amount > 0:
    print("Amount Due: " + str(amount))
    coin = int(input("Insert Coin: "))
    match coin:
        case 25 | 10 | 5:
            amount -= coin
        case _:
            continue

print("Change Owed: " + str(amount * -1)) if amount < 0 else print("Change Owed: 0")
