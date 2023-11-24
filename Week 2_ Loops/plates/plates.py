def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # 1) Is the text alphanumeric?
    if s.isalnum():

        # 2) Does the text fit between 2 to 6 characters?
        if 2 <= len(s) <= 6:

            # 3) Are the first two characters of a text alphabetical?
            if s[0:2].isalpha():

                # (Optional) Are there numbers on the text?
                iter_count = 0
                for c in s:
                    if c.isnumeric():
                        firstnum = c

                        # 4) If there are numbers on the text, is the first number reading from left to right not a 0?
                        if firstnum == "0":
                            return False # 4) is false

                        else:

                            # 5) Are the rest of the characters from the first number onward all numbers (no alphas)?
                            if s[iter_count:].isnumeric():
                                return True
                            elif s[iter_count:].isnumeric() == False:
                                return False

                    else: # If (Optional) is false, keep iterating. If there are no numbers, True.
                        iter_count += 1
                        continue
                return True

            else: # 3) is false
                return False

        else: # 2) is false
            return False

    else: # 1) is false
        return False

main()
