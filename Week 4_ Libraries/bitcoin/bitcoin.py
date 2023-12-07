import requests, sys

def main():

    amount = conv_to_usd() * bitcoin_is_float(sys.argv)
    print(f"${amount:,.4f}")


def bitcoin_is_float(args): # checks if the given argument is valid

    if len(args) < 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            return float(args[1])

        except ValueError:
            sys.exit("Command-line argument is not a number")

def conv_to_usd(): # gets the rate of bitcoin to USD
    btcn_database = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

    return float(btcn_database["bpi"]["USD"]["rate"].replace(",",""))

main()

