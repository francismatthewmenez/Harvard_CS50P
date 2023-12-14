def main():
    x = shorten(input())
    print(x)


def shorten(word):
    novowel = []

    for c in word:
        match c:
            case "a"|"e"|"i"|"o"|"u"|"A"|"E"|"I"|"O"|"U":
                novowel.append("")
            case _:
                novowel.append(c)

    return ''.join(novowel)


if __name__ == "__main__":
    main()
