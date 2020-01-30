#!/usr/bin/env python3

#
# fetches the market price from the exchanges
#

import sys
import requests
from .secret import FIXER_API_KEY


def krw_rate():
    """ Converts 1 EUR to KRW"""
    if FIXER_API_KEY == '':
        print('Input your fixer.io API key in secrets.py')
        sys.exit()

    endpoint = 'http://data.fixer.io/api/latest?access_key='
    req = requests.get(endpoint + FIXER_API_KEY)
    req.raise_for_status()
    krw_string = req.json()['rates']['KRW']
    krw = float(krw_string)
    return krw


def korbit(currency_in):
    """ Returns the value of 1 currency_in according to korbit """
    korbit_endpoint = 'https://api.korbit.co.kr/v1/ticker?currency_pair='
    req = requests.get(korbit_endpoint + currency_in.lower() + "_krw")
    req.raise_for_status()
    btc_korbit = req.json()
    price = float(btc_korbit['last']) / krw_rate()
    return price


def coinone(currency_in):
    """ Returns the value of 1 currency_in according to coinone """
    req = requests.get(url="https://api.coinone.co.kr/ticker/",
                       params={"currency": currency_in})
    req.raise_for_status()
    btc_coinone = req.json()
    price = float(btc_coinone['last']) / krw_rate()
    return price


def gdax(currency_in):
    """ Returns the value of 1 currency_in according to Coinbase Pro """
    req = requests.get("https://api.pro.coinbase.com/products/" +
                       currency_in.upper() + "-EUR/ticker")
    req.raise_for_status()
    btc_gdax = req.json()
    price = float(btc_gdax['ask'])
    return price


def bittrex(currency_in):
    """ Returns the value of 1 currency_in according to bittrex """
    bittrex_endpoint = ('https://bittrex.com/api/v1.1/public'
                        '/getticker?market=')
    req = requests.get(bittrex_endpoint + "usd-" + currency_in.upper())
    price_json = req.json()
    price = float(price_json['result']['Last'])
    return price


def cryptonator(currency_in, market):
    req = requests.get("https://api.cryptonator.com/api/full/" +
                       currency_in.lower() + "-eur")
    req.raise_for_status()
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
    return False

###############################################################################
#
# ADD MARKETS APIs HERE
#
