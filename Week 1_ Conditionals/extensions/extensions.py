def main():
    filename = input("File name: ").lower().strip()
    ext(filename)

def ext(file):
    if file.endswith((".jpeg", ".jpg")):
        print(f'image/jpeg')
    elif file.endswith((".gif", ".png")):
        print(f'image/{file.split(".")[-1]}')
    elif file.endswith((".pdf", ".zip")):
        print(f'application/{file.split(".")[-1]}')
    elif file.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")


main()