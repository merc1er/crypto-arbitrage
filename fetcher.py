#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# fetches the market price from the exchanges
#

import sys
import requests
import json

FIXER_API_KEY = ''

def errorHandler(errors):
    print('Error: ' + errors)
    sys.exit();

####################
#### krw to eur ####
####################
def krwCalc():
    try:
        endpoint = 'http://data.fixer.io/api/latest?access_key='
        req = requests.get(endpoint + FIXER_API_KEY)
        krw_string = req.json()['rates']['KRW']
        krw = float(krw_string)
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
        errorHandler('Could not fetch from korbit')

#################
#### COINONE ####
#################

def coinone(currencyIn):
    try:
        req = requests.get(url = "https://api.coinone.co.kr/ticker/",
                                                params = {"currency":currency})
        btc_coinone = req.json()
        price = float(btc_coinone['last']) / krwCalc()
        return price
    except Exception as e:
        errorHandler('Could not fetch from coinone')

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

###############
### BITTREX ###
###############

def bittrex(currencyIn):
    """
    not deployed
    """
    try:
        req = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=" +
                                            currencyIn.upper() + "-btc")
        price_json = req.json()
        price = float(price_json['ask'])
        return price
    except Exception as e:
        errorHandler('Could not fetch from bittrex')

###################
### CRYPTONATOR ###
###################

def cryptonator(currencyIn, market):
    try:
        req = requests.get("https://api.cryptonator.com/api/full/" +
                                                    currencyIn.lower() + "-eur")
        callback = req.json()
        markets = callback['ticker']['markets']
        if market == 'bitfinex':
            return markets[0]['price']
        if market == 'cexio':
            return markets[1]['price']
        if market == 'exmo':
            return markets[2]['price']
        if market == 'kraken':
            return markets[3]['price']
        if market == 'livecoin':
            return markets[4]['price']
        if market == 'wexnz':
            return markets[5]['price']
    except Exception as e:
        errorHandler('Could not fetch from cryptonator')

################################################################################
#
# ADD MARKETS APIs HERE
#
