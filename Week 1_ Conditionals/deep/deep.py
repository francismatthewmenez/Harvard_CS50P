def main():
    txt = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    is42(txt)

def is42(word):
    match word:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")

main()