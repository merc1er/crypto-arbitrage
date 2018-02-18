"""
"""
__author__ = "merc1er"
__version__ = "0.1"
__email__ = "corentin@mercier.link"

################################################################################
import requests
import json
################################################################################

#################
#### COINONE ####
#################

req = requests.get("https://api.coinone.co.kr/ticker/")
# print(req.status_code)
btc = json.loads(req.text)

print("Coinone:")
print(btc['last'])

###############
#### G-DAX ####
###############

req = requests.get("https://api.gdax.com/products/BTC-EUR/ticker")
# print(req.status_code)
btc = json.loads(req.text)

print("G-DAX:")
print(btc['ask'])