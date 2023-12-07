import pyfiglet, sys, random

# check whether or not sys.argv has any arguments
if len(sys.argv) == 1:
    chosen_font = random.choice(pyfiglet.FigletFont.getFonts())

elif len(sys.argv) == 3 and (sys.argv[1] in ("-f", "--font") and sys.argv[2] in pyfiglet.FigletFont.getFonts()):
    chosen_font = sys.argv[2]

else:
    sys.exit("Try again.")

figlet = pyfiglet.Figlet()

# set the font
figlet.setFont(font = chosen_font)

# output
print(figlet.renderText(input("Input: ")))






