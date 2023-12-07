import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        else:
            break
    except ValueError:
        continue

the_number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        else:
            if guess == the_number:
                print("Just right!")
                break
            elif guess > the_number:
                print("Too large!")
                continue
            else:
                print("Too small!")
                continue

    except ValueError:
        continue



