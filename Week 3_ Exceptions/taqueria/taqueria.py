menu = {
    "bajataco": 4.25, 
    "burrito": 7.50, 
    "bowl": 8.50, 
    "nachos": 11.00, 
    "quesadilla": 8.50, 
    "superburrito": 8.50, 
    "superquesadilla": 9.50, 
    "taco": 3.00,
    "tortillasalad": 8.00
}

total = 0


while True:
    try:
        order = input("Item: ").lower().replace(" ", "")
        if order in menu:

            total += menu[order]
            print(f"Total: ${total:.2f}")

    except EOFError:
        break


