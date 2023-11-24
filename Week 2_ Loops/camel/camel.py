def main():
    camelCase = input("camelCase: ")
    camel_to_snake(camelCase)

def camel_to_snake(txt):

    print("snake_case: ", end="")

    for c in txt: # iterates through every character in the text provided by the user
        
        if c.isupper() == True: # if the character being iterated is uppercase
            print("_" + c.lower(), end="") 
        else: 
            print(c, end="")
    print()


main()




