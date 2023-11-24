grocery_lists = {}

while True:
    try:
        item = input().upper()

        if item in grocery_lists:
            grocery_lists[item] = grocery_lists[item] + 1


        else:
            grocery_lists[item] = 1

    except EOFError:
        for grocery, count in sorted(grocery_lists.items()):
            print(count, grocery)
        break