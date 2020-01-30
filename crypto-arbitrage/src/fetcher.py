#!/usr/bin/env python3

#
# fetches the market price from the exchanges
#

import sys
import requests
from .secret import FIXER_API_KEY


def errorHandler(errors):
    print('Error: ' + errors)
    sys.exit()


def krwCalc():
    """ Converts 1 EUR to KRW"""
    if FIXER_API_KEY == '':
        errorHandler('Input your fixer.io API key in secrets.py')
    try:
        endpoint = 'http://data.fixer.io/api/latest?access_key='
        req = requests.get(endpoint + FIXER_API_KEY)
        krw_string = req.json()['rates']['KRW']
        krw = float(krw_string)
        return krw
    except Exception:
        errorHandler("Couldn't fetch from fixer.io")


def korbit(currency_in):
    """ Returns the value of 1 currency_in according to korbit """
    try:
        korbit_endpoint = 'https://api.korbit.co.kr/v1/ticker?currency_pair='
        req = requests.get(korbit_endpoint + currency_in.lower() + "_krw")
        btc_korbit = req.json()
        price = float(btc_korbit['last']) / krwCalc()
        return price
    except Exception:
        errorHandler('Could not fetch from korbit')


def coinone(currency_in):
    """ Returns the value of 1 currency_in according to coinone """
    try:
        req = requests.get(url="https://api.coinone.co.kr/ticker/",
                           params={"currency": currency_in})
        btc_coinone = req.json()
        price = float(btc_coinone['last']) / krwCalc()
        return price
    except Exception:
        errorHandler('Could not fetch from coinone')


def gdax(currency_in):
    """ Returns the value of 1 currency_in according to Coinbase Pro """
    try:
        req = requests.get("https://api.pro.coinbase.com/products/" +
                           currency_in.upper() + "-EUR/ticker")
        btc_gdax = req.json()
        price = float(btc_gdax['ask'])
        return price
    except Exception:
        errorHandler('Could not fetch from Coinbase Pro')


def bittrex(currency_in):
    """ Returns the value of 1 currency_in according to bittrex """
    bittrex_endpoint = ('https://bittrex.com/api/v1.1/public'
                        '/getticker?market=')
    req = requests.get(bittrex_endpoint + "usd-" + currency_in.upper())
    price_json = req.json()
    price = float(price_json['result']['Last'])
    return price


def cryptonator(currency_in, market):
    try:
        req = requests.get("https://api.cryptonator.com/api/full/" +
                           currency_in.lower() + "-eur")
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
    except Exception:
        errorHandler('Could not fetch from cryptonator')

###############################################################################
#
# ADD MARKETS APIs HERE
#
