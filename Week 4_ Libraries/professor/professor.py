import random

def main():

    i = 0
    score = 0
    lvl = get_level()
    lvl = lvl


    for i in range(10):

        k = 0

        nums = list(generate_integer(lvl))
        summ = 0

        for j in nums:
            summ += j

        while True:

            answer = int(input(f"{nums[0]} + {nums[1]} = "))

            if answer == summ:
                score += 1
                i += 1
                break
            else:
                print("EEE")
                k += 1

                if k == 3:
                    print(f"{nums[0]} + {nums[1]} = {summ}")
                    i += 1
                    break
                else:
                    continue

    print(f"Score: {score}")


def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):

    match level:
        case 1:
            x, y = random.randint(0,9), random.randint(0,9)
        case 2:
            x, y = random.randint(10,99), random.randint(10,99)
        case 3:
            x, y = random.randint(100,999), random.randint(100,999)

    return x, y


if __name__ == "__main__":
    main()
