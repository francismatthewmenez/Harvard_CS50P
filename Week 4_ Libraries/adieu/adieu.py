import inflect

p = inflect.engine()
names = []

while True:

    try:
        names.append(input("Name: "))

    except EOFError:
        break

names = p.join(names)
print(f"Adieu, adieu, to {names}")
