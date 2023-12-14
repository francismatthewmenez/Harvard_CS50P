def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # 1) Is the text... Alphanumeric? In between 2 and 6 characters? First two characters are letters?
    if (s.isalnum() and 2 <= len(s) <= 6) and s[0:2].isalpha():

        # Are there numbers on the text?
        iter_count = 0
        for c in s:
            if c.isnumeric():
                firstnum = c

                # If there are numbers on the text, is the first number reading from left to right not a 0?
                if firstnum == "0":
                    return False

                else:

                    # Are the rest of the characters from the first number onward all numbers (no alphas)?
                    if s[iter_count:].isnumeric():
                        return True
                    elif s[iter_count:].isnumeric() == False:
                        return False

            else:
                iter_count += 1
                continue
        return True

    else:
        return False

if __name__ == "__main__":
    main()
