def main():
    expression = input("Expression: ")
    print(round(interpreter(expression), 1))


def interpreter(math):
    x = float(math.split()[0])
    y = math.split()[1]
    z = float(math.split()[2])

    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z

main()




