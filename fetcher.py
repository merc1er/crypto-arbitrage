#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# fetches the market price from the exchanges
#


import requests
import json


####################
#### krw to eur ####
####################
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
def korbit(currencyIn):
    try:
    	req = requests.get("https://api.korbit.co.kr/v1/ticker?currency_pair=" +
    										      currencyIn.lower() + "_krw")
    	btc_korbit = req.json()
    	price = float(btc_korbit['last']) / krwCalc()
    	return price
    except Exception as e:
        errorHandler('Could not fetch from korbit API')

###############
#### G-DAX ####
###############
def gdax(currencyIn):
    try:
    	req = requests.get("https://api.gdax.com/products/" +
                                            currencyIn.upper() + "-EUR/ticker")
    	btc_gdax = req.json()
    	price = float(btc_gdax['ask'])
    	return price
    except Exception as e:
        errorHandler('Could not fetch from gdax')