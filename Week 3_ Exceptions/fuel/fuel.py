def main():

    print(check_fuel())


def check_fuel():
    while True:
        try:
            fuel = input("Fraction: ")

            x = int(fuel.split("/")[0])
            y = int(fuel.split("/")[1])

            percent = int(round((x/y), 2)*100)


            if percent > 100:
                continue
            elif 99 <= percent <= 100:
                return "F"
            elif percent <= 1:
                return "E"
            else:
                return f"{percent}%"

        except(ValueError, ZeroDivisionError):
            pass


main()