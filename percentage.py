"""
"""
__author__ = "merc1er"
__version__ = "0.1"
__email__ = "corentin@mercier.link"

################################################################################
import requests
import json
################################################################################

##################
#### currency ####
##################

req = requests.get("https://api.fixer.io/latest")
rate = req.json()

krw = rate['rates']['KRW']

#################
#### COINONE ####
#################

req = requests.get("https://api.coinone.co.kr/ticker/")
btc_coinone = json.loads(req.text)

sell = float(btc_coinone['last']) / krw

###############
#### G-DAX ####
###############

req = requests.get("https://api.gdax.com/products/BTC-EUR/ticker")
btc_gdax = json.loads(req.text)

buy = float(btc_gdax['ask'])

print(sell/buy)