def main():

    txt = input("Greeting: ").lower().strip()
    greeting(txt)

def greeting(text):

    if "hello" in text:
        print("$0")
    elif text[0] == "h":
        print("$20")
    else:
        print("$100")


main()