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

##################
#### currency ####
##################

try:
	req = requests.get("https://api.fixer.io/latest")
	rate = req.json()

	krw = rate['rates']['KRW']
except:
	print("Error: KRW rate was not fetched")
	sys.exit()

#################
#### COINONE ####
#################

# try:
# 	req = requests.get(url = "https://api.coinone.co.kr/ticker/",
# 												params = {"currency":currency})
# 	btc_coinone = req.json()

# 	sell = float(btc_coinone['last']) / krw
# except:
# 	print("Error: could not fetch Coinone")
# 	sys.exit()

################
#### KORBIT ####
################

try:
	req = requests.get("https://api.korbit.co.kr/v1/ticker?currency_pair=" + currency.lower() + "_krw")
	btc_korbit = req.json()

	sell = float(btc_korbit['last']) / krw
except:
	print("Error: could not fetch Korbit")
	sys.exit()

###############
#### G-DAX ####
###############

try:
	req = requests.get("https://api.gdax.com/products/" + currency.upper() + "-EUR/ticker")
	btc_gdax = req.json()

	buy = float(btc_gdax['ask'])
except:
	print("Error: could not fetch GDAX")
	sys.exit()

#################
#### display ####
#################

premium = (sell/buy - 1) * 100 # quick mafs

info = "<small>buy: " + str(buy) + " - sell: " + str('%.2f'%sell) + "</small>"
print("<p class='text-center'>" + currency.upper() + ": " + str('%.2f'%premium) + "% "
	+ info + "</p>")
