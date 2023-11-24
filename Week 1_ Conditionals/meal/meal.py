def main():
    num_of_hrs = convert(input("What time is it? "))

    if 7.0 <= num_of_hrs <= 8.0:
        print("breakfast time")
    elif 12.0 <= num_of_hrs <= 13.0:
        print("lunch time")
    elif 18.0 <= num_of_hrs <= 19.0:
        print("dinner time")
    else:
        pass


def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)


    return float(hour + (minute/60))


if __name__ == "__main__":
    main()




