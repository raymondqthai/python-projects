# Currency Converter


# install module
get_ipython().run_line_magic('pip', 'install requests')


# load module
import requests


# load api
# free currency converter api - https://freecurrencyapi.com/
# create a freecurrencyapi account beforehand
# obtain api key
# API_KEY located on Dashboard > Default Key
# DON'T COPY API_KEY IT MIGHT NOT WORK FOR YOU
# GENERATE YOUR OWN
API_KEY = "fca_live_oayiNAdKsnFJXsAVu1veE4S6dO2fvIDKPOH1Bl4D"
# obtain url
# BASE_URL located on Request Playground > Generated Request URL
# remove everything from the link after "apikey="
# use f-string to inject our own API_KEY to the link after "apikey="
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"


# variable of currencies of interest
CURRENCIES = ["USD","EUR","JPY","GBP","CNY","CAD","AUD","CHF","HKD","SGD"]


# create a function to send a request to the api to send data back to use
# URL parameter
def convert_currency(base):
    # 
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        #print(data) # debug print data's key and values
        return data["data"]
    except:
        print("Invalid Currency")
        return None


# create a function for price amount the user want to convert
def price():
    while True:
        amount = input("What is the amount you would like to convert? ")
        if amount == "":
            amount = 1
            break
        elif amount.isnumeric:
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")
    return amount


def main():
    while True:
        try:
            base = input("Enter the base currency (q for quit): ").upper()
            if base == "Q":
                break
            # set default currency
            data = convert_currency(base)
            if not data:
                continue
            # delete base since we know by default
            del data[base]
            #print(data) # debug print data's values only
            amounts = price()
            # create a for loop to better display the currency converter
            for ticker, value in data.items():
                print(f"{ticker}: {value:.6f} x {amounts:.2f} = {value*amounts:.2f}")
        except KeyError: # handle error when base input registered an empty string
            continue
main()
