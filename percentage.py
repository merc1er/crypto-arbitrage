#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "merc1er"
__version__ = "0.5"
__email__ = "corentin@mercier.link"


################################################################################
import sys
from fetcher import *
################################################################################



# Default Global Variables
marketIn = ['gdax']
marketOut = ['korbit']
markets = [ 'korbit',
            'gdax',
            'coinone',
            'bitfinex',
            'cexio',
            'exmo',
            'kraken',
            'livecoin',
            'wexnz']
accepted_currencies = ['btc', 'bch', 'eth', 'ltc']


##################
####  display ####
##################

def display(currency, html):
    # print("Buy from", marketIn[0], "- Sell to", marketOut[0])
    buy = fetch(marketIn[0], currency)
    sell = fetch(marketOut[0], currency)
    premium = (sell / buy - 1) * 100
    if html:
        info = "<small>buy: " + str('%.2f'%buy) + " - sell: " \
        							+ str('%.2f'%sell) + "</small>"
        print("<p class='text-center'>" + currency.upper() + ": " \
        						+ str('%.2f'%premium) + "% " + info + "</p>")
    else:
        info = "buy: " + str('%.2f'%buy) + " - sell: " +\
                                                    str('%.2f'%sell)
        print(currency.upper() + ": " + str('%.2f'%premium) + "% " + info)

##############
### checks ###
##############

def verifyArgs():
    if len(sys.argv) < 2:
        print("Usage:\npython percentage.py cryptocurrency [marketIn] " +
                                                        "[marketOut] [options]")
        sys.exit()
    # checking length
    if len(sys.argv) > 3:
        marketIn[0] = sys.argv[2].lower()
        marketOut[0] = sys.argv[3].lower()
    # checking argument 1
    currency = sys.argv[1].lower()
    if currency not in accepted_currencies:
        if currency in ['-h', 'help', '--help']:
            print("Usage:\npython percentage.py [cryptocurrency]")
            sys.exit()
        print("Invalid argument")
        print("Supported currencies are:", accepted_currencies)
        sys.exit()
    # and now the rest
    if marketIn[0] not in markets or marketOut[0] not in markets:
        print("Invalid market name")
        sys.exit()
    return currency

#############
### FETCH ###
#############

def fetch(market, currency):
    if market == "gdax":
        return gdax(currency)
    if market == "coinone":
        return coinone(currency)
    if market == "korbit":
        return korbit(currency)
    else:
        return float(cryptonator(currency, market))

################################################################################
# main

def main():
    currency = verifyArgs()
    if len(sys.argv) > 2 and sys.argv[-1] in ['--html']:
        display(currency, True);
    else:
        display(currency, False)

if __name__ == '__main__':
    main()
