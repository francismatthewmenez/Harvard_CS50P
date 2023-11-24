def main():
    emoji = input()
    print(convert(emoji))

def convert(face):
    newmain = face.replace(":)", "🙂").replace(":(", "🙁")
    return newmain

main()

