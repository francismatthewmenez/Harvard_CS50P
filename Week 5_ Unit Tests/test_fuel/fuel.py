def main():
    txt = input("Fraction: ")
    print(gauge(convert(txt)))

def convert(fraction):

    fuel = fraction.split("/")
    try:
        x = int(fuel[0])
        y = int(fuel[1])
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError
    elif x>y:
        raise ValueError
    else:
        return int(round((x/y), 2)*100)


def gauge(percentage):

    if 99 <= percentage <= 100:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
