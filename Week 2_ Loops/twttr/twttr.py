text = input("Input: ")
print("Output: ", end="")

for c in text:
    match c:
        case "a"|"e"|"i"|"o"|"u"|"A"|"E"|"I"|"O"|"U":
            print("", end="")
        case _:
            print(c, end="")

print()
