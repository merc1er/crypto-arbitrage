"""
"""
__author__ = "merc1er"
__version__ = "0.3.1"
__email__ = "corentin@mercier.link"

################################################################################
import sys
import requests
import json
################################################################################


#################
####  errors ####
#################
def errorHandler(errors):
    print('Error: ' + errors)
    sys.exit();

def display():
		premium = (sell(currency)/buy(currency) - 1) * 100 # quick mafs

		info = "<small>buy: " + str(buy(currency)) + " - sell: " + str('%.2f'%sell(currency)) + "</small>"
		print("<p class='text-center'>" + currency.upper() + ": " + str('%.2f'%premium) + "% "
			+ info + "</p>")

#################
#### display ####
#################
def krwCalc():
	try:
		req = requests.get("https://api.fixer.io/latest")
		rate = req.json()
		krw = rate['rates']['KRW']
		return krw
	except Exception as e:
		errorHandler("Couldn't fetch from fixer")

################
#### KORBIT ####
################
def sell(currencyIn):
    try:
    	req = requests.get("https://api.korbit.co.kr/v1/ticker?currency_pair=" + currencyIn.lower() + "_krw")
    	btc_korbit = req.json()
    	sell = float(btc_korbit['last']) / krwCalc()
    	return sell
    except Exception as e:
        errorHandler('Could not fetch from korbit API')

###############
#### G-DAX ####
###############
def buy(currencyIn):
    try:
    	req = requests.get("https://api.gdax.com/products/" + currencyIn.upper() + "-EUR/ticker")
    	btc_gdax = req.json()
    	buy = float(btc_gdax['ask'])
    	return buy
    except Exception as e:
        errorHandler('Could not fetch from gdax')

# checking arguments
if len(sys.argv) < 2:
	print("Usage:\npython percentage.py [cryptocurrency]")
	sys.exit()

currency = sys.argv[1]
if currency not in ['btc', 'bch', 'eth']:
	if currency in ['-h', 'help', '--help']:
		print("Usage:\npython percentage.py [cryptocurrency]")
		sys.exit()
	print("Invalid argument")
	sys.exit()
else:
    display()
