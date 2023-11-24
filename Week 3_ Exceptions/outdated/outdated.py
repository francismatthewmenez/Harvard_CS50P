months = {
    "january": '01',
    "february": '02',
    "march": '03',
    "april": '04',
    "may": '05',
    "june": '06',
    "july": '07',
    "august": '08',
    "september": '09',
    "october": '10',
    "november": '11',
    "december": '12'
}

while True:


    date = input("Date: ")

    # Check if the day exceeds 31

    # Check if the month (in word form) is in the input
    if date.split()[0].lower() in months and "," in date:
        newdate = date.replace(",","").split()
        if int(newdate[1]) > 31:
            continue
        else:
            print(f"{int(newdate[2]):04}-{months[newdate[0].lower()]}-{int(newdate[1]):02}")
            break

    # Check if the date is in number format m/d/yyyy
    elif "/" in date:
        date = date.split("/")
        try:
            if int(date[1]) > 31 or int(date[0]) > 12:
                continue
            else:
                date = [int(date_digit) for date_digit in date]
                print(f"{date[2]:04}-{date[0]:02}-{date[1]:02}")
                break
        except ValueError:
            continue

    else:
        pass

