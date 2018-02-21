"""
"""
__author__ = "merc1er"
__version__ = "0.3"
__email__ = "corentin@mercier.link"

################################################################################
import sys
import requests
import json
################################################################################

# checking arguments
currency = sys.argv[1]
if currency not in "btcethltcbch":
	print("Invalid argument")
	sys.exit()

##################
#### currency ####
##################

req = requests.get("https://api.fixer.io/latest")
rate = req.json()

krw = rate['rates']['KRW']

#################
#### COINONE ####
#################

req = requests.get(url = "https://api.coinone.co.kr/ticker/",
											params = {"currency":currency})
btc_coinone = req.json()

sell = float(btc_coinone['last']) / krw

###############
#### G-DAX ####
###############

req = requests.get("https://api.gdax.com/products/" + currency.upper() + "-EUR/ticker")
btc_gdax = req.json()

buy = float(btc_gdax['ask'])

premium = (sell/buy - 1) * 100
print("<p>" + currency.upper() + ": " + str('%.2f'%premium) + "% </p>")
